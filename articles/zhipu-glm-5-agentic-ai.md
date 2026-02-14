---
title: "【GLM-5】Claude CodeやCursorと同等性能で月$10〜。AIコーディングの価格破壊が始まった"
emoji: "💸"
type: "tech"
topics: ["AI", "LLM", "GLM5", "ClaudeCode", "Cursor"]
published: true
---

## 📌 3行でわかるこの記事

- 💸 Claude Max（月$100〜$200）やCursor Pro（月$20+従量課金）と同等性能が、**GLM Coding Planなら月$10〜$20**で使える
- 🏆 GLM-5はSWE-bench Verified 77.8%でClaude Opus 4.5（80.9%）に迫るOSS最高スコア
- 🔧 Claude Code / Cursor / Cline / OpenCode など20以上のコーディングツールにそのまま対応

## はじめに：AIコーディング、高すぎませんか？

Claude Codeを本格的に使おうとすると**Claude Max $100/月〜$200/月**。CursorもPro $20/月に加えて、使い込むと従量課金が加算されていく。

「AIコーディングは便利だけど、毎月の出費が痛い」

そう感じている開発者に朗報です。2026年2月11日、中国の智譜AI（Z.ai）がリリースした**GLM-5**は、Claude Opus 4.5に迫るコーディング性能を持ちながら、**月$10〜$20の定額プラン**で使えます。

本記事では、GLM-5が実際にどれだけ使えるのか、どうやって導入するのか、そしていくらかかるのかを解説します。

![GLM-5 ベンチマーク結果](https://github.com/zai-org/GLM-5/raw/main/resources/bench.png)
*(出典: [zai-org/GLM-5 GitHub](https://github.com/zai-org/GLM-5))*

## GLM-5はどれだけ「使える」のか？

### コーディング性能：Claude Opus 4.5の96%に到達

最も重要なベンチマークであるSWE-bench Verified（実際のGitHub Issueを解決する能力）の比較です。

| モデル | SWE-bench Verified | Terminal Bench 2.0 | 月額コスト |
|--------|-------------------|-------------------|-----------|
| Claude Opus 4.5 | 80.9% | 58.1 | $100〜$200 |
| GPT-5.2 | 80.0% | - | $200 |
| **GLM-5** | **77.8%** | **56.2** | **$10〜$20** |
| Gemini 3.0 Pro | 73.2% | - | $19.99〜 |

GLM-5のスコア77.8%はClaude Opus 4.5の**96%の性能**です。この3%の差に**毎月$80〜$180の差額**を払う価値があるかどうか——多くの開発者にとって、答えは明白でしょう。

### 前モデルGLM-4.7からの進化

GLM-5は2025年12月リリースのGLM-4.7から大幅に強化されています。

| 項目 | GLM-4.7 | GLM-5 | 進化幅 |
|------|---------|-------|--------|
| 総パラメータ数 | 355B | 744B | 2.1倍 |
| アクティブパラメータ | 32B | 40B | 1.25倍 |
| コンテキスト長 | 200K | 200K | 同等 |
| 事前学習データ | 23Tトークン | 28.5Tトークン | +24% |
| SWE-bench Verified | 73.8% | 77.8% | **+4.0pt** |
| Terminal Bench 2.0 | 41.0 | 56.2 | **+15.2pt** |
| AIME 2025 | 95.7% | 97.2% | +1.5pt |
| BrowseComp | 67 | OSS最高 | 大幅向上 |
| τ²-Bench | 84.7 | OSS最高 | 大幅向上 |
| ライセンス | MIT | MIT | 同じ |

特に**Terminal Bench 2.0が+15.2pt**の大幅向上。これはターミナル上での複雑なタスク遂行能力（＝Claude Codeのようなエージェント利用）が飛躍的に改善されたことを意味します。

### ハルシネーションが業界最低水準

GLM-5は**AA-Omniscience Index**でスコア-1を記録。前世代から35ポイント改善し、「知らないことは知らないと答える」能力でAI業界トップです。コーディング中に嘘の関数名やAPIを提案されるストレスが大幅に減ります。

### エージェント能力もOSS最強

| ベンチマーク | 評価内容 | GLM-5の成績 |
|-------------|---------|------------|
| BrowseComp | ネット検索・情報理解 | OSS最高 |
| MCP-Atlas | ツール呼び出し・多段階タスク | OSS最高 |
| τ²-Bench | 複雑なマルチツールシナリオ | OSS最高 |
| Vending Bench 2 | 長期計画・意思決定 | $4,432（OSS最高） |

## GLM-5は何に使えるのか？

### 1. 普段のコーディング作業（最大の用途）

今Claude CodeやCursorでやっていることが、そのままGLM-5でできます。

- バグ修正・機能追加の自動実装
- コードレビュー・リファクタリング
- テストコード生成
- 複数ファイルにまたがる大規模な変更

**対応ツール：**
Claude Code / Cursor / Cline / OpenCode / Roo Code / Kilo Code / Goose / OpenClaw など**20以上のツール**

つまり、今使っているツールを変える必要はありません。**バックエンドのモデルをGLM-5に差し替えるだけ**で、月額コストが1/10以下になります。

### 2. ドキュメント・事務作業の自動化（Agent Mode）

GLM-5にはネイティブの**Agent Mode**が搭載されており、プロンプトから直接オフィスドキュメントを生成できます。

- 📝 **Word文書**（.docx）：書式設定・表・図の挿入付き
- 📊 **Excel**（.xlsx）：データ整理・グラフ生成
- 📄 **PDF**：チャート付きレポート生成

会議資料、週次レポート、データ分析表など、定型業務を丸投げできます。

### 3. エージェントタスク・Web調査

BrowseComp・MCP-Atlas・τ²-Benchで全てOSS最高スコア。以下のような複雑なタスクが得意です。

- Web検索 → 情報統合 → レポート作成
- 複数ツールを組み合わせた多段階ワークフロー
- 長期的な計画立案と意思決定

### 4. 機密環境でのプライベートAI

MITライセンスのオープンソースなので、**自社サーバーに完全デプロイ可能**です。社外にコードを出せない環境でも使えます。

## いくらかかるのか？（料金比較）

### GLM Coding Plan vs 競合サービス

まず、各サービスの月額コストを並べます。

| サービス | 月額料金 | 備考 |
|----------|---------|------|
| Claude Max 5x | $100/月 | Claude Code用 |
| Claude Max 20x | $200/月 | ヘビーユーザー向け |
| Cursor Pro | $20/月 + 従量課金 | 使い込むと$50〜$100超えも |
| Windsurf | $15/月 + 従量課金 | |
| **GLM Coding Pro** | **≒$10/月** | **Claude Code/Cursor対応** |
| **GLM Coding Max** | **≒$20/月** | **2,400プロンプト/5時間** |
| **GLM Coding Lite** | **$6/月** | **GLM-4.7対応（GLM-5は近日対応）** |

:::message
**Claude Max $100/月の代わりにGLM Coding Pro $10/月。同じClaude Code上で使えて、コストは1/10。**
:::

### GLM Coding Planの詳細

| プラン | 料金 | 5時間あたりの利用量 | GLM-5対応 |
|--------|------|---------------------|-----------|
| **Lite** | $6/月 | 約120プロンプト | GLM-4.7対応（GLM-5は近日対応） |
| **Pro** | $30/四半期（≒$10/月） | 約600プロンプト | ✅ |
| **Max** | $60/四半期（≒$20/月） | 約2,400プロンプト | ✅ |

5時間ごとにプロンプト数がリセットされるサイクル制です。使い切っても追加課金は発生せず、次のサイクルまで待てばまた使えます。**予想外の高額請求が来ることがないので安心**です。

### API従量課金（アプリ開発者向け）

自前のアプリケーションに組み込む場合の料金比較です。

| モデル | 入力（/百万トークン） | 出力（/百万トークン） |
|--------|----------------------|----------------------|
| **GLM-5** | **$1.00** | **$3.20** |
| Claude Opus 4.6 | $5.00 | $25.00 |
| GPT-5.2 | $1.75 | $14.00 |
| Gemini 3.0 Pro | $2.00 | $12.00 |

:::message alert
GLM-5はClaude Opus 4.6と比較して**入力5倍、出力約8倍安い**。API利用でも圧倒的なコストパフォーマンスです。
:::

## どうやって使うのか？

### 方法1: GLM Coding Plan（おすすめ）

**いま使っているコーディングツールで、そのままGLM-5を使う最もお手軽な方法**です。

**3ステップで始められます：**
1. [z.ai/subscribe](https://z.ai/subscribe) でプランを選択・登録
2. APIキーを取得
3. お使いのツールにAPIキーを設定

以下のツールに対応しています：

| ツール | 対応状況 |
|--------|---------|
| Claude Code | ✅ |
| Cursor | ✅ |
| Cline | ✅ |
| OpenCode | ✅ |
| Roo Code | ✅ |
| Kilo Code | ✅ |
| Goose | ✅ |
| OpenClaw | ✅ |

各ツールの設定方法は、プラン登録後のダッシュボードに記載されています。基本的には**API ProviderをOpenAI Compatibleに変更してAPIキーを入力するだけ**です。

### 方法2: chat.z.aiで試す（無料）

[chat.z.ai](https://chat.z.ai) にアクセスすれば、ブラウザ上で直接GLM-5を試せます。新規登録で無料クレジットが付与されるので、**契約前にまず実力を確認したい方はこちら**がおすすめです。

### 方法3: OpenRouter経由

すでにOpenRouterを使っている方は、モデル指定を`zai/glm-5`に変えるだけです。

### 方法4: セルフホスティング（上級者向け）

[Hugging Face](https://huggingface.co/zai-org/GLM-5)からMITライセンスでウェイトをダウンロードし、自社サーバーで運用できます。vLLM / SGLangに対応。ただし推論に**約1,490GBのメモリ**が必要なため、マルチGPU環境が必須です。

## GLM-5の技術的な裏側

### アーキテクチャ

GLM-5はMixture-of-Experts（MoE）構造を採用。256個のエキスパートからトークンごとに8個だけを活性化するため、744Bの巨大モデルでありながら推論コストは40B相当に抑えられています。

さらにDeepSeek Sparse Attention（DSA）を統合し、200Kトークンの長文脈を効率的に処理します。

### Huawei Ascendチップで完全独立訓練

GLM-5はHuawei AscendチップとMindSporeフレームワークのみで訓練されており、米国製GPU（NVIDIA A100/H100）に一切依存していません。

### 「slime」：新しい強化学習基盤

智譜AIが独自開発した非同期RL基盤「slime」により、ハルシネーション率の劇的な低下とエージェント能力の大幅向上を実現しています。

## 「Pony Alpha」の正体はGLM-5だった

2026年2月上旬、OpenRouterに「**Pony Alpha**」という謎のモデルが突如登場し、コーディング能力でClaude Opusに迫ると話題になりました。その正体がGLM-5のステルスリリースだったことが後に判明。正体が明かされる前から実力が認められていたことが、GLM-5の実力を何より証明しています。

## まとめ：性能は同等、コストは1/10

GLM-5を一言でまとめると：

:::message
**Claude Opus 4.5の96%のコーディング性能を、1/10の料金で使える。**
:::

- ✅ SWE-bench Verified 77.8%（OSS世界最高）
- ✅ Claude Code / Cursor / Cline / OpenCode など20以上のツール対応
- ✅ GLM Coding Plan Pro なら**月わずか$10**
- ✅ 5時間サイクル制で予想外の高額請求なし
- ✅ ハルシネーション率が業界最低水準
- ✅ Agent Modeでドキュメント自動生成
- ✅ MITライセンスで完全オープンソース

「AIコーディングにお金をかけすぎている」と感じている方は、まず[chat.z.ai](https://chat.z.ai)で無料で試してみてください。実力に納得したら、[GLM Coding Plan](https://z.ai/subscribe)で本格導入がおすすめです。

## 参考リンク

- [GLM-5 公式GitHub](https://github.com/zai-org/GLM-5)
- [Hugging Face モデルカード](https://huggingface.co/zai-org/GLM-5)
- [GLM Coding Plan](https://z.ai/subscribe)
- [GLM-5 APIドキュメント](https://docs.bigmodel.cn/cn/guide/models/text/glm-5)
- [智譜AI公式サイト](https://www.zhipuai.cn/en)
- [GIGAZINE - GLM-5解説記事](https://gigazine.net/gsc_news/en/20260212-z-ai-glm-5/)
- [VentureBeat - GLM-5のslime技術](https://venturebeat.com/technology/z-ais-open-source-glm-5-achieves-record-low-hallucination-rate-and-leverages)
- [Medium - GLM Coding Planレビュー](https://medium.com/@elio.verhoef/glm-coding-plan-how-i-get-3-claude-max-code-usage-for-30-month-07503db5eeb2)
