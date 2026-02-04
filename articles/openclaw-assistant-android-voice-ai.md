---
title: "OpenClaw Assistant - あなたのAIをAndroidの音声アシスタントにするOSSアプリ"
emoji: "🤖"
type: "tech"
topics: ["Android", "AI", "OpenSource", "音声認識", "Kotlin"]
published: true
---

## 📌 3行でわかるこの記事

- 🎤 **ホームボタン長押し**や**ウェイクワード**でAIアシスタントを起動できるAndroidアプリ
- 🔗 **OpenClaw**と連携して、Claude/GPT/Geminiなど任意のAIに接続可能
- 🌐 **完全オープンソース**で日英両対応、カスタマイズ自由

## はじめに

「OK Google」の代わりに、**自分のAI**を呼び出せたらいいと思いませんか？

**OpenClaw Assistant**は、Androidのシステムアシスタント機能を使って、[OpenClaw](https://github.com/openclaw/openclaw)経由で任意のAIバックエンドに接続できるオープンソースアプリです。

https://github.com/yuga-hashimoto/OpenClawAssistant

---

## 🚀 セットアップガイド（完全版）

### Step 1: OpenClawをインストール

まずサーバー（Mac/Linux/Windows）にOpenClawをセットアップします。

```bash
# npmでインストール
npm install -g openclaw

# または直接実行
npx openclaw
```

詳細: https://docs.openclaw.ai

### Step 2: OpenClawの設定（config.yaml）

`~/.openclaw/config.yaml` に以下を追加：

```yaml
# AIモデルの設定
defaults:
  model: anthropic/claude-sonnet-4  # または openai/gpt-4o, google/gemini-pro など

# APIキーの設定（環境変数でもOK）
providers:
  anthropic:
    apiKey: sk-ant-xxxxx  # Anthropic APIキー
  # または
  openai:
    apiKey: sk-xxxxx  # OpenAI APIキー

# 音声アシスタント用Webhookの設定
hooks:
  voice:
    path: /hooks/voice
    auth:
      bearer: "your-secret-token"  # 任意のトークン（アプリ側と一致させる）
```

### Step 3: OpenClawを起動

```bash
# ゲートウェイを起動（バックグラウンド）
openclaw gateway start

# ステータス確認
openclaw status
```

外部からアクセスするには、以下のいずれかが必要：
- **ポートフォワーディング**（ルーターで18080ポートを開放）
- **Cloudflare Tunnel**（推奨）
- **Tailscale/ZeroTier**などのVPN

#### Cloudflare Tunnelの例

```bash
# cloudflaredをインストール
brew install cloudflare/cloudflare/cloudflared

# トンネル作成
cloudflared tunnel create openclaw
cloudflared tunnel route dns openclaw your-subdomain.yourdomain.com

# 設定ファイル (~/.cloudflared/config.yml)
tunnel: <tunnel-id>
credentials-file: ~/.cloudflared/<tunnel-id>.json
ingress:
  - hostname: your-subdomain.yourdomain.com
    service: http://localhost:18080
  - service: http_status:404

# 起動
cloudflared tunnel run openclaw
```

### Step 4: Androidアプリのインストール

1. [Releases](https://github.com/yuga-hashimoto/OpenClawAssistant/releases) からAPKをダウンロード
2. インストール（「提供元不明のアプリ」を許可）

### Step 5: アプリの設定

1. アプリを開く
2. 右上の⚙️から設定画面へ
3. 以下を入力：

| 項目 | 値 |
|------|-----|
| **Webhook URL** | `https://your-subdomain.yourdomain.com/hooks/voice` |
| **Auth Token** | config.yamlで設定した`bearer`トークン |

4. 「Test Connection」で接続確認
5. 「Save」で保存

### Step 6: システムアシスタントに設定

1. Android設定 → アプリ → デフォルトのアプリ → デジタルアシスタント
2. 「OpenClaw Assistant」を選択
3. ホームボタン長押しで起動！

---

## ✨ 主な機能

### 🏠 ホームボタン長押しで起動

Googleアシスタントの代わりに、OpenClaw Assistantをデフォルトアシスタントに設定できます。

### 🎤 カスタムウェイクワード

「Open Claw」「Jarvis」「Computer」など、好きなウェイクワードを選択可能。

オフライン音声認識エンジン [Vosk](https://alphacephei.com/vosk/) を使用しているため、ウェイクワード検知はデバイス内で完結します。

### 🔊 音声入出力

- **音声認識**: Android標準のSpeechRecognizer
- **音声合成**: Android標準のTextToSpeech
- **連続会話モード**: AI応答後に自動でマイクを再起動

---

## 📡 通信フォーマット

### リクエスト（アプリ → OpenClaw）

```http
POST /hooks/voice
Content-Type: application/json
Authorization: Bearer your-secret-token

{
  "message": "今日の天気は？",
  "session_id": "uuid-xxx-xxx"
}
```

### レスポンス（OpenClaw → アプリ）

```json
{"response": "東京は晴れ、気温は15度です。"}
```

または：
```json
{"text": "..."}
{"message": "..."}
```

---

## 🛠 技術スタック

| カテゴリ | 技術 |
|---------|------|
| 言語 | Kotlin |
| UI | Jetpack Compose + Material 3 |
| 音声認識 | Android SpeechRecognizer |
| 音声合成 | Android TextToSpeech |
| ウェイクワード | Vosk（オフライン） |
| システム連携 | VoiceInteractionService |
| 通信 | OkHttp + Gson |
| セキュリティ | EncryptedSharedPreferences |

---

## 💡 ユースケース

### ローカルLLMと連携

Ollamaなどのローカルで動くLLMと組み合わせれば、**完全オフライン**の音声アシスタントが実現できます。

```yaml
# OpenClawでOllamaを使う設定
defaults:
  model: ollama/llama3

providers:
  ollama:
    baseUrl: http://localhost:11434
```

### スマートホーム連携

Home Assistantなどと連携して、音声でスマートホームを操作。

---

## 🤝 コントリビュート

Pull Requests歓迎！Issues報告もお気軽にどうぞ。

## まとめ

OpenClaw Assistantは、**あなたのAIをAndroidのネイティブ音声アシスタントにする**オープンソースアプリです。

Googleアシスタントに依存せず、自分だけのAIアシスタントを構築したい方はぜひお試しください！

## リンク

- 📦 [GitHub - OpenClawAssistant](https://github.com/yuga-hashimoto/OpenClawAssistant)
- 🐙 [OpenClaw](https://github.com/openclaw/openclaw)
- 📖 [OpenClaw Docs](https://docs.openclaw.ai)
