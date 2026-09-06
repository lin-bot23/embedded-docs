# MiniMax H3 首末幀生成影片

此節點使用 MiniMax H3 模型，從第一幀影像以及可選的最後一幀影像生成影片。`model` 選擇器會變更適用的生成設定與約束條件，而生成影片的長寬比會與提供的影像一致。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的模型。選取模型後，下方會顯示該模型專屬的設定。 | DYNAMIC_COMBO | 是 | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `first_frame` | 影片的第一幀影像。生成影片的長寬比會與此影像一致。 | IMAGE | 是 | - |
| `last_frame` | 可選的影片最後一幀影像。提供此影像時，影片會從第一幀朝此最後一幀生成。 | IMAGE | 否 | - |
| `seed` | 隨機種子。使用相同種子的相同請求會產生相似但無法保證完全相同的結果。包含「生成後控制」選項。預設值：42。 | INT | 是 | 0 到 4294967295 |
| `watermark` | 是否為影片加入 AIGC 浮水印。這是進階參數。僅 `MiniMax H3` 模型支援。預設值：False。 | BOOLEAN | 是 | True<br>False |

### MiniMax H3 輸入

當在 `model` 選擇器中選取 `MiniMax H3` 時，會顯示這些設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。必須包含至少一個非空白字元。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "768P"<br>"2K" |
| `duration` | 輸出影片的時長（秒）。預設值：5。 | INT | 是 | 4 到 15 |

### MiniMax H3 Max 與 MiniMax H3 Max Turbo 輸入

當在 `model` 選擇器中選取 `MiniMax H3 Max` 或 `MiniMax H3 Max Turbo` 時，會顯示這些設定。兩個模型有相同的設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。不得為空或僅含空白字元，且長度限制為 50,000 個字元。 | STRING | 是 | 多行文字 |
| `resolution` | 輸出影片的解析度。預設值：768P。 | COMBO | 是 | "480P"<br>"768P" |
| `duration` | 輸出影片的時長（秒）。預設值：5。 | INT | 是 | 5 到 15 |
| `prompt_expansion_mode` | 在生成前投入多少心力來重寫提示詞。預設值：balanced。 | COMBO | 是 | "balanced"<br>"quality" |

**約束條件說明：**

- 提示詞必須包含文字：空白或僅含空白字元的提示詞會被拒絕。
- 任何提供的幀影像寬和高都必須至少為 256 像素，且寬高比需介於 0.4 與 2.5 之間（約 2:5 到 5:2）。此要求適用於 `first_frame`，若提供了 `last_frame`，也同樣適用。
- 省略 `last_frame` 時，影片僅由第一幀生成。
- 輸出影片的長寬比會與提供的影像一致。
- `watermark` 僅受 `MiniMax H3` 支援。在 `MiniMax H3 Max` 或 `MiniMax H3 Max Turbo` 上啟用此參數會產生錯誤。
- `MiniMax H3` 的時長範圍為 4 到 15 秒；`MiniMax H3 Max` 和 `MiniMax H3 Max Turbo` 的時長範圍為 5 到 15 秒。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 使用所選的 MiniMax H3 模型，由第一幀與可選的最後一幀所生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6eaf895e6e9e46b9a1efb1dd13e951040e12e865cc73d7741ab7546f5f8f9ec0`
