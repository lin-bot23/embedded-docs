# Tripo P1：文字轉模型

Tripo P1 text-to-3D。此節點使用 Tripo P1 API 從文字描述生成 3D 模型。它針對建立低多邊形、可直接用於遊戲的網格進行最佳化，並具有穩定拓撲，適合即時應用程式。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `輸出模式` | 控制生成模型僅包含幾何，或也包含顏色/PBR 貼圖。`"Geometry only"` 會傳回無貼圖的網格。`"Textured"` 會加入顏色/PBR 貼圖，並顯示下方的貼圖選項。 | DYNAMIC_COMBO | 是 | `"Geometry only"`<br>`"Textured"` |
| `提示詞` | 要生成之 3D 模型的文字描述。最多 1024 個字元。必填且不可為空。 | STRING | 是 | 最多 1024 個字元 |
| `負面提示詞` | 不希望生成模型中出現內容的文字描述。最多 255 個字元。預設：未設定。 | STRING | 否 | 最多 255 個字元 |
| `圖像種子` | 用於控制隨機性的種子值。預設：42。 | INT | 否 | 0 to 2147483647 |
| `面數上限` | 目標面數，48-20000。-1 讓 Tripo 自適應選擇。預設：-1。 | INT | 否 | -1 to 20000 |
| `模型種子` | 用於控制隨機性的種子值。預設：42。 | INT | 否 | 0 to 2147483647 |
| `自動尺寸` | 將輸出縮放至接近真實世界公尺。預設：False。 | BOOLEAN | 否 | True / False |
| `匯出 UV` | 生成期間進行 UV 展開。若僅執行幾何生成並想加快速度，請關閉。預設：True。 | BOOLEAN | 否 | True / False |
| `壓縮幾何` | 套用 meshopt 幾何壓縮（EXT_meshopt_compression）。檔案更小，但 ComfyUI 的 3D 預覽無法顯示；編輯前請先解壓縮。預設：False。 | BOOLEAN | 否 | True / False |

### Geometry only 輸入

當 `output_mode` 設為 `"Geometry only"` 時，沒有可用的額外輸入。此模式下，與貼圖相關的參數不會傳送至 Tripo。

### Textured 輸入

這些輸入僅在 `output_mode` 設為 `"Textured"` 時出現。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `pbr` | 包含 PBR 貼圖。開啟時，基礎貼圖也會強制開啟。預設：True。 | BOOLEAN | 是 | True / False |
| `texture_quality` | 貼圖品質預設集。detailed = HD 貼圖，extreme = 8K Ultra 貼圖。預設：`"standard"`。 | COMBO | 是 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | 用於貼圖生成的種子值，用來控制隨機性。預設：42。 | INT | 是 | 0 to 2147483647 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 生成的模型檔案名稱，僅為回溯相容性保留。 | STRING |
| `模型任務 ID` | 模型生成請求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `53a5573384294612b912558436e82f3481717d2ba3d50b73f1e40c3065aff2a0`
