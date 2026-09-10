# OpenAI ChatGPT 詳細オプション

OpenAIChatConfig ノードを使用すると、OpenAI Chat ノードが応答を生成する方法を制御する高度なオプションを定義できます。トランケーション戦略の設定、出力トークン数の制限、カスタム指示の提供、回答前にモデルが推論する量の選択が可能です。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `切り捨て` | モデルの応答に使用するトランケーション戦略です。auto: この応答と以前の応答のコンテキストがモデルのコンテキストウィンドウサイズを超える場合は、会話の中盤にある入力項目を削除して、コンテキストウィンドウに収まるように応答をトランケーションします。disabled: モデルの応答がモデルのコンテキストウィンドウサイズを超える場合は、リクエストは400エラーで失敗します（デフォルト: "auto"） | COMBO | 必須 | "auto"<br>"disabled" |
| `最大出力トークン数` | 応答に対して生成できるトークン数の上限です。表示される出力トークンと推論トークンが含まれます（デフォルト: 4096） | INT | 任意 | 16〜16384 |
| `指示` | 応答の生成方法に関するモデルへの指示です（複数行の入力に対応） | STRING | 任意 | - |
| `reasoning_effort` | モデルが回答する前にどれだけ推論するかを指定します。"default" はモデルに選択を委ねます。サポートされるレベルはモデルごとに異なります：GPT-6 Astra は low-max、GPT-5.6 は none-max（minimal なし）、GPT-5.5 は none-xhigh、GPT-5.5 Pro は medium-xhigh、GPT-5 は minimal-high、o-series は low-high。GPT-4.1 は推論を行いません。サポートされていないレベルは、リクエストが送信される前に拒否されます（デフォルト: "default"） | COMBO | 任意 | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

注：`top_p` と `temperature` はAPI仕様ではプロパティとして記載されていますが、すべてのモデルでサポートされているわけではないため、入力としては公開されていません。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | OpenAI Chat ノードで使用する、指定された設定を含む設定オブジェクトです。 | OPENAI_CHAT_CONFIG |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/ja.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
