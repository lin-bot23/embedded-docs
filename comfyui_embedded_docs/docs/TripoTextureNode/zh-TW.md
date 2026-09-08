# Tripo：紋理模型

TripoTextureNode 節點使用 Tripo API 為現有的 Tripo 3D 模型添加紋理。它會接收由其他 Tripo 節點所建立的模型任務 ID，並在紋理任務完成後回傳具有紋理的 GLB 或 FBX 模型。您可以控制材質貼圖、紋理品質、對齊方式、種子，並可透過文字提示、風格圖片或參考圖片來引導紋理生成。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型任務ID` | 要添加紋理的 Tripo 模型任務 ID。接受模型任務 ID 與分割任務 ID。 | MODEL_TASK_ID | 是 | - |
| `紋理` | 已忽略：此節點一律會生成紋理。為舊版工作流程保留。（預設值：True） | BOOLEAN | 否 | true<br>false |
| `PBR材質` | PBR 材質貼圖（基底色、金屬度、粗糙度、法線）；關閉時會產生純色紋理。（預設值：True） | BOOLEAN | 否 | true<br>false |
| `紋理種子` | 紋理生成的隨機種子。使用相同種子與相同輸入會產生相同結果。（預設值：42） | INT | 否 | 0 – 2147483647 |
| `紋理品質` | 紋理解析度品質：detailed = HD 紋理，extreme = 8K Ultra 紋理。（預設值："standard"）。約略費用：standard $0.10、detailed $0.20、extreme $0.30。 | COMBO | 否 | "standard"<br>"detailed"<br>"extreme" |
| `紋理對齊` | 用於將生成的紋理對齊至模型的方法。（預設值："original_image"）。 | COMBO | 否 | "original_image"<br>"geometry" |
| `texture_prompt` | 用於紋理生成的選用文字指引。對於匯入的模型（Tripo: Import Model）在實務上為必填，因為這類模型沒有可用於推斷顏色的來源圖片。無法與參考圖片同時使用。（預設值：""） | STRING | 否 | - |
| `model_version` | 紋理模型：v3.0 用於以 v3.x 生成的網格，v2.5 用於以 v2.5 生成的網格。（預設值：最新的 v3.0 版本） | COMBO | 否 | Multiple options available |
| `style_image` | 紋理藝術風格的參考圖片。僅與 `texture_prompt` 一起使用。 | IMAGE | 否 | - |
| `參考` | 引導紋理生成的參考圖片。無法與 `texture_prompt` 或 `style_image` 同時使用。（預設值："none"） | DYNAMIC_COMBO | 否 | "none"<br>"image"<br>"multiview" |
| `part_names` | 以逗號分隔的部分名稱，這些部分名稱來自 Tripo 的「Segment Model」，用於指定要貼紋理的部分。留空則會為所有部分生成紋理。（預設值：""） | STRING | 否 | - |

### "image" 參考輸入

當 `reference` 設為 `"image"` 時，可使用以下輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | 紋理應遵循的單張參考圖片。 | IMAGE | 否 | - |

### "multiview" 參考輸入

當 `reference` 設為 `"multiview"` 時，可使用以下輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image_front` | 前視圖（0°）。 | IMAGE | 否 | - |
| `image_left` | 左視圖（90°）。 | IMAGE | 否 | - |
| `image_back` | 後視圖（180°）。 | IMAGE | 否 | - |
| `image_right` | 右視圖（270°）。 | IMAGE | 否 | - |

**注意：** `"image"` 與 `"multiview"` 參考模式無法與非空的 `texture_prompt` 或 `style_image` 同時使用。`style_image` 輸入需要非空的 `texture_prompt`。當 `texture_prompt` 保留空白時，來源模型必須已經擁有自己的來源圖片（例如由文字生成模型、圖片生成模型、多視圖生成模型或較早的紋理任務所產生的模型）。沒有來源圖片的模型——例如匯入、分割、補全或重新拓撲的模型——必須搭配 `texture_prompt` 進行紋理化；參考圖片僅接受 Tripo API 自行生成的模型使用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 生成的模型檔案（僅供向後相容）。 | STRING |
| `模型任務 ID` | 已完成紋理生成任務的任務 ID，可作為其他 Tripo 節點的輸入。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的紋理模型。若來源為四邊網格或 FBX 匯入，則此值為空。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的紋理模型。對四邊網格與 FBX 匯入，Tripo 會回傳 FBX；其他情況則為空。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `815c22a9d8f4785ef5219789e0f2eee804776ec7e4752099ec0db0a2b5ad4bb2`
