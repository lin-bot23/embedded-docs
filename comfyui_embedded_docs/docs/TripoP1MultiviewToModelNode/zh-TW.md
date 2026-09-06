# Tripo P1：多視角轉模型

此節點會根據物件或角色的兩到四張參考影像生成 3D 模型。提供正面視圖，再加上左側、背面及右側視圖的任意組合，節點便會以 GLB 網格形式傳回重建主體。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 正面視圖（0°）。必填。 | IMAGE | 是 | - |
| `image_left` | 左側視圖（90°），即主體左側。 | IMAGE | 否 | - |
| `image_back` | 背面視圖（180°）。 | IMAGE | 否 | - |
| `image_right` | 右側視圖（270°），即主體右側。 | IMAGE | 否 | - |
| `output_mode` | 選擇要生成的模型類型。"Geometry only" 會傳回未經紋理處理的網格；"Textured" 則會加入顏色／PBR 貼圖。 | DYNAMIC_COMBO | 是 | "Geometry only"<br>"Textured" |
| `face_limit` | 目標面數，範圍 48-20000。-1 讓 Tripo 自適應選擇。（預設值：-1） | INT | 否 | -1 至 20000 |
| `model_seed` | 用於可重現模型生成的種子。（預設值：42） | INT | 否 | 0 至 2147483647 |
| `auto_size` | 將輸出縮放到接近真實世界公尺數。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `export_uv` | 在生成期間執行 UV 拆解。若為僅幾何執行，關閉可加快速度。（預設值：True） | BOOLEAN | 否 | True<br>False |
| `compress_geometry` | 套用 meshopt 幾何壓縮（EXT_meshopt_compression）。檔案較小，但 ComfyUI 的 3D 預覽無法顯示；編輯前需先解壓縮。（預設值：False） | BOOLEAN | 否 | True<br>False |

### 僅幾何輸入

此模式不會顯示額外輸入。生成的模型會以未經紋理處理的狀態傳回。

### 紋理輸入

當 `output_mode` 設定為 `"Textured"` 時，就會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `pbr` | 包含 PBR 貼圖。開啟時，基底紋理也會強制開啟。（預設值：True） | BOOLEAN | 是 | True<br>False |
| `texture_quality` | 紋理品質等級。`detailed` = HD 紋理，`extreme` = 8K Ultra 紋理。（預設值："standard"） | COMBO | 是 | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | 選擇優先保持來源影像的視覺保真度，或是對齊網格幾何。（預設值："original_image"） | COMBO | 是 | "original_image"<br>"geometry" |
| `orientation` | 旋轉輸出以配合來源影像。僅在紋理模式下套用。（預設值："default"） | COMBO | 是 | "default"<br>"align_image" |
| `texture_seed` | 用於紋理生成的種子。（預設值：42） | INT | 是 | 0 至 2147483647 |

**注意：** 您至少必須提供 2 張影像：正面視圖（`image`）加上其他視圖（`image_left`、`image_back` 或 `image_right`）中的至少一張。如果提供的影像少於 2 張，節點將回報錯誤。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 生成的 GLB 模型檔案名稱（僅供向後相容使用）。 | STRING |
| `model_task_id` | 此模型生成要求的唯一任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c26bf9d46f6b95ec57e4eb663cb6c602035c3ad00682e7f9622ce575ff54d228`
