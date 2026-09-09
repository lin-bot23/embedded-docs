# モデルアテンションバックエンド

## 概要

ModelAttentionBackend ノードは、モデルに対して密度の高いアテンション実装を選択するために使用できます。選択されたアテンションバックエンドでモデルをパッチ処理し、PyTorch アテンションまたは利用可能な場合の Comfy Kitchen アテンションが適用されます。スパースアテンションが無効またはサポートされていない場合に特に有用で、モデルが指定された密度の高いアテンションメカニズムで動作するようにします。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 范囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | 選択されたアテンションバックエンドでパッチ処理されるモデル。 | MODEL | はい |  |
| `attention` | モデルに適用する密度の高いアテンションバックエンド。利用可能なオプションは "pytorch attention" で、環境に "comfy kitchen attention" が利用可能な場合にそのオプションが利用できます。 | STRING | はい | "pytorch attention"<br> "comfy kitchen attention" (利用可能な場合) |

- "comfy kitchen attention" オプションは量子化された INT8 アテンションを使用し、NvidiaおよびAMD GPUでのみサポートされます。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `model` | 選択されたアテンションバックエンドが適用された入力モデル。 | MODEL |

## 注意事項

- 選択されたアテンションバックエンドが利用できない場合、ノードは自動的に PyTorch アテンションを使用し、警告をログに記録します。
- ModelAttentionBackend ノードは実験的なものであり、将来のリリースで変更される可能性があります。

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/ja.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
