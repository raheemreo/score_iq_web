# ScoreIQ static Android app website

The public website source is in `site/`. It uses semantic HTML, CSS, local fonts and the nine owner-supplied promotional images. The support and privacy contact is `reodevelopers@gmail.com`.

## Pages

The homepage links to Privacy Policy, Terms of Service & Conditions, About Us, Contact & Support, Educational Disclaimer, Delete Account and Data Request. `/terms-and-conditions/` redirects to `/terms/`, which contains the same governing terms.

Account deletion and data requests can be sent by email without installing the app. Opening an email link starts a draft in the visitor’s email application. Sending that email submits the request.

## Preview and validation

Run `python3 -m http.server 8765 --directory site` from this directory to preview the homepage locally. The custom 404 uses the production `/score_iq_web/` prefix. Run `python3 scripts/validate_site.py` to validate the Pages subpath, sitemap, internal references and supplied-image inventory.

## Publishing

GitHub Actions validates and publishes `site/` on pushes to `main`. Enable **Settings → Pages → Source → GitHub Actions** in this repository. The publishing workflow is also available through **Actions → Verify and deploy static site → Run workflow**.

The intended URL is `https://raheemreo.github.io/score_iq_web/`. Confirm the deploy job succeeds and the live pages return HTTP 200 before distributing their URLs.

## App release configuration

The website policies were prepared from the app information and the owner’s publication instructions. Keep them aligned with app changes and Google Play Data Safety. Website publication does not update the Android app or Play Console fields.

The exact app package is `com.reotech.scoreiq`. Its public Google Play listing was unavailable when checked. The homepage therefore displays download-pending text. Add the official Play badge only after verifying the exact package’s live listing.

A custom domain and `app-ads.txt` require confirmed domain control and authorized seller records. No advertising record has been supplied for this deployment.
