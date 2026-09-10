# Tripo: リグ付きモデルのリターゲット

TripoRetargetNode は、既存のリグ済み3Dモデルにプリセットアニメーションを適用します。以前にリグ付けされたモデルのタスクIDを受け取り、Tripo API にリターゲット要求を送信し、結果のアニメーションファイルをダウンロードします。アニメーション付きモデルは GLB または FBX として返すことができ、オプションでメッシュジオメトリを含めたり、オプションでインプレイス再生を行えます。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | リターゲットする、以前にリグ付けされた3DモデルのタスクID。参照されるタスクはリグタスクである必要があります。 | RIG_TASK_ID | はい | - |
| `animation` | リグ済みモデルに適用するアニメーションプリセット。`preset:*` アニメーションは両方のリグモデルで動作します。`preset:biped:*` アニメーションはモデル v1.0-20240301 以降のリグ向けに作られています。v2.5 リグは chop、climb、dive、fall、hurt、idle、jump、run、shoot、slash、turn、walk のみを受け付けます。 | COMBO | はい | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>さらに、UI に表示される追加の `"preset:biped:*"` オプション |
| `out_format` | 出力ファイル形式。結果は対応する出力に届きます。（デフォルト: glb） | COMBO | いいえ | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | エクスポートにメッシュを含めます。オフにすると、アニメーション化されたスケルトンのみをエクスポートします。（デフォルト: True） | BOOLEAN | いいえ | True<br>False |
| `animate_in_place` | ルートの変位なしで、アニメーションをインプレイスで再生します。（デフォルト: False） | BOOLEAN | いいえ | True<br>False |
| `auth_token_comfy_org` | Comfy.org API アクセス用の認証トークン（非表示パラメータ）。 | AUTH_TOKEN_COMFY_ORG | いいえ | - |
| `api_key_comfy_org` | Comfy.org サービスアクセス用の API キー（非表示パラメータ）。 | API_KEY_COMFY_ORG | いいえ | - |
| `unique_id` | 操作を追跡するための一意の識別子（非表示パラメータ）。 | UNIQUE_ID | いいえ | - |

注意: `preset:*` グループのアニメーションは両方のリグモデルで動作します。`preset:biped:*` グループのアニメーションは、モデル v1.0-20240301 以降のリグ向けに作られています。v2.5 リグは chop、climb、dive、fall、hurt、idle、jump、run、shoot、slash、turn、walk のみを受け付けます。参照されたリグが Mixamo 仕様と `v1.0` で始まるモデルバージョンで作成されている場合、リターゲット呼び出しはエラーで失敗します。要求された出力形式は GLB または FBX である必要があります。サービスが他のファイルタイプを返した場合、ノードはエラーを発生させます。

## 出力

| 出力名 | 説明 | データ型 |
|-------------|-------------|-----------|
| `リターゲットタスクID` | 生成されたアニメーション付き3Dモデルファイル（後方互換性のみ）。 | STRING |
| `リターゲット タスクID` | リターゲット操作を追跡するためのタスクID。 | RETARGET_TASK_ID |
| `GLB` | GLB 形式のアニメーション付き3Dモデル。`out_format` が glb の場合に設定されます。 | FILE3DGLB |
| `FBX` | FBX 形式のアニメーション付き3Dモデル。`out_format` が fbx の場合に設定されます。 | FILE3DFBX |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/ja.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`
