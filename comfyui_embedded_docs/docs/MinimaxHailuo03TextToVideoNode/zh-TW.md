# MiniMax H3 文生影片

此節點使用 MiniMax H3 系列模型（MiniMax H3、MiniMax H3 Max 與 MiniMax H3 Max Turbo）從文字提示詞生成影片。您可以選擇模型、輸入文字提示詞，並調整解析度、畫面比例與影片長度等設定。節點會將請求傳送至 MiniMax API，等待生成任務完成，並回傳產生的影片。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於影片生成的模型（預設：「MiniMax H3」）。選取模型後，也會顯示下列小節所述、專屬於該模型的設定。 | DYNAMIC_COMBO | 是 | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `隨機種子` | 隨機種子。使用相同種子的相同請求會產生相似但不保證完全相同的結果（預設：42）。 | INT | 是 | 0 至 4294967295 |
| `浮水印` | 是否在影片中加入 AIGC 浮水印（預設：false）。啟用此功能時，僅支援「MiniMax H3」模型。 | BOOLEAN | 否 | true<br>false |

### MiniMax H3 輸入

當選取「MiniMax H3」模型時，會顯示以下設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示詞。必須包含至少一個非空白字元。 | STRING | 是 | 任意文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "768P"<br>"2K" |
| `ratio` | 輸出影片的畫面比例（預設：「16:9」）。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | 輸出影片的長度，單位為秒（4-15）（預設：5）。 | INT | 是 | 4 至 15 |

### MiniMax H3 Max 與 MiniMax H3 Max Turbo 輸入

這些設定由「MiniMax H3 Max」與「MiniMax H3 Max Turbo」模型共用，並在選取任一模型時顯示。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示詞。必須包含至少一個非空白字元，且最多可長達 50,000 個字元。 | STRING | 是 | 最多 50000 個字元 |
| `resolution` | 輸出影片的解析度（預設：「768P」）。 | COMBO | 是 | "480P"<br>"768P" |
| `ratio` | 輸出影片的畫面比例（預設：「16:9」）。 | COMBO | 是 | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | 輸出影片的長度，單位為秒（5-15）（預設：5）。 | INT | 是 | 5 至 15 |
| `prompt_expansion_mode` | 在生成前投入多少心力重新編寫提示詞（預設：「balanced」）。 | COMBO | 是 | "balanced"<br>"quality" |

### 注意事項

- 所有模型的提示詞都必須包含至少一個非空白字元。
- `watermark` 設定僅「MiniMax H3」支援。若搭配「MiniMax H3 Max」或「MiniMax H3 Max Turbo」啟用，會產生錯誤。
- 「MiniMax H3 Max」與「MiniMax H3 Max Turbo」模型會將提示詞限制為 50,000 個字元。
- 解析度與長度限制取決於所選模型：「MiniMax H3」支援「768P」與「2K」解析度，以及 4-15 秒的影片；「MiniMax H3 Max」與「MiniMax H3 Max Turbo」則支援「480P」與「768P」解析度，以及 5-15 秒的影片。
- 此節點顯示的預估費用是根據所選的模型、解析度與影片長度計算。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `VIDEO` | 由提供的文字提示詞所產生的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4d3de190d18de4370aff878279755e881841d2ada28320a7c1d7c52061071c05`
