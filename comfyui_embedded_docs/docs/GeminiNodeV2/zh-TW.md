# Google Gemini

使用 Google 的 Gemini 模型產生文字回應。提供文字提示詞，並可選擇性提供一或多個圖像、音訊片段、影片或檔案作為多模態上下文。

## 輸入

### 通用輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於產生回應的 Gemini 模型。 | DYNAMIC_COMBO | 是 | `"Gemini 3.8 Flash"`<br>`"Gemini 3.7 Flash"`<br>`"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `prompt` | 輸入至模型的文字。請包含詳細的指示、問題或上下文。必須包含至少一個非空白字元。（預設值：""） | STRING | 是 |  |
| `seed` | 取樣用的種子。設為 0 即使用隨機種子。不保證輸出具有確定性。（預設值：42） | INT | 是 | 0 至 2147483647 |
| `system_prompt` | 決定模型行為的基礎指示。（預設值：""） | STRING | No |  |

### Gemini 3.8 Flash 輸入

當 `model` 設為 `"Gemini 3.8 Flash"` 時，會顯示這些輸入。

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | 模型在回答前進行內部推理的強度。HIGH 可提升困難任務的品質，但會消耗更多（思考）token 且速度較慢。（預設值："MEDIUM"） | COMBO | 是 | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `max_output_tokens` | 要產生的最大 token 數，包含模型內部的思考。當 thinking_level 為 HIGH 時，數值過低可能導致沒有空間產生答案；若回應為空或被截斷，請調高此值。模型完成後會提前停止，因此對於簡短回覆而言，較高的上限不會增加額外成本。（預設值：32768） | INT | 是 | 16 至 65536 |

**注意：** 此模型未提供 `temperature` 或 `top_p` 取樣控制項。

### Gemini 3.7 Flash 輸入

當 `model` 設為 `"Gemini 3.7 Flash"` 時，會顯示這些輸入。

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | 模型在回答前進行內部推理的強度。HIGH 可提升困難任務的品質，但會消耗更多（思考）token 且速度較慢。（預設值："MEDIUM"） | COMBO | 是 | `"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | 控制隨機性。數值越低越聚焦／越具確定性，數值越高越有創意。（預設值：1.0） | FLOAT | 是 | 0.0 至 2.0 |
| `top_p` | 核取樣（nucleus sampling）：從累積機率達到 top_p 的最小 token 集合中取樣。（預設值：0.95） | FLOAT | 是 | 0.0 至 1.0 |
| `max_output_tokens` | 要產生的最大 token 數，包含模型內部的思考。當 thinking_level 為 HIGH 時，數值過低可能導致沒有空間產生答案；若回應為空或被截斷，請調高此值。模型完成後會提前停止，因此對於簡短回覆而言，較高的上限不會增加額外成本。（預設值：32768） | INT | 是 | 16 至 65536 |

### Gemini 3.5 Flash 輸入

當 `model` 設為 `"Gemini 3.5 Flash"` 時，會顯示這些輸入。

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | 模型在回答前進行內部推理的強度。HIGH 可提升困難任務的品質，但會消耗更多（思考）token 且速度較慢。（預設值："MEDIUM"） | COMBO | 是 | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | 控制隨機性。數值越低越聚焦／越具確定性，數值越高越有創意。（預設值：1.0） | FLOAT | 是 | 0.0 至 2.0 |
| `top_p` | 核取樣（nucleus sampling）：從累積機率達到 top_p 的最小 token 集合中取樣。（預設值：0.95） | FLOAT | 是 | 0.0 至 1.0 |
| `max_output_tokens` | 要產生的最大 token 數，包含模型內部的思考。當 thinking_level 為 HIGH 時，數值過低可能導致沒有空間產生答案；若回應為空或被截斷，請調高此值。模型完成後會提前停止，因此對於簡短回覆而言，較高的上限不會增加額外成本。（預設值：32768） | INT | 是 | 16 至 65536 |

### Gemini 3.1 Pro 輸入

當 `model` 設為 `"Gemini 3.1 Pro"` 時，會顯示這些輸入。

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | 模型在回答前進行內部推理的強度。HIGH 可提升困難任務的品質，但會消耗更多（思考）token 且速度較慢。（預設值："HIGH"） | COMBO | 是 | `"LOW"`<br>`"HIGH"` |
| `temperature` | 控制隨機性。數值越低越聚焦／越具確定性，數值越高越有創意。（預設值：1.0） | FLOAT | 是 | 0.0 至 2.0 |
| `top_p` | 核取樣（nucleus sampling）：從累積機率達到 top_p 的最小 token 集合中取樣。（預設值：0.95） | FLOAT | 是 | 0.0 至 1.0 |
| `max_output_tokens` | 要產生的最大 token 數，包含模型內部的思考。當 thinking_level 為 HIGH 時，數值過低可能導致沒有空間產生答案；若回應為空或被截斷，請調高此值。模型完成後會提前停止，因此對於簡短回覆而言，較高的上限不會增加額外成本。（預設值：32768） | INT | 是 | 16 至 65536 |

### Gemini 3.1 Flash-Lite 輸入

當 `model` 設為 `"Gemini 3.1 Flash-Lite"` 時，會顯示這些輸入。

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | 模型在回答前進行內部推理的強度。HIGH 可提升困難任務的品質，但會消耗更多（思考）token 且速度較慢。（預設值："LOW"） | COMBO | 是 | `"LOW"`<br>`"HIGH"` |
| `temperature` | 控制隨機性。數值越低越聚焦／越具確定性，數值越高越有創意。（預設值：1.0） | FLOAT | 是 | 0.0 至 2.0 |
| `top_p` | 核取樣（nucleus sampling）：從累積機率達到 top_p 的最小 token 集合中取樣。（預設值：0.95） | FLOAT | 是 | 0.0 至 1.0 |
| `max_output_tokens` | 要產生的最大 token 數，包含模型內部的思考。當 thinking_level 為 HIGH 時，數值過低可能導致沒有空間產生答案；若回應為空或被截斷，請調高此值。模型完成後會提前停止，因此對於簡短回覆而言，較高的上限不會增加額外成本。（預設值：32768） | INT | 是 | 16 至 65536 |

### 媒體與檔案輸入

以下輸入由所有模型共用，並與各模型專屬的輸入一併顯示。

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | 可擴充插槽：連接 1 至 16 張圖像（`image_1` ... `image_16`）。可選的圖像，用作模型的上下文。最多 16 張圖像。 | IMAGE | No | 0 至 16 張圖像 |
| `audio` | 可擴充插槽：連接一個音訊片段（`audio_1`）。可選的音訊片段，用作模型的上下文。 | AUDIO | No | 0 至 1 個片段 |
| `video` | 可擴充插槽：連接一個影片片段（`video_1`）。可選的影片片段，用作模型的上下文。 | VIDEO | No | 0 至 1 個片段 |
| `files` | 可選的檔案，用作模型的上下文。接受來自 Gemini Input Files 節點的輸入。 | GEMINI_INPUT_FILES | No |  |

**注意：** 當附加媒體（圖像、音訊或影片）時，節點會將前 10 個媒體項目上傳至 ComfyAPI 儲存空間，並以 URL 形式傳遞；此 URL 額度由所有媒體類型共用，並依序消耗（影片優先，其次音訊，最後圖像）。其餘媒體會以 base64 資料內嵌編碼，內嵌內容的合計上限為 18 MB。若內嵌內容會超過 18 MB，節點會引發錯誤。`prompt` 參數必須包含至少一個非空白字元。將 `seed` 設為 0 會要求使用隨機種子。

## 輸出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | 來自 Gemini 模型所產生的文字回應。若模型未產生任何文字，則會回傳字串 "Empty response from Gemini model..."。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `98a19d1b29e80907477d24d813593950a028021ee8bcf634f505e11a15daa383`
