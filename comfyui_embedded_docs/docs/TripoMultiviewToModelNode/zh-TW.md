# Tripo：多視角轉模型

此節點使用 Tripo 的 API 同步產生 3D 模型，透過處理最多四張顯示物體不同視角的影像（正面、左側、背面、右側）。它需要一張正面影像，以及至少一個額外視角（左側、背面或右側）來建立 3D 模型。紋理、PBR 材質、幾何品質與輸出格式均可從節點控制。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖像` | 物體的正面視圖影像。 | IMAGE | 是 | - |
| `左側圖像` | 物體的左側視圖影像。 | IMAGE | 否 | - |
| `後方圖像` | 物體的背面視圖影像。 | IMAGE | 否 | - |
| `右側圖像` | 物體的右側視圖影像。 | IMAGE | 否 | - |
| `model_version` | 用於生成的模型版本。 | COMBO | 否 | 多個可用選項 |
| `orientation` | 3D 模型的方向設定（預設：`"default"`）。 | COMBO | 否 | 多個可用選項 |
| `texture` | 生成紋理貼圖。關閉時會回傳未帶紋理的幾何形狀，並忽略 pbr。（預設：True） | BOOLEAN | 否 | - |
| `pbr` | PBR 材質貼圖（基礎顏色、金屬度、粗糙度、法線）。需要紋理。（預設：True） | BOOLEAN | 否 | - |
| `model_seed` | 用於模型生成的隨機種子（預設：42）。 | INT | 否 | 0 至 2,147,483,647 |
| `texture_seed` | 用於紋理生成的隨機種子（預設：42）。 | INT | 否 | 0 至 2,147,483,647 |
| `texture_quality` | 紋理生成的品質等級（預設：`"standard"`）。`"detailed"` = HD 紋理，`"extreme"` = 8K Ultra 紋理。 | COMBO | 否 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | 用於將紋理對齊到模型的方法（預設：`"original_image"`）。 | COMBO | 否 | `"original_image"`<br>`"geometry"` |
| `face_limit` | 最大面數。-1 讓 Tripo 自適應選擇（v3.x 標準約 140 萬面，詳細模式約 200 萬面）。Tripo 會靜默限制：v2.5 為 500,000，四邊形網格為 150,000。（預設：-1） | INT | 否 | -1 至 2,000,000 |
| `quad` | 四邊形網格輸出。Tripo 以 FBX 格式提供四邊形網格，因此結果會出現在 FBX 輸出，而 GLB 輸出保持為空。（預設：False） | BOOLEAN | 否 | - |
| `幾何品質` | 幾何生成的品質等級（預設：`"standard"`）。 | COMBO | 否 | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | 具有乾淨手工風格拓撲的低多邊形網格（500–20,000 個面，四邊形網格 500–10,000）。最適合簡單物體；複雜物體可能失敗。（預設：False） | BOOLEAN | 否 | - |
| `auto_size` | 將帶有紋理的模型縮放到其實際尺寸（以公尺為單位）。Tripo 將尺寸儲存為模型的場景變換，並在模型被轉換、骨骼綁定或重定向時將其烘焙進去；若無紋理則忽略。（預設：False） | BOOLEAN | 否 | - |

**注意：** 正面影像（`image`）始終必填，且 `image_left`、`image_back` 或 `image_right` 中至少需提供一個。關閉 `texture` 也會自動關閉 `pbr`，因為 `pbr` 需要紋理。啟用 `smart_low_poly` 且 `face_limit` 未保持為 -1 時，`face_limit` 若用於三角形網格必須介於 500 到 20,000 之間，若用於四邊形網格則必須介於 500 到 10,000 之間。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 生成之 3D 模型的檔案路徑或識別碼（僅供向後相容）。 | STRING |
| `模型任務 ID` | 用於追蹤模型生成過程的任務識別碼。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型檔案。啟用 `quad` 時為空。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型檔案。僅在啟用 `quad` 時填入。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `73f1259dcba75ce1d56aabb6f0435f11d21eee3268f93502c4c3293d562a6db0`
