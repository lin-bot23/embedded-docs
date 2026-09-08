# Tripo: 重新定位骨架模型

TripoRetargetNode 可將預設動畫套用於現有的已綁定 3D 模型。它會接收先前已綁定模型的任務 ID，向 Tripo API 傳送重定向要求，並下載產生的動畫檔案。動畫模型可回傳為 GLB 或 FBX 格式，並可選擇性地包含網格幾何與原地播放。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | 要重定向之先前已綁定 3D 模型的任務 ID。參照的工作必須是綁定工作；使用 Mixamo 規範在模型版本 v1.0 上製作的綁定無法用於重定向。 | RIG_TASK_ID | 是 | - |
| `animation` | 要套用至已綁定模型的動畫預設。`preset:*` 動畫可用於兩種綁定模型；`preset:biped:*` 動畫需要使用 model v1.0-20240301 製作的綁定。 | COMBO | 是 | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>加上 UI 中顯示的其他 `"preset:biped:*"` 選項 |
| `out_format` | 輸出檔案格式；結果會送至相符的輸出。（預設：glb） | COMBO | 否 | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | 在匯出時包含網格；關閉時僅匯出動畫骨架。（預設：True） | BOOLEAN | 否 | True<br>False |
| `animate_in_place` | 在原地播放動畫，不包含根部位移。（預設：False） | BOOLEAN | 否 | True<br>False |
| `auth_token_comfy_org` | 用於 Comfy.org API 存取的驗證權杖（隱藏參數）。 | AUTH_TOKEN_COMFY_ORG | 否 | - |
| `api_key_comfy_org` | 用於 Comfy.org 服務存取的 API 金鑰（隱藏參數）。 | API_KEY_COMFY_ORG | 否 | - |
| `unique_id` | 用於追蹤操作的唯一識別碼（隱藏參數）。 | UNIQUE_ID | 否 | - |

注意：`preset:*` 群組中的動畫可用於兩種綁定模型，而 `preset:biped:*` 群組中的動畫需要使用 model v1.0-20240301 製作的綁定。如果參照的綁定是以 Mixamo 規範與開頭為 `v1.0` 的模型版本建立的，則重定向呼叫會失敗並傳回錯誤。

## 輸出

| 輸出名 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `模型檔案` | 產生的動畫 3D 模型檔案（僅用於回溯相容）。 | STRING |
| `重定向任務 ID` | 用於追蹤重定向操作的任務 ID。 | RETARGET_TASK_ID |
| `GLB` | GLB 格式的動畫 3D 模型。當 `out_format` 為 glb 時填充。 | FILE3DGLB |
| `FBX` | FBX 格式的動畫 3D 模型。當 `out_format` 為 fbx 時填充。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e5417a8fa584285ba9e57526e65b091c2383374c70364df9053777a3ce09541a`
