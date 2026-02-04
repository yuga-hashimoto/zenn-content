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

## 🚀 セットアップガイド

### Step 1: OpenClawでWebhookを作成

OpenClawにWebhookを設定します。以下の指示をあなたのOpenClawにコピペしてください：

```
OpenClaw Assistant用のWebhookを設定してください。

GitHub: https://github.com/yuga-hashimoto/OpenClawAssistant

- hooksにvoice用のエンドポイントを追加
- Bearer認証トークンを設定（任意）
- ngrokで外部公開

設定が完了したら、Webhook URLを教えてください（トークンを設定した場合はそれも）。
```

### Step 2: Androidアプリのインストール

1. [Releases](https://github.com/yuga-hashimoto/OpenClawAssistant/releases) からAPKをダウンロード
2. インストール（「提供元不明のアプリ」を許可）

### Step 3: アプリの設定

1. アプリを開く
2. 右上の⚙️から設定画面へ
3. 以下を入力：

| 項目 | 値 |
|------|-----|
| **Webhook URL** | OpenClawから取得したURL |
| **Auth Token** | Webhookのトークン（任意） |

4. 「Test Connection」で接続確認
5. 「Save」で保存

### Step 4: システムアシスタントに設定

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

- **ローカルLLM**: Ollamaと組み合わせて完全オフラインの音声アシスタント
- **スマートホーム**: Home Assistantと連携して音声操作
- **カスタムワークフロー**: n8n、Make、Zapierなどと連携

---

## 🤝 コントリビュート

Pull Requests歓迎！Issues報告もお気軽にどうぞ。

## リンク

- 📦 [GitHub - OpenClawAssistant](https://github.com/yuga-hashimoto/OpenClawAssistant)
- 🐙 [OpenClaw](https://github.com/openclaw/openclaw)
- 📖 [OpenClaw Docs](https://docs.openclaw.ai)
