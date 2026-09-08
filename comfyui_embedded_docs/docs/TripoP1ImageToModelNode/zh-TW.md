# Tripo P1：圖片轉模型

Tripo P1：Image to Model 使用 Tripo P1 API 將單張 2D 影像轉換為 3D 模型。它針對生成低多邊形、可立即用於遊戲的網格進行了最佳化，並讓您可以選擇僅含幾何的網格，或帶有 PBR 貼圖的紋理模型。完成後的模型會以 GLB 檔案形式回傳。

## 輸入

### 通用輸入

這些參數隨時可用。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `輸出模式` | 選擇結果類型。"Geometry only" 會回傳未貼紋理的網格；"Textured" 則加入顏色與 PBR 貼圖，並顯示額外的紋理設定。 | DYNAMIC_COMBO | 是 | `"Geometry only"`<br>`"Textured"` |
| `圖片` | 用於生成 3D 模型的來源 2D 影像。此節點需要單張影像，若未提供則會引發錯誤。 | IMAGE | 是 | - |
| `啟用圖片自動修正` | 預先處理輸入影像，以獲得更好的生成品質。(預設值：False) | BOOLEAN | 否 | True<br>False |
| `面數上限` | 目標面數，範圍 48-20000。-1 表示讓 Tripo 自適應選擇。(預設值：-1) | INT | 否 | -1 至 20000 |
| `模型種子` | 用於幾何生成的種子，以便結果可重現。(預設值：42) | INT | 否 | 0 至 2147483647 |
| `自動尺寸` | 將輸出縮放至接近真實世界的公尺單位。(預設值：False) | BOOLEAN | 否 | True<br>False |
| `匯出 UV` | 在生成期間進行 UV 展開。若只想更快地執行僅幾何模式，請關閉此選項。(預設值：True) | BOOLEAN | 否 | True<br>False |
| `壓縮幾何` | 套用 meshopt 幾何壓縮 (EXT_meshopt_compression)。檔案較小，但 ComfyUI 的 3D 預覽無法顯示；請在編輯前先解壓縮。(預設值：False) | BOOLEAN | 否 | True<br>False |

### 紋理輸入

當 `output_mode` 設定為 "Textured" 時，會顯示這些參數。"Geometry only" 模式沒有額外參數。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `pbr` | 包含 PBR 貼圖。啟用時，也會強制啟用基礎紋理。(預設值：True) | BOOLEAN | 否 | True<br>False |
| `texture_quality` | 紋理解析度等級。"detailed" = HD 紋理，"extreme" = 8K Ultra 紋理。(預設值："standard") | COMBO | 否 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | 優先保持與來源影像的視覺逼真度，或與網格幾何的對齊程度。(預設值："original_image") | COMBO | 否 | `"original_image"`<br>`"geometry"` |
| `orientation` | 旋轉輸出以符合來源影像。僅在已加上紋理時套用。(預設值："default") | COMBO | 否 | `"default"`<br>`"align_image"` |
| `texture_seed` | 用於紋理生成的種子，以便紋理結果可重現。(預設值：42) | INT | 否 | 0 至 2147483647 |

注意：當 `output_mode` 為 "Geometry only" 時，該請求會停用紋理。在 "Textured" 模式下，一律會要求顏色紋理；停用 `pbr` 會移除 PBR 貼圖，但仍保留基礎顏色紋理，而啟用 `pbr` 則會同時強制啟用基礎紋理。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 生成的 3D 模型結果。僅為向後相容而保留。 | STRING |
| `模型任務 ID` | Tripo API 為已完成的生成作業回傳的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db5dc76518a4efcd28d388dc00ad0810f619481482f20fa456c4ff2478192aa3`
