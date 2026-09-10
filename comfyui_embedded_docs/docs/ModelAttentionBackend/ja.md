# モデルアテンションバックエンド

このノードは、モデルがアテンション計算に使用する dense アテンションバックエンドを選択します。指定されたモデルをクローンし、選択したバックエンドを適用して、パッチ適用済みのクローンを返します。Block Sparse Attention と併用する場合、スパースアテンションが非アクティブまたはサポートされていないときは、このバックエンドが使用されます。選択したバックエンドが利用できない場合、ノードは自動的に PyTorch アテンションにフォールバックします。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model` | パッチ適用対象のモデルです。 | MODEL | はい |  |
| `attention` | 適用する dense アテンションバックエンドです（デフォルト: "pytorch attention"）。Comfy Kitchen attention は INT8 量子化アテンションを使用しており、Nvidia GPU および AMD GPU でのみ利用できます。選択したバックエンドが利用できない場合は、PyTorch アテンションがフォールバックとして使用されます。 | COMBO | はい | "pytorch attention"<br>"comfy kitchen attention" |

注："comfy kitchen attention" オプションは、現在の環境で Comfy Kitchen INT8 アテンションモジュールが利用可能な場合にのみ表示されます。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `model` | 選択したアテンションバックエンドを適用した入力モデルのクローンです。 | MODEL |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/ja.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
