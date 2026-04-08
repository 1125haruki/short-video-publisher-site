# Portal URL Update 2026-04-09

TikTok reviewer comment:

> Website URL should not contain TikTok.

Update these three fields in TikTok Developer Portal before resubmitting:

- Website URL
  - `https://1125haruki.github.io/short-video-publisher-site/`
- Privacy Policy
  - `https://1125haruki.github.io/short-video-publisher-site/privacy-policy.html`
- Terms of Service
  - `https://1125haruki.github.io/short-video-publisher-site/terms-of-service.html`

Checks completed:

- All three URLs return `200`
- Public site links are aligned to the new neutral GitHub Pages path
- Worker `APP_RETURN_URL` points to the new workspace path
- Production and sandbox worker health are both healthy

Do not change for this revision:

- Redirect URI
- Sandbox Redirect URI
- Worker domain names
- App scopes

Remaining reviewer-facing task after these URL changes:

- Replace the demo video so the recorded browser URL also uses `short-video-publisher-site`
