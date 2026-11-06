# ScoreIQ static Android app website

The deployable files are in `site/`. They use HTML and CSS with no package installation, site JavaScript, API, or runtime build. The Android app is a separate project. The supplied delivery package contains the source verification notes and release review items.

## Preview and validate

Serve from the directory **above** the extracted `score_iq_web` project to emulate the GitHub Pages project subpath:

```sh
mkdir -p preview
ln -s "$(pwd)/score_iq_web/site" preview/score_iq_web
python3 -m http.server 8765 --bind 127.0.0.1 --directory preview
```

Open `http://127.0.0.1:8765/score_iq_web/`. On Windows, copy the contents of `site` to `preview\score_iq_web` or create a directory junction in place of the symlink. The standard Python server returns its own 404 document. GitHub Pages serves `site/404.html` for missing pages.

From inside the project, run `python3 scripts/validate_site.py`.

## Release review

1. Verify a developer-controlled support inbox that receives external requests and is monitored for ScoreIQ. Test inbound receipt and a reply. Add the visible, copyable address and `mailto:` links on Contact, Delete Account and Data Request, using distinct subject lines. On the deletion and data request pages, explain how to submit from the sign-in address, ownership verification and the confirmed retention policy. Remove the `RELEASE_BLOCKER_SUPPORT` comments once the route is usable without the app.
2. Have the owner approve the website policies against the actual release and Google Play Data Safety form. Confirm developer identity, age/eligibility language, diagnostics and analytics collection, payment and entitlement records, deletion coverage and exceptions, regional processing and applicable rights. Replace the draft notices with approved update dates and remove the `RELEASE_BLOCKER_LEGAL` comments once review is complete.
3. Keep the Google Play status text until the public listing shows ScoreIQ for `com.reotech.scoreiq`. Then use the official Google Play badge asset with the verified destination in the header, hero and final section, and link it in the footer. Recheck signed out in the intended distribution region. A pending public listing can be represented by the existing status text.
4. If a custom domain is later approved and verified, change canonical and social URLs, sitemap and robots sitemap reference, 404 paths and the validator base to the final host. Deploy `app-ads.txt` only if you have verified authorized seller records and can publish at the Play developer website hostname root. Keep the contact website and mailbox checks separate.

## GitHub publishing

The chosen host is GitHub Pages for the separate `raheemreo/score_iq_web` project. The workflow verifies links on main and uploads only `site/` once the release blockers are resolved.

1. Create an empty repository at [GitHub New Repository](https://github.com/new) under `raheemreo` named `score_iq_web`. Choose visibility explicitly. Public Pages supports public repositories on GitHub Free. A private source repository requires a compatible GitHub plan to serve public Pages. If the target already exists, clone it and review its history before integrating these files.
2. From the extracted project folder, initialize Git if necessary and push to the new **empty** target using your authorized GitHub session.

   ```sh
   git init -b main
   git add .
   git commit -m "Build ScoreIQ static website"
   git remote add origin https://github.com/raheemreo/score_iq_web.git
   git push -u origin main
   ```

3. In the target repository, select **Settings → Pages → Build and deployment → Source → GitHub Actions**. Run **Verify and deploy static site** from the Actions tab after the release review. Future pushes to main run it automatically. See [GitHub’s Pages source setup](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
4. Verify the deployed Actions run commit, HTTPS homepage and every public policy URL while signed out. Retest the off-app support link and the store status or badge. Verify the alias and an unknown path, which should return HTTP 404. A project-subpath robots file can advertise the sitemap locally, but crawler directives are normally fetched at hostname root. Submit the project sitemap directly in the search provider tools if applicable.
5. Once the live contact channel and public URLs work, enter the approved privacy and deletion URLs in Play Console. Use the final Developer Website URL in the store listing. Changes to the Android project’s currently null external URLs are a separate Android release task.
