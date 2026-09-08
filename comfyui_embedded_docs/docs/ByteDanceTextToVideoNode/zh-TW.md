# 字節跳動文字轉影片

# ByteDance 文本轉視頻節點

ByteDance 文本轉視頻節點透過基於文本提示的 API 使用 ByteDance 模型生成視頻。它接受文本描述和各種視頻設定作為輸入，然後創建符合提供規格的視頻。此節點處理 API 通訊並將生成的視頻作為輸出返回。

## 概述

ByteDance 文本轉視頻節點設計用於將文本提示轉換為視頻，利用 ByteDance 的 AI 能力。用戶可以指定模型、解析度、畫面比例、持續時間和其他參數以控制視頻生成過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 使用於生成的 ByteDance 模型。 | STRING | 是 | 
  - "seedance-1-5-pro-251215"
  - "seedance-1-0-pro-250528"
  - "seedance-1-0-pro-fast-251015" |
| `提示詞` | 用於生成視頻的文本提示。 | STRING | 是 | 多行文本輸入 |
| `解析度` | 輸出視頻的解析度。 | STRING | 是 | 
  - "480p"
  - "720p"
  - "1080p" |
| `長寬比` | 輸出視頻的畫面比例。 | STRING | 是 | 
  - "16:9"
  - "4:3"
  - "1:1"
  - "3:4"
  - "9:16"
  - "21:9" |
| `持續時間` | 輸出視頻的持續時間（秒）。 | INT | 是 | 3 到 12 秒 |
| `種子值` | 用於生成的種子。 | INT | 否 | 0 到 2,147,483,647 |
| `固定攝影機` | 指定是否固定攝影機。 | BOOLEAN | 否 | - |
| `浮水印` | 是否在視頻中添加 "AI generated" 水印。 | BOOLEAN | 否 | - |
| `generate_audio` | 此參數對除 `seedance-1-5-pro-251215` 模型以外的任何模型都無效。 | BOOLEAN | 否 | - |

**參數約束：**

- `prompt` 必須在去除空白後至少包含 1 個字符。
- `prompt` 不可以包含以下文本參數："resolution"、"ratio"、"duration"、"seed"、"camerafixed"、"watermark"。
- `duration` 限制在 3 到 12 秒之間的值。
- 對於 `seedance-1-5-pro-251215` 模型，最低支持的持續時間為 4 秒。
- `seed` 接受從 0 到 2,147,483,647 的值。
- `generate_audio` 參數只在 `model` 設置為 `seedance-1-5-pro-251215` 時有效；對於所有其他模型都會被忽略。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的視頻文件。 | VIDEO |

**注意：** ByteDance 文本轉視頻節點是一個 API 節點，需要通過 `auth_token_comfy_org` 和 `api_key_comfy_org` 隱藏輸入來提供身份驗證令牌和 API 金鑰以正確運作。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
