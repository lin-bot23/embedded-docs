# Tripo: モデルのテクスチャリング

このノードはソース上で非推奨（レガシー）としてマークされています。表示名は「Tripo: Texture model (Legacy)」です。既存のドキュメントのパラメータ表は、現在のソースに対して引き続き正確です。ここではそれらを保持し、概要でレガシー状態について言及します。

Tripo: Texture model (Legacy) ノードは、Tripo API を通じて既存の Tripo 3D モデルにテクスチャを追加します。別の Tripo ノードで作成されたモデルのタスク ID を受け取り、テクスチャジョブが完了すると、テクスチャ付きの GLB または FBX モデルを返します。マテリアルマップ、テクスチャ品質、位置合わせ、シードを制御でき、テキストプロンプト、スタイル画像、または参照画像でテクスチャを誘導できます。このノードはテクスチャツールのレガシーバージョンです。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | テクスチャを適用するモデルの Tripo タスク ID。モデルタスク ID とセグメンテーションタスク ID を受け付けます。 | MODEL_TASK_ID, SEGMENT_TASK_ID | はい | - |
| `texture` | 無視されます。このノードは常にテクスチャを生成します。古いワークフロー用に保持されています。（デフォルト: True） | BOOLEAN | いいえ | true<br>false |
| `pbr` | PBR マテリアルマップ（ベースカラー、メタリック、ラフネス、ノーマル）。オフにすると単色テクスチャになります。（デフォルト: True） | BOOLEAN | いいえ | true<br>false |
| `texture_seed` | テクスチャ生成用のランダムシード。（デフォルト: 42） | INT | いいえ | 0 – 2147483647 |
| `texture_quality` | テクスチャ解像度の品質: detailed = HD テクスチャ、extreme = 8K Ultra テクスチャ。（デフォルト: "standard"）。おおよそのコスト: standard $0.10、detailed $0.20、extreme $0.30。 | COMBO | いいえ | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | 生成されたテクスチャをモデルに位置合わせする方法。（デフォルト: "original_image"） | COMBO | いいえ | "original_image"<br>"geometry" |
| `texture_prompt` | テクスチャリング用の任意のテキストガイダンス。実際には、色を推測する元画像を持たないインポート済みモデル（Tripo: Import Model）では必須です。参照画像と組み合わせることはできません。（デフォルト: ""） | STRING | いいえ | - |
| `model_version` | Texture model: v3.0 は v3.x で生成されたメッシュ用、v2.5 は v2.5 で生成されたメッシュ用です。（デフォルト: v3.0_20250812） | COMBO | いいえ | 複数のオプションがあります |
| `style_image` | テクスチャの芸術的スタイルの参照画像。`texture_prompt` と一緒にのみ使用されます。 | IMAGE | いいえ | - |
| `reference` | テクスチャを誘導する参照画像。`texture_prompt` または `style_image` と組み合わせることはできません。（デフォルト: "none"） | DYNAMIC_COMBO | いいえ | "none"<br>"image"<br>"multiview" |
| `part_names` | Tripo: Segment Model から取得した、テクスチャを適用するパーツ名のカンマ区切りリスト。空の場合はすべてのパーツにテクスチャを適用します。（デフォルト: ""） | STRING | いいえ | - |

### `image` 参照入力

これらの入力は、`reference` が `"image"` に設定されている場合に利用できます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | テクスチャが従うべき単一の参照画像。 | IMAGE | はい | - |

### `multiview` 参照入力

これらの入力は、`reference` が `"multiview"` に設定されている場合に利用できます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `image_front` | 正面ビュー（0°）。 | IMAGE | はい | - |
| `image_left` | 左ビュー（90°）。 | IMAGE | はい | - |
| `image_back` | 背面ビュー（180°）。 | IMAGE | はい | - |
| `image_right` | 右ビュー（270°）。 | IMAGE | はい | - |

**注記:** `"image"` および `"multiview"` 参照モードは、空でない `texture_prompt` または `style_image` と組み合わせることはできません。`style_image` 入力には、空でない `texture_prompt` が必要です。`texture_prompt` を空のままにする場合、ソースモデルはすでに自身のソース画像を持っている必要があります（たとえば、text-to-model、image-to-model、multiview-to-model、または以前のテクスチャリングタスクで生成されたモデル）。インポート済み、セグメント済み、完了済み、またはリトポロジ済みのモデルなど、ソース画像を持たないモデルは、`texture_prompt` でテクスチャリングする必要があります。参照画像は、Tripo API 自体が生成したモデルにのみ受け付けられます。`part_names` 入力を空のままにすると、すべてのパーツにテクスチャを適用できます。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `モデルファイル` | 生成されたモデルファイル（後方互換性のみ）。 | STRING |
| `モデルタスクID` | 完了したテクスチャ生成タスクのタスク ID。他の Tripo ノードへの入力として使用できます。 | MODEL_TASK_ID |
| `GLB` | 生成されたテクスチャ付きモデル（GLB 形式）。ソースがクワッドメッシュまたは FBX インポートの場合は空になります。 | FILE3DGLB |
| `FBX` | 生成されたテクスチャ付きモデル（FBX 形式）。Tripo はクワッドメッシュと FBX インポートに対して FBX を返します。それ以外の場合は空になります。 | FILE3DFBX |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/ja.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`
