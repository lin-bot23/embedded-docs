# Tripo P1：圖片轉模型

Tripo P1: Image to Model 會使用 Tripo P1 API 將單一 2D 影像轉換為 3D 模型。它針對生成低多邊形、可直接用於遊戲的網格進行最佳化，並讓你選擇僅含幾何的網格，或帶有 PBR 貼圖的貼圖模型。完成的模型會以 GLB 檔案形式傳回。

## 輸入

### 通用輸入

這些參數一律可用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `輸出模式` | 選擇結果類型。"Geometry only" 會傳回無貼圖的網格；"Textured" 會加入色彩/PBR 貼圖並顯示額外的貼圖設定。 | DYNAMIC_COMBO | 是 | `"Geometry only"`<br>`"Textured"` |
| `圖片` | 用於生成 3D 模型的來源 2D 影像。必須提供單一影像；若未提供，節點會引發錯誤。 | IMAGE | 是 | - |
| `啟用圖片自動修正` | 預先處理輸入影像以獲得更好的生成品質。（預設：False） | BOOLEAN | 否 | True<br>False |
| `面數上限` | 目標面數，48-20000。-1 讓 Tripo 自適應選擇。（預設：-1） | INT | 否 | -1 至 20000 |
| `模型種子` | 用於幾何生成的種子，以便重現結果。（預設：42） | INT | 否 | 0 至 2147483647 |
| `自動尺寸` | 將輸出縮放至接近真實世界公尺。（預設：False） | BOOLEAN | 否 | True<br>False |
| `匯出 UV` | 生成期間進行 UV 展開。關閉可讓僅幾何的執行更快。（預設：True） | BOOLEAN | 否 | True<br>False |
| `壓縮幾何` | 套用 meshopt 幾何壓縮（EXT_meshopt_compression）。檔案較小，但 ComfyUI 的 3D 預覽無法顯示；編輯前請先解壓縮。（預設：False） | BOOLEAN | 否 | True<br>False |

### Geometry only 輸入

沒有其他參數。輸出為無貼圖的網格。

### Textured 輸入

當 `output_mode` 設為 "Textured" 時，會顯示這些參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `pbr` | 包含 PBR 貼圖。開啟時，基礎貼圖也會強制開啟。（預設：True） | BOOLEAN | 是 | True<br>False |
| `texture_quality` | detailed = HD 貼圖，extreme = 8K Ultra 貼圖。（預設："standard"） | COMBO | 是 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | 優先考慮對來源影像的視覺保真度，或對網格幾何的對齊。（預設："original_image"） | COMBO | 是 | `"original_image"`<br>`"geometry"` |
| `orientation` | 旋轉輸出以符合來源影像。僅在貼圖模式下適用。（預設："default"） | COMBO | 是 | `"default"`<br>`"align_image"` |
| `texture_seed` | 用於貼圖生成的種子，以便重現貼圖結果。（預設：42） | INT | 是 | 0 至 2147483647 |

注意：當 `output_mode` 為 "Geometry only" 時，此請求會停用貼圖。在 "Textured" 模式中，一律會請求色彩貼圖；停用 `pbr` 會移除 PBR 貼圖，但保留基礎色彩貼圖，而啟用 `pbr` 也會一併強制啟用基礎貼圖。`texture_alignment` 和 `orientation` 僅能在 "Textured" 模式中使用。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 包含所生成模型檔案名稱（`<task_id>.glb`）的字串。僅為向後相容而保留。 | STRING |
| `模型任務 ID` | Tripo API 針對已完成生成工作所傳回的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 所生成的 GLB 格式 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`
