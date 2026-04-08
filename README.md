# Short Video Publisher Site

Short Video Publisher の公開サイトと Direct Post 審査導線です。

## 構成

- ルート
  - GitHub Pages で公開する静的ページ
- `cloudflare-worker/`
  - OAuth callback と Direct Post を扱う Worker

## GitHub Pages 側で公開するファイル

- `index.html`
- `tour.html`
- `workspace.html`
- `help.html`
- `review.html`
- `demo.html`
- `privacy-policy.html`
- `terms-of-service.html`
- `callback.html`

`index.html` は外部ユーザー向けの product website です。
`tour.html` は reviewer と利用者向けの product walkthrough です。
`workspace.html` は TikTok Login Kit、creator info review、Direct Post、publish status を扱う creator workspace です。
`help.html` は workflow と support の公開ヘルプページです。
`review.html` と `demo.html` は古い URL からの redirect 用に残しています。

## 再申請メモ

- TikTok 再申請用の録画手順・Portal 記入文・提出前チェックは
  - `artifacts/review/resubmission-kit-20260408.md`

## TikTok Developers に登録する URL

- `Web URL`
  - `https://1125haruki.github.io/short-video-publisher-site/`
- `Product Tour`
  - `https://1125haruki.github.io/short-video-publisher-site/tour.html`
- `Publisher Workspace`
  - `https://1125haruki.github.io/short-video-publisher-site/workspace.html`
- `Sandbox Workspace`
  - `https://1125haruki.github.io/short-video-publisher-site/workspace.html?mode=sandbox`
- `Help Center`
  - `https://1125haruki.github.io/short-video-publisher-site/help.html`
- `Privacy Policy URL`
  - `https://1125haruki.github.io/short-video-publisher-site/privacy-policy.html`
- `Terms of Service URL`
  - `https://1125haruki.github.io/short-video-publisher-site/terms-of-service.html`
- `Redirect URI`
  - `https://tiktok-short-video-publisher-auth.chillsabo1125.workers.dev/tiktok/callback`
- `Sandbox Redirect URI`
  - `https://tiktok-short-video-publisher-auth-sandbox.chillsabo1125.workers.dev/tiktok/callback`
- `Health Check`
  - `https://tiktok-short-video-publisher-auth.chillsabo1125.workers.dev/tiktok/health`
- `Sandbox Health Check`
  - `https://tiktok-short-video-publisher-auth-sandbox.chillsabo1125.workers.dev/tiktok/health`

## 運用前に確認する項目

- Worker 側の `ALLOWED_ORIGIN`
- Worker 側の `TOKEN_SINK_URL` か保存先
- Worker 側の `TIKTOK_CLIENT_KEY` / `TIKTOK_CLIENT_SECRET` / `STATE_SECRET`
- Privacy Policy / Terms / Help Center のサポート窓口

## 実務メモ

- GitHub Pages は無料
- Cloudflare Workers も小規模なら無料枠で始めやすい
- `Redirect URI` は静的ページではなく server-side endpoint が必要
- `Website URL` は login page ではなく public website にする
- live な TikTok 認可導線は `workspace.html` のような separate app page に分ける
- workflow 動画と product walkthrough は `tour.html` にまとめる
- Direct Post 審査では `creator_info/query` を使って privacy / interaction / duration を creator に見せる
- production app の scope は `user.info.basic,video.upload,video.publish` を基準にする
- `PULL_FROM_URL` で使う動画URLは、自分が所有・検証できる domain か URL prefix に寄せる
- Sandbox で Direct Post を試す時は `workspace.html?mode=sandbox` を使う
- Cloudflare Worker の sandbox 環境は `npm run deploy:sandbox` で deploy する
- local 自動投稿は `automation/README.md` を入口にし、公開審査導線とは分けて運用する
- 緊急時の復旧用 snapshot は `archive/approved_production_20260317/` に残してある
