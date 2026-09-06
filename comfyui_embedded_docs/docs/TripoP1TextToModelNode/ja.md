# Tripo P1：テキストからモデルへ

このノードは、Tripo P1 API を使用して、テキスト記述から 3D モデルを生成します。低ポリゴンかつゲーム向けのメッシュを安定したトポロジーで作成するよう最適化されており、リアルタイムアプリケーションに適しています。

## 入力

### 共通入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|------|----------|------|-------|
| `output_mode` | 生成されるモデルがジオメトリのみか、色/PBR テクスチャも含むかを制御します。"Textured" を選択すると、以下のテクスチャ入力が追加されます。"Geometry only" はテクスチャなしのメッシュを返し、"Textured" はカラー/PBR マップを追加します。 | DYNAMIC_COMBO | 必須 | `"Geometry only"`<br>`"Textured"` |
| `prompt` | 生成したい 3D モデルのテキスト説明です。最大 1024 文字。 | STRING | 必須 | 最大1024文字 |
| `negative_prompt` | 生成されるモデルに含まれたくない内容のテキスト説明です。最大 255 文字。 | STRING | 任意 | 最大255文字 |
| `image_seed` | 画像生成用のシード値で、ランダム性を制御するために使用します。デフォルト: 42。 | INT | 任意 | 0〜2147483647 |
| `face_limit` | 目標とする面数（48〜20000）です。-1 を指定すると、Tripo が適応的に選択します。デフォルト: -1。 | INT | 任意 | -1〜20000 |
| `model_seed` | モデル生成用のシード値で、ランダム性を制御するために使用します。デフォルト: 42。 | INT | 任意 | 0〜2147483647 |
| `auto_size` | 出力を実世界のメートルに近似するようスケールします。デフォルト: False。 | BOOLEAN | 任意 | True / False |
| `export_uv` | 生成時に UV 展開を行います。ジオメトリのみの処理を高速化するにはオフにします。デフォルト: True。 | BOOLEAN | 任意 | True / False |
| `compress_geometry` | meshopt のジオメトリ圧縮（EXT_meshopt_compression）を適用します。ファイルサイズは小さくなりますが、ComfyUI の 3D プレビューでは表示できません。編集前に圧縮を解除してください。デフォルト: False。 | BOOLEAN | 任意 | True / False |

### ジオメトリのみ入力

`output_mode` が `"Geometry only"` に設定されている場合、追加の入力はありません。このモードでは、テクスチャ関連のパラメータは Tripo に送信されません。

### テクスチャ付き入力

これらの入力は、`output_mode` が `"Textured"` に設定されている場合にのみ表示されます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|------|----------|------|-------|
| `pbr` | PBR マップを含めます。オンの場合は、ベーステクスチャも強制的にオンになります。デフォルト: True。 | BOOLEAN | 必須 | True / False |
| `texture_quality` | テクスチャ品質のプリセットです。detailed は HD テクスチャ、extreme は 8K ウルトラテクスチャです。デフォルト: "standard"。 | COMBO | 必須 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | テクスチャ生成用のシード値で、ランダム性を制御するために使用します。デフォルト: 42。 | INT | 必須 | 0〜2147483647 |

## 出力

| 出力名 | 説明 | データ型 |
|---------|------|----------|
| `model_file` | 生成された 3D モデルのファイルパスです。後方互換性のためだけに維持されています。 | STRING |
| `model task_id` | モデル生成リクエストの一意のタスク ID です。 | MODEL_TASK_ID |
| `GLB` | GLB 形式で生成された 3D モデルです。 | FILE3DGLB |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/ja.md)

---
**Source fingerprint (SHA-256):** `63781a990f892e6b1f241179039d1fb24778ba7aa7dccda7d14557cbf190b712`
