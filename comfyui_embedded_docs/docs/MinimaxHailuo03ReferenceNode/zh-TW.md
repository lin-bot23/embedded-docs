# MiniMax H3 參考生成影片

此節點會以參考圖片、影片及音訊為條件，使用 MiniMax H3 模型生成影片。參考素材在提示詞中依連接順序被引用，例如「Image 1」、「Image 2」、「Video 1」、「Audio 1」等。提供兩種模型：「MiniMax H3」與「MiniMax H3 Max」。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於影片生成的模型（預設值：「MiniMax H3」）。選擇「MiniMax H3」會提供下列 MiniMax H3 生成輸入與參考輸入。選擇「MiniMax H3 Max」則會提供下列 MiniMax H3 Max 生成輸入與參考輸入。 | DYNAMIC_COMBO | 是 | "MiniMax H3"<br>"MiniMax H3 Max" |
| `隨機種子` | 隨機種子。相同請求搭配相同種子會產生相似，但不保證完全相同的結果（預設值：42）。 | INT | 是 | 0 至 4294967295 |
| `浮水印` | 是否在影片中加入 AIGC 浮水印（預設值：false）。僅 MiniMax H3 模型支援此選項。 | BOOLEAN | 否 | true<br>false |

### MiniMax H3 輸入

當選擇「MiniMax H3」作為模型時，可使用下列輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的提示詞。可以依順序引用參考媒體，例如「Image 1」、「Image 2」、「Video 1」或「Audio 1」。 | STRING | 是 | 至少 1 個字元 |
| `resolution` | 輸出影片的解析度（預設值：「768P」）。 | COMBO | 是 | "768P"<br>"2K" |
| `ratio` | 輸出影片的長寬比（預設值：「adaptive」）。 | COMBO | 是 | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | 輸出影片的持續時間（秒）（預設值：5）。 | INT | 是 | 4 至 15 |

### MiniMax H3 Max 輸入

當選擇「MiniMax H3 Max」作為模型時，可使用下列輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的提示詞。可以依順序引用參考媒體，例如「Image 1」、「Image 2」、「Video 1」或「Audio 1」。 | STRING | 是 | 1 至 50000 個字元 |
| `resolution` | 輸出影片的解析度（預設值：「768P」）。 | COMBO | 是 | "480P"<br>"768P" |
| `ratio` | 輸出影片的長寬比（預設值：「adaptive」）。 | COMBO | 是 | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | 輸出影片的持續時間（秒）（預設值：5）。 | INT | 是 | 5 至 15 |
| `prompt_expansion_mode` | 生成前花費多少心力改寫提示詞（預設值：「balanced」）。 | COMBO | 是 | "balanced"<br>"quality" |
| `reference_detail` | 傳送參考圖片時的細節等級。「high」會以模型使用的最大尺寸傳送圖片（短邊最長 2048 像素）；「standard」則會將圖片縮小至最多 2048x1024，以降低參考成本（預設值：「standard」）。 | COMBO | 是 | "high"<br>"standard" |

### 參考輸入

下列參考輸入由兩種模型共用。每一項皆為可增長的插槽。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可增長的插槽：最多可連接 9 個項目（`image_1`...`image_9`）。主體或風格參考圖片，在提示詞中依連接順序以「Image 1」至「Image 9」引用。最多 9 張圖片。 | IMAGE | 否 | 0 至 9 張圖片 |
| `reference_videos` | 可增長的插槽：最多可連接 3 個項目（`video_1`...`video_3`）。動態或場景參考影片，在提示詞中依連接順序以「Video 1」至「Video 3」引用。最多 3 段影片，每段 2-15 秒，總長最多 15 秒。 | VIDEO | 否 | 0 至 3 段影片 |
| `reference_audios` | 可增長的插槽：最多可連接 3 個項目（`audio_1`...`audio_3`）。音訊參考，在提示詞中依連接順序以「Audio 1」至「Audio 3」引用。最多 3 段，每段 2-15 秒，總長最多 15 秒。若無參考圖片或參考影片，則無法使用。 | AUDIO | 否 | 0 至 3 段 |

### 參數限制

- 至少需要一張參考圖片或一段參考影片。不接受僅提供參考音訊。
- 每張參考圖片的長寬比必須約在 0.4 至 2.5（2:5 至 5:2）之間，且寬度與高度皆至少為 256 像素。
- 每段參考影片長度必須在 2 至 15 秒之間，幀率介於 23.976 至 60 FPS。所有參考影片的總時長不得超過 15 秒。
- 每個參考音訊片段長度必須在 2 至 15 秒之間。所有參考音訊片段的總時長不得超過 15 秒。
- 選擇「MiniMax H3 Max」時，必須停用 `watermark` 設定。
- 選擇「MiniMax H3 Max」時，參考檔案（圖片、影片與音訊合計）總數不得超過 12。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b77eedb1f7757e60518c04484f1cc24c27cf6886b3ae31c15207ea49fd436a73`
