# TikTok Automation

このディレクトリは `Short Video Publisher` の内部運用用です。  
TikTok 審査提出や画面収録では使いません。

## 位置づけ

- 公開審査導線
  - `index.html`
  - `tour.html`
  - `help.html`
  - `workspace.html?mode=sandbox`
- 内部運用導線
  - この `automation/` 配下
  - 接続済み session と local script を使った補助運用

## 前提

- production app は `video.publish` 承認済み
- production worker は `user.info.basic,video.upload,video.publish` を使う
- 公開 workspace の審査向け UI には automation 導線を出していない

## 収録・再申請時の注意

- `automation/` の内容は TikTok reviewer に見せない
- `session export`、bundle JSON、local script は審査動画に含めない
- 再申請時は `artifacts/review/resubmission-kit-20260408.md` を正本として扱う

## 投稿スクリプト

```bash
export TIKTOK_CLIENT_KEY='...'
export TIKTOK_CLIENT_SECRET='...'

python3 automation/publish_tiktok_job.py \
  --job-file /Users/takasuharuki/dev26/ショート動画/state/publish_jobs/publish_gen_zatsugaku_20260316_001.json \
  --check-status
```

## 既定動作

- `video.publish` scope があれば Direct Post
- なければ Upload API fallback
- `tiktok` ブロックが job に無い場合は既定値を補完

## 注意

- token や session JSON は機密情報として扱う
- token が revoke されたら再接続が必要
- 緊急時は `archive/approved_production_20260317/` の snapshot を参照できる
