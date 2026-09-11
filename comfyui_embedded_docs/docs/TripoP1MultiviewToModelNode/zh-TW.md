# Tripo P1：多視角轉模型

此節點會根據物件或角色的二至四張參考影像生成 3D 模型。提供正面視圖，以及左、後、右視圖的任意組合，節點會以 GLB 網格傳回重建後的主體。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖片` | 正面視圖（0°）。必填。 | IMAGE | 是 | - |
| `左側圖片` | 左側視圖（90°），即主體的左側。 | IMAGE | 否 | - |
| `背面圖片` | 背面視圖（180°）。 | IMAGE | 否 | - |
| `右側圖片` | 右側視圖（270°），即主體的右側。 | IMAGE | 否 | - |
| `輸出模式` | 選擇要生成的模型類型。"Geometry only" 會傳回未貼紋理的網格。"Textured" 會加入色彩/PBR 貼圖。 | DYNAMIC_COMBO | 是 | "Geometry only"<br>"Textured" |
| `面數上限` | 目標面數，48-20000。-1 讓 Tripo 自適應選擇。（預設：-1） | INT | 否 | -1 至 20000 |
| `模型種子` | 用於可重現模型生成的種子。（預設：42） | INT | 否 | 0 至 2147483647 |
| `自動尺寸` | 將輸出縮放至近似真實世界的公尺單位。（預設：False） | BOOLEAN | 否 | True<br>False |
| `匯出 UV` | 生成期間進行 UV 展開。僅需幾何的執行可關閉以加快速度。（預設：True） | BOOLEAN | 否 | True<br>False |
| `壓縮幾何` | 套用 meshopt 幾何壓縮（EXT_meshopt_compression）。檔案較小，但 ComfyUI 的 3D 預覽無法顯示這些檔案；編輯前請先解壓縮。（預設：False） | BOOLEAN | 否 | True<br>False |

### Geometry only 輸入

此模式不會顯示其他輸入。生成的模型會在不含貼圖的情況下傳回。

### Textured 輸入

當 `output_mode` 設為 `"Textured"` 時，會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `pbr` | 包含 PBR 貼圖。開啟時，基礎貼圖也會強制開啟。（預設：True） | BOOLEAN | 是 | True<br>False |
| `texture_quality` | 貼圖品質等級。`detailed` = HD 貼圖，`extreme` = 8K Ultra 貼圖。（預設："standard"） | COMBO | 是 | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | 優先考慮對來源影像的視覺保真度，或與網格幾何的對齊。（預設："original_image"） | COMBO | 是 | "original_image"<br>"geometry" |
| `orientation` | 旋轉輸出以符合來源影像。僅在貼圖模式下適用。（預設："default"） | COMBO | 是 | "default"<br>"align_image" |
| `texture_seed` | 用於貼圖生成的種子。（預設：42） | INT | 是 | 0 至 2147483647 |

**注意：** 你必須至少提供 2 張影像：正面視圖（`image`）加上其他視圖中的至少一個（`image_left`、`image_back` 或 `image_right`）。如果提供的影像少於 2 張，節點會引發錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-----------|-----------|
| `模型檔案` | 生成的 GLB 模型檔名（僅供回溯相容性使用）。 | STRING |
| `模型任務 ID` | 此模型生成請求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 生成的 GLB 格式 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1153f74ac76603829142959844e701f3c8f16be080e3de849951cffdda322d12`
