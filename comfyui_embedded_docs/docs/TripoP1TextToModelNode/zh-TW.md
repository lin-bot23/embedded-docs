# Tripo P1：文字轉模型

此節點使用 Tripo P1 API 從文字描述生成 3D 模型。它針對建立具有穩定拓撲的低多邊形、適合遊戲使用的網格進行了最佳化，因此適用於即時應用程式。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `輸出模式` | 控制生成的模型僅包含幾何形狀，還是同時包含顏色/PBR 紋理。選擇「Textured」會在下文加入紋理輸入。「Geometry only」會回傳未套用紋理的網格；「Textured」則會新增顏色/PBR 貼圖。 | DYNAMIC_COMBO | 是 | `"Geometry only"`<br>`"Textured"` |
| `提示詞` | 您想要生成的 3D 模型的文字描述。最多 1024 個字元。 | STRING | 是 | 最多 1024 個字元 |
| `負面提示詞` | 對您不希望出現在生成模型中的內容的文字描述。最多 255 個字元。 | STRING | 否 | 最多 255 個字元 |
| `圖像種子` | 影像生成的種子值，用於控制隨機性。預設：42。 | INT | 否 | 0 至 2147483647 |
| `面數上限` | 目標面數，範圍為 48 至 20000。若為 -1，則讓 Tripo 自適應選取。預設：-1。 | INT | 否 | -1 至 20000 |
| `模型種子` | 模型生成的種子值，用於控制隨機性。預設：42。 | INT | 否 | 0 至 2147483647 |
| `自動尺寸` | 將輸出縮放為約略符合真實世界的公尺數。預設：False。 | BOOLEAN | 否 | True / False |
| `匯出 UV` | 在生成期間執行 UV 展開。若只要幾何形狀並希望加快執行速度，可關閉此選項。預設：True。 | BOOLEAN | 否 | True / False |
| `壓縮幾何` | 套用 meshopt 幾何壓縮（EXT_meshopt_compression）。檔案較小，但 ComfyUI 的 3D 預覽無法顯示；編輯前請先解壓縮。預設：False。 | BOOLEAN | 否 | True / False |

### 僅幾何形狀輸入

當 `output_mode` 設為「Geometry only」時，沒有額外的輸入可用。在此模式下，與紋理相關的參數不會傳送至 Tripo。

### 紋理輸入

這些輸入僅在 `output_mode` 設為「Textured」時才會出現。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `pbr` | 包含 PBR 貼圖。開啟時，也會強制啟用基礎紋理。預設：True。 | BOOLEAN | 是 | True / False |
| `texture_quality` | 紋理品質預設。detailed = HD 紋理，extreme = 8K 超高畫質紋理。預設：「standard」。 | COMBO | 是 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | 紋理生成的種子值，用於控制隨機性。預設：42。 | INT | 是 | 0 至 2147483647 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 生成的 3D 模型的檔案路徑，僅為向後相容性而保留。 | STRING |
| `模型任務 ID` | 模型生成請求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `63781a990f892e6b1f241179039d1fb24778ba7aa7dccda7d14557cbf190b712`
