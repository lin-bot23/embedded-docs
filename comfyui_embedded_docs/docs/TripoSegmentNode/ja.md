# Tripo: モデルをセグメント化

このノードは、3D モデルを個々のパーツに分割します。モデルを Tripo セグメンテーションサービスに送信し、ジョブが完了するのを待って、分割されたモデルを GLB 形式で、パーツ名のカンマ区切りリストとともに返します。これらのパーツ名は、Tripo: Complete Mesh Parts、Tripo: Retopology、Tripo: Convert model などの下流のステップで使用されます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | パーツに分割する 3D モデルのタスク ID です。 | MODEL_TASK_ID | はい | N/A |

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `model_file` | 分割された GLB モデルの出力ファイル名で、`<task_id>.glb` の形式です。後方互換性のためにのみ保持されています。 | STRING |
| `segment task_id` | 結果を生成した分割ジョブのタスク ID です。 | SEGMENT_TASK_ID |
| `GLB` | 分割された 3D モデルです（GLB ファイル）。 | GLB |
| `part_names` | パーツ名のカンマ区切りリストです。 | STRING |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/ja.md)

---
**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`
