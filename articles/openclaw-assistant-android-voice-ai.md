---
title: "OpenClaw Assistant - あなたのAIをAndroidの音声アシスタントにするOSSアプリ"
emoji: "🤖"
type: "tech"
topics: ["Android", "AI", "OpenSource", "音声認識", "Kotlin"]
published: true
---

## 📌 3行でわかるこの記事

- 🎤 **ホームボタン長押し**や**ウェイクワード**でAIアシスタントを起動できるAndroidアプリ
- 🔗 **任意のAIバックエンド**（OpenClaw, Ollama, OpenAI API等）に接続可能
- 🌐 **完全オープンソース**で日英両対応、カスタマイズ自由

## はじめに

「OK Google」の代わりに、**自分のAI**を呼び出せたらいいと思いませんか？

**OpenClaw Assistant**は、Androidのシステムアシスタント機能を使って、任意のAIバックエンドに接続できるオープンソースアプリです。

https://github.com/yuga-hashimoto/OpenClawAssistant

## ✨ 主な機能

### 🏠 ホームボタン長押しで起動

Googleアシスタントの代わりに、OpenClaw Assistantをデフォルトアシスタントに設定できます。

```
設定 → アプリ → デフォルトアプリ → デジタルアシスタント → OpenClaw Assistant
```

### 🎤 カスタムウェイクワード

「Open Claw」「Jarvis」「Computer」など、好きなウェイクワードを選択可能。カスタムワードも設定できます。

オフライン音声認識エンジン [Vosk](https://alphacephei.com/vosk/) を使用しているため、ウェイクワード検知はデバイス内で完結します。

### 🔊 音声入出力

- **音声認識**: Android標準のSpeechRecognizer
- **音声合成**: Android標準のTextToSpeech
- **連続会話モード**: AI応答後に自動でマイクを再起動

### 🔗 任意のバックエンドに接続

Webhook URLを設定するだけで、どんなAIバックエンドにも接続できます。

```yaml
# OpenClawの設定例
hooks:
  voice:
    path: /hooks/voice
    auth:
      bearer: "your-token"
```

**対応フォーマット:**
```json
// リクエスト
POST /hooks/voice
{"message": "今日の天気は？", "session_id": "uuid-xxx"}

// レスポンス（以下のいずれか）
{"response": "東京は晴れです"}
{"text": "東京は晴れです"}
{"message": "東京は晴れです"}
```

## 📱 スクリーンショット

| ホーム画面 | 設定画面 | チャット画面 |
|:---:|:---:|:---:|
| ステータス表示・起動方法選択 | Webhook・音声・ウェイクワード設定 | テキスト＆音声入力対応 |

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

## 🚀 インストール方法

### APKダウンロード

[Releases](https://github.com/yuga-hashimoto/OpenClawAssistant/releases) からAPKをダウンロードしてインストール。

### ソースからビルド

```bash
git clone https://github.com/yuga-hashimoto/OpenClawAssistant.git
cd OpenClawAssistant
./gradlew assembleDebug
```

## 🌐 多言語対応

アプリはデバイスの言語設定に自動追従します：
- 🇯🇵 日本語
- 🇺🇸 英語

## 💡 ユースケース

### ローカルLLMと連携

Ollamaなどのローカルで動くLLMと組み合わせれば、**完全オフライン**の音声アシスタントが実現できます。

### スマートホーム連携

Home Assistantなどと連携して、音声でスマートホームを操作。

### カスタムワークフロー

n8n、Make、Zapierなどのワークフロー自動化ツールと連携可能。

## 🤝 コントリビュート

Pull Requests歓迎！Issues報告もお気軽にどうぞ。

## まとめ

OpenClaw Assistantは、**あなたのAIをAndroidのネイティブ音声アシスタントにする**オープンソースアプリです。

Googleアシスタントに依存せず、自分だけのAIアシスタントを構築したい方はぜひお試しください！

## リンク

- 📦 [GitHub - OpenClawAssistant](https://github.com/yuga-hashimoto/OpenClawAssistant)
- 🐙 [OpenClaw](https://github.com/openclaw/openclaw)
- 📖 [OpenClaw Docs](https://docs.openclaw.ai)
