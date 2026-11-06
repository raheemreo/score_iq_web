#!/usr/bin/env python3
"""Validate static links, fragments and sitemap under the GitHub Pages project path."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree

SITE = Path(__file__).resolve().parents[1] / "site"
BASE = "https://raheemreo.github.io/score_iq_web/"
BASE_PARTS = urlsplit(BASE)
PAGES = ("", "privacy/", "terms/", "about/", "contact/", "disclaimer/", "delete-account/", "data-request/")
PLAY = "https://play.google.com/store/apps/details?id=com.reotech.scoreiq"
ASSETS = {
    "hero-home-light", "feature-question-papers", "feature-current-affairs",
    "feature-study-cards", "feature-topic-practice", "feature-mistake-review",
    "feature-exams-categories", "feature-light-dark", "feature-dark-mode",
}

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []
        self.canonical = None
        self.headings = 0
        self.has_description = False
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.headings += 1
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs["href"]
        if tag == "meta" and attrs.get("name") == "description":
            self.has_description = bool(attrs.get("content"))
        if tag == "img":
            assert "alt" in attrs and attrs.get("width") and attrs.get("height"), attrs
            self.images.append(attrs)
        if tag in ("a", "link", "img"):
            key = "src" if tag == "img" else "href"
            if key in attrs:
                self.links.append(attrs[key])

def serve_path(relative):
    return SITE / (relative + "index.html" if not relative or relative.endswith("/") else relative)

def page_route(path):
    relative = path.relative_to(SITE).as_posix()
    return relative.removesuffix("index.html") if relative.endswith("index.html") else relative

def validate():
    documents = {path: Page(path) for path in SITE.rglob("*.html")}
    for route in PAGES:
        page = documents[serve_path(route)]
        assert page.canonical == BASE + route, route
        assert page.has_description and page.headings == 1, route
        assert "main" in page.ids, route
        for footer_route in PAGES[1:]:
            assert any(urljoin(BASE + route, link) == BASE + footer_route for link in page.links), (route, footer_route)

    checked = 0
    for path, page in documents.items():
        for link in page.links:
            assert link and not link.startswith(("javascript:", "http:")), (path, link)
            target = urlsplit(urljoin(BASE + page_route(path), link))
            if target.netloc != BASE_PARTS.netloc:
                if target.netloc == "play.google.com" and target.path == "/store/apps/details":
                    assert target.geturl() == PLAY, link
                continue
            assert target.path.startswith(BASE_PARTS.path), (path, link)
            relative = unquote(target.path[len(BASE_PARTS.path):])
            file = serve_path(relative)
            assert file.is_file(), (path, link)
            if target.fragment:
                assert unquote(target.fragment) in documents[file].ids, (path, link)
            checked += 1

    homepage = documents[serve_path("")]
    marketing = [img for img in homepage.images if img["src"].endswith(".webp")]
    assert len(marketing) == len(ASSETS) and {Path(img["src"]).stem for img in marketing} == ASSETS
    for img in marketing:
        assert img["alt"] and img["width"] == "1672" and img["height"] == "941", img
        if Path(img["src"]).stem != "hero-home-light":
            assert img.get("loading") == "lazy", img
    tree = ElementTree.parse(SITE / "sitemap.xml")
    urls = {node.text for node in tree.findall(".//{*}loc")}
    assert urls == {BASE + path for path in PAGES}
    assert f"Sitemap: {BASE}sitemap.xml" in (SITE / "robots.txt").read_text(encoding="utf-8")
    print(f"Passed: {len(PAGES)} canonical pages, {len(documents)} HTML documents, {checked} local references, {len(marketing)} promotional images.")

if __name__ == "__main__":
    validate()
