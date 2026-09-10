# Tripo：紋理模型

此節點在原始碼中標記為已棄用（legacy）；顯示名稱為「Tripo: Texture model (Legacy)」。

Tripo: Texture model (Legacy) 節點透過 Tripo API 為現有的 Tripo 3D 模型加上紋理。它會接收由其他 Tripo 節點所建立模型的任務 ID，並在紋理工作完成後傳回已加上紋理的 GLB 或 FBX 模型。你可以控制材質貼圖、紋理品質、對齊與 seed，並透過文字提示、風格圖片或參考圖片引導紋理。此節點是紋理工具的 legacy 版本。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型任務ID` | 要加上紋理的模型 Tripo 任務 ID。接受模型任務 ID 與分割任務 ID。 | MODEL_TASK_ID, SEGMENT_TASK_ID | 是 | - |
| `紋理` | 已忽略：此節點一律會產生紋理。保留是為了舊版工作流程。（預設：True） | BOOLEAN | 否 | true<br>false |
| `PBR材質` | PBR 材質貼圖（base color、metallic、roughness、normal）；關閉時會產生純色紋理。（預設：True） | BOOLEAN | 否 | true<br>false |
| `紋理種子` | 用於紋理生成的隨機 seed。（預設：42） | INT | 否 | 0 – 2147483647 |
| `紋理品質` | 紋理解析度品質：detailed = HD 紋理，extreme = 8K Ultra 紋理。（預設："standard"）。約略費用：standard $0.10、detailed $0.20、extreme $0.30。 | COMBO | 否 | "standard"<br>"detailed"<br>"extreme" |
| `紋理對齊` | 用於將產生的紋理對齊至模型的方法。（預設："original_image"） | COMBO | 否 | "original_image"<br>"geometry" |
| `texture_prompt` | 用於引導紋理生成的選用文字提示。實務上，對於匯入模型（Tripo: Import Model）而言是必要的，因為這些模型沒有可用來推斷顏色的來源圖片。不能與參考圖片同時使用。（預設：""） | STRING | 否 | - |
| `model_version` | 紋理模型：v3.0 用於以 v3.x 產生的網格，v2.5 用於以 v2.5 產生的網格。（預設：v3.0_20250812） | COMBO | 否 | 有多個可用選項 |
| `style_image` | 用於紋理藝術風格的參考圖片。僅與 `texture_prompt` 搭配使用。 | IMAGE | 否 | - |
| `參考` | 引導紋理的參考圖片。不能與 `texture_prompt` 或 `style_image` 同時使用。（預設："none"） | DYNAMIC_COMBO | 否 | "none"<br>"image"<br>"multiview" |
| `part_names` | 從 Tripo: Segment Model 取得、以逗號分隔的部件名稱，用於指定要加上紋理的部件。留空時會為每個部件加上紋理。（預設：""） | STRING | 否 | - |

### `image` 參考輸入

當 `reference` 設為 `"image"` 時，這些輸入可用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | 紋理應遵循的單一參考圖片。 | IMAGE | 是 | - |

### `multiview` 參考輸入

當 `reference` 設為 `"multiview"` 時，這些輸入可用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image_front` | 正面視圖（0°）。 | IMAGE | 是 | - |
| `image_left` | 左側視圖（90°）。 | IMAGE | 是 | - |
| `image_back` | 背面視圖（180°）。 | IMAGE | 是 | - |
| `image_right` | 右側視圖（270°）。 | IMAGE | 是 | - |

**注意：** `"image"` 與 `"multiview"` 參考模式不能與非空的 `texture_prompt` 或 `style_image` 同時使用。`style_image` 輸入需要非空的 `texture_prompt`。當 `texture_prompt` 留空時，來源模型必須已經有自己的來源圖片（例如由 text-to-model、image-to-model、multiview-to-model 或先前的紋理任務所產生的模型）。沒有來源圖片的模型——例如匯入、分割、完成或重新拓撲的模型——必須使用 `texture_prompt` 來加上紋理；只有 Tripo API 自行產生的模型才接受參考圖片。`part_names` 輸入可以留空，以對每個部件加上紋理。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 產生的模型檔案（僅供回溯相容性使用）。 | STRING |
| `模型任務 ID` | 已完成紋理生成任務的任務 ID，可作為其他 Tripo 節點的輸入。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式產生的已加上紋理模型。當來源是四邊形網格或 FBX 匯入時，此輸出為空。 | FILE3DGLB |
| `FBX` | 以 FBX 格式產生的已加上紋理模型。Tripo 會為四邊形網格與 FBX 匯入傳回 FBX；其他情況為空。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`
