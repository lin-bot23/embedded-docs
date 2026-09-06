# 字節跳動圖片轉影片

# ByteDance 圖片轉影片節點

ByteDance 圖片轉影片節點使用 ByteDance 的 API，從輸入圖片和文字提示生成影片。它會創建一個視覺上呈現所提供描述的影片序列，並提供選項以自訂輸出畫質、畫面比例、持續時間和其他參數。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 使用於影片生成的 ByteDance 模型。可用的選項有：<br>`"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` | STRING | 是 | 如上所示 |
| `prompt` | 用於生成影片的文字提示。必須至少包含 1 個字符，在刪除空白後。 | STRING | 是 | - |
| `image` | 用於影片的第一個畫面。圖片大小必須在 300x300 和 6000x6000 像素之間，畫面比例在 0.4 和 2.5 之間。 | IMAGE | 是 | - |
| `resolution` | 輸出影片的畫質。可用的選項有：<br>`"480p"`<br>`"720p"`<br>`"1080p"` | STRING | 是 | 如上所示 |
| `aspect_ratio` | 輸出影片的畫面比例。可用的選項有：<br>`"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | STRING | 是 | 如上所示 |
| `duration` | 輸出影片的持續時間（秒）。對於 `seedance-1-5-pro-251215` 模型，最低支援持續時間為 4 秒。 | INT | 是 | 3 - 12 |
| `seed` | 用於生成的種子。選擇性，默認值為 0。 | INT | 否 | 0 - 2147483647 |
| `camera_fixed` | 指定是否固定攝影機。平台會將固定攝影機的指示添加到您的提示中，但不保證實際效果。選擇性，默認值為 False。 | BOOLEAN | 否 | - |
| `watermark` | 是否在影片中添加 "AI 生成的" 水印。選擇性，默認值為 False。 | BOOLEAN | 否 | - |
| `generate_audio` | 此參數對除 `seedance-1-5-pro-251215` 模型以外的任何模型都無效。選擇性，默認值為 False。 | BOOLEAN | 否 | - |

**注意：** 提示中不得包含以下單詞（不區分大小寫）：`resolution`、`ratio`、`duration`、`seed`、`camerafixed`、`watermark`。這些參數通過其專屬輸入設置。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 基於輸入圖片和提示參數生成的影片文件。 | VIDEO |

上述文檔反映了從源代碼中提取的信息，並遵守了對文檔結構和內容指定的指南。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9f4ad18642533689f9c664f2ca6a4ce8e92c8698754cdf9b6bb2d2735bc80415`
