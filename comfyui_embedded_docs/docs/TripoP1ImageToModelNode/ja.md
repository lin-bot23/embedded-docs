# Tripo P1：画像からモデルへ

Tripo P1: Image to Model は、Tripo P1 API を使用して単一の2D画像を3Dモデルに変換します。低ポリゴンでゲーム向けのメッシュ生成に最適化されており、ジオメトリのみのメッシュか、PBRマップ付きのテクスチャモデルを選択できます。完成したモデルはGLBファイルとして返されます。

## 入力

### 共通入力

これらのパラメータは常に使用できます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `出力モード` | 結果のタイプを選択します。"Geometry only" はテクスチャなしメッシュを返し、"Textured" はカラー/PBRマップを追加して追加のテクスチャ設定を表示します。 | DYNAMIC_COMBO | はい | `"Geometry only"`<br>`"Textured"` |
| `画像` | 3Dモデル生成に使用するソース2D画像。単一画像が必要で、指定がない場合ノードはエラーを発生させます。 | IMAGE | はい | - |
| `画像自動補正を有効化` | 生成品質を高めるために入力画像を前処理します。（デフォルト: False） | BOOLEAN | いいえ | True<br>False |
| `面数制限` | 目標フェイス数、48～20000。-1 にすると Tripo が適応的に選択します。（デフォルト: -1） | INT | いいえ | -1 to 20000 |
| `モデルシード` | ジオメトリ生成に使用するシードで、結果を再現できるようにします。（デフォルト: 42） | INT | いいえ | 0 to 2147483647 |
| `自動サイズ調整` | 出力を実世界のメートルに近づくようにスケーリングします。（デフォルト: False） | BOOLEAN | いいえ | True<br>False |
| `UV展開を出力` | 生成中にUV展開を行います。より高速なジオメトリのみの実行にはオフにします。（デフォルト: True） | BOOLEAN | いいえ | True<br>False |
| `ジオメトリ圧縮` | meshoptジオメトリ圧縮（EXT_meshopt_compression）を適用します。ファイルは小さくなりますが、ComfyUIの3Dプレビューでは表示できません。編集前に展開してください。（デフォルト: False） | BOOLEAN | いいえ | True<br>False |

### Geometry only 入力

追加パラメータはありません。出力はテクスチャなしメッシュです。

### Textured 入力

これらのパラメータは `output_mode` が "Textured" に設定されている場合に表示されます。

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBRマップを含めます。オンの場合、ベーステクスチャも強制的にオンになります。（デフォルト: True） | BOOLEAN | はい | True<br>False |
| `texture_quality` | detailed = HDテクスチャ、extreme = 8K Ultraテクスチャ。（デフォルト: "standard"） | COMBO | はい | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | ソース画像への視覚的な忠実さを優先するか、メッシュジオメトリへの整合を優先します。（デフォルト: "original_image"） | COMBO | はい | `"original_image"`<br>`"geometry"` |
| `orientation` | ソース画像に合わせて出力を回転します。テクスチャ付きの場合にのみ適用されます。（デフォルト: "default"） | COMBO | はい | `"default"`<br>`"align_image"` |
| `texture_seed` | テクスチャ生成に使用するシードで、テクスチャ付き結果を再現できるようにします。（デフォルト: 42） | INT | はい | 0 to 2147483647 |

注: `output_mode` が "Geometry only" の場合、リクエストではテクスチャ処理が無効になります。"Textured" モードではカラーテクスチャが常に要求されます。`pbr` を無効にするとPBRマップは削除されますがベースカラーテクスチャは保持され、`pbr` を有効にするとベーステクスチャも強制的にオンになります。`texture_alignment` と `orientation` は "Textured" モードでのみ使用できます。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `モデルファイル` | 生成されたモデルファイル名（`<task_id>.glb`）を含む文字列。後方互換性のためだけに保持されています。 | STRING |
| `モデルタスクID` | 完了した生成ジョブに対してTripo APIから返される一意のタスクID。 | MODEL_TASK_ID |
| `GLB` | GLB形式で生成された3Dモデル。 | FILE3DGLB |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/ja.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`
