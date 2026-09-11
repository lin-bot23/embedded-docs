# Tripo: モデルのリグ設定

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | リグを付ける元の 3D モデルのタスクID。通常、以前の Tripo モデル生成ノードで生成された ID です。 | MODEL_TASK_ID | はい | - |
| `model_version` | 使用するリグモデルバージョン。v1.0: ヒューマノイド（二足歩行）キャラクターのみ、90以上のアニメーションプリセット。v2.5: 非ヒューマノイド生物（四足、六足、八足、鳥類型、蛇類型、水棲）。デフォルト: `v1.0-20240301`。 | COMBO | いいえ | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | スケルトンタイプ。"auto" の場合、最初に Tripo の無料リグチェックを実行し、推奨タイプを使用します。デフォルト: "auto"。 | COMBO | いいえ | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | ボーン命名: Tripo ネイティブまたは Mixamo 互換。Tripo は、mixamo spec で作成された v1.0 リグに自身のアニメーションプリセットをリターゲットできません。Tripo: Retarget rigged model を使用する場合は tripo を使用してください。デフォルト: "tripo"。 | COMBO | いいえ | "tripo"<br>"mixamo" |
| `out_format` | 出力ファイル形式。結果は対応する出力に格納されます。デフォルト: "glb"。 | COMBO | いいえ | "glb"<br>"fbx" |

**注意:** v1.0 モデルバージョン（`v1.0-20240301`）は biped スケルトンのみをサポートします。このバージョンで biped 以外の `rig_type` を使用すると、ノードはエラーを発生させ、代わりに `v2.5-20260210` を使用するよう指示します。

**注意:** `rig_type` が "auto" の場合、Tripo はまずモデルにリグを付けられるかどうかを確認し、推奨されるスケルトンタイプを選択します。Tripo がモデルにリグを付けられないと報告した場合、ノードはエラーで失敗します。

**注意:** このノードは、Tripo が GLB または FBX ファイルを返すことを想定しています。Tripo がそれ以外のファイルタイプを返した場合、ノードはエラーを発生させます。

**注意:** `out_format` に一致する出力のみに値が設定されます。`out_format` が "glb" の場合は `GLB`、`out_format` が "fbx" の場合は `FBX` です。もう一方の 3D 出力は空です。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `モデルファイル` | 生成されたリグ付きモデルのファイル名（タスクIDと形式拡張子）。後方互換性のためにのみ保持されています。 | STRING |
| `リグタスクID` | リグ生成プロセスを追跡するためのタスクID。 | RIG_TASK_ID |
| `GLB` | リグ付きモデルの GLB 3D ファイル。`out_format` が "glb" の場合に値が設定されます。 | FILE3DGLB |
| `FBX` | リグ付きモデルの FBX 3D ファイル。`out_format` が "fbx" の場合に値が設定されます。 | FILE3DFBX |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/ja.md)

---
**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`
