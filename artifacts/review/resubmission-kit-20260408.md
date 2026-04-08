---
project_id: short-video-publisher-site
created_at: 2026-04-08
purpose: tiktok_direct_post_resubmission
---

# TikTok Direct Post 再申請キット

## 1. これで用意できたもの

- 公開サイトは `Direct Post` 前提の外部向け製品説明に更新済み
- `workspace.html` は `creator settings -> disclosure -> consent -> Direct Post -> status` の流れに整理済み
- production / sandbox の scope は `user.info.basic,video.upload,video.publish` に整理済み
- この文書に、録画手順・Portal 記入文・提出前チェックを固定済み

## 2. 再申請で必要なもの

- 1本の画面収録動画
- 最新の Website URL / Privacy Policy / Terms URL
- TikTok Developer Portal に貼る説明文
- 動画内で実演した内容と一致する scope 設定

## 3. 収録前チェック

- Website URL
  - `https://1125haruki.github.io/short-video-publisher-site/`
- Workspace URL
  - `https://1125haruki.github.io/short-video-publisher-site/workspace.html?mode=sandbox`
- Privacy Policy
  - `https://1125haruki.github.io/short-video-publisher-site/privacy-policy.html`
- Terms of Service
  - `https://1125haruki.github.io/short-video-publisher-site/terms-of-service.html`
- Sandbox callback
  - `https://tiktok-short-video-publisher-auth-sandbox.chillsabo1125.workers.dev/tiktok/callback`
- Sandbox health
  - `https://tiktok-short-video-publisher-auth-sandbox.chillsabo1125.workers.dev/tiktok/health`

収録前に確認すること:
- sandbox app が TikTok Developer Portal で有効
- sandbox creator でログインできる
- `workspace.html?mode=sandbox` で `Connect TikTok` が開く
- 接続後に `video.publish` を含む session scope が見える
- `Load Creator Posting Settings` が成功する
- 使う MP4 URL は公開URLである

## 4. 画面収録のやり方

### 収録設定

- 収録時間は 2分から4分
- ブラウザは Chrome か Safari の通常UI
- 画面は desktop 幅
- 文字が読める倍率で固定
- 途中で別タブやローカルファイルを見せない

### 収録手順

1. `index.html` を開く
2. サイト名 `Short Video Publisher` を見せる
3. 製品説明、`Privacy Policy`、`Terms of Service` が公開されていることを見せる
4. `Open Publisher Workspace` を押して `workspace.html?mode=sandbox` に移動する
5. `Connect TikTok` を押す
6. sandbox TikTok で認証する
7. workspace に戻ったら、接続済み creator と scope が見えることを見せる
8. `Load Creator Posting Settings` を押す
9. privacy options、interaction availability、duration limit が読み込まれることを見せる
10. `Public MP4 URL` に公開動画URLを入れる
11. `TikTok title / caption` を入力する
12. privacy を手動で選ぶ
13. comment / duet / stitch のチェック欄を見せる
14. 必要に応じて `AI-generated content`、`paid partnership` など disclosure を入れる
15. consent checkbox をオンにする
16. `Direct Post to TikTok` を押す
17. `Publish ID` が返ることを見せる
18. `Check Publish Status` を押して status を確認する

### 収録中に言う説明

以下をそのまま読めばよい:

`Short Video Publisher is a public web product for creators.`

`Creators connect TikTok, load creator posting settings, choose privacy and disclosures, confirm consent, and publish directly from the workspace.`

`This demo is recorded on our sandbox environment for TikTok app review.`

`Now I open the public website, move to the creator workspace, connect TikTok, load creator settings, and send a Direct Post request.`

`The workspace shows creator privacy options, interaction availability, and duration limits before publishing.`

`The creator manually selects privacy, reviews disclosures, confirms consent, and submits the Direct Post request.`

`Finally, the workspace returns a publish ID and checks the publish status.`

## 5. Portal に貼る文面

### Product Description

`Short Video Publisher is a public web product that helps creators prepare original videos, connect TikTok, review creator posting settings, and publish directly to their TikTok profiles with creator-selected privacy and disclosure controls.`

### Review Steps

`Open the website URL, go to the publisher workspace, connect TikTok in sandbox, load creator posting settings, choose privacy and disclosures, confirm consent, send Direct Post, and verify publish status.`

### Scope Justification

- `user.info.basic`
  - `Used to show the connected TikTok creator account inside the workspace after Login Kit authorization.`
- `video.upload`
  - `Used by the Content Posting API flow to send the selected original video asset for TikTok publishing.`
- `video.publish`
  - `Used to initialize Direct Post after the creator reviews privacy, interaction, disclosure, and consent settings in the workspace.`

### Resubmission Note

`We updated the public website and workspace so the reviewer can clearly see the complete creator-facing Direct Post flow, including creator settings, manual privacy selection, disclosures, consent, and publish status.`

## 6. 提出前の最終チェック

- App Name が `Short Video Publisher`
- Website URL が公開トップURL
- Privacy Policy / Terms が公開URL
- Review video の内容と Portal 記入文が一致
- 動画内のUIが今の公開サイトと一致
- 動画内で `video.publish` を使う流れが見える
- 動画内で `creator_info` ベースの privacy options が見える
- 動画内で consent と publish status が見える
- 不要な scope を選んでいない

## 7. やってはいけないこと

- Upload fallback を主機能として説明する
- automation / session export / internal tool を動画に入れる
- personal use / private tool と説明する
- モック動画だけを提出する
- Website URL と違うドメインを動画に映す
- 動画で見せていない scope を申請する
