# Recraft V4 建立風格

此節點可從 1 到 10 張參考影像建立可重複使用的 Recraft V4 風格。傳回的風格 ID 可搭配相同輸出類型（點陣圖或向量圖）的所有 Recraft V4 與 V4.1 模型使用，並可在後續的影像生成步驟中重複使用。所有參考影像的總大小限制為 10 MB。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 建立此風格所適用的模型。Standard 與 Pro 共用同一個風格池：點陣圖風格可搭配所有 Recraft V4 與 V4.1 點陣圖模型使用，向量風格（*_vector）則可搭配所有 V4 與 V4.1 向量模型使用。 | COMBO | 是 | "recraftv4_styles"<br>"recraftv4_styles_vector"<br>"recraftv4_styles_pro"<br>"recraftv4_styles_pro_vector" |
| `images` | 定義此風格的參考影像。相似的參考影像會強化比對結果，多樣化的參考影像則會擴大風格範圍。可擴充插槽：可連接 1 到 10 張影像（`image_1` 至 `image_10`）。 | IMAGE | 是 | 1 到 10 張影像 |

### 備註

- 至少需要一張參考影像；若未提供任何影像，節點會回報錯誤。
- 最多允許 10 張參考影像；若提供超過 10 張，節點會回報錯誤。
- 所有參考影像的編碼後總大小不得超過 10 MB；若超過此限制，節點會回報錯誤。
- 每張參考影像在傳送至 Recraft API 前，會先縮小至最多 2048×2048 像素，並編碼為 WebP 格式。
- 結尾為 `_vector` 的模型會建立向量風格；其他選項則建立點陣圖風格。在每種輸出類型中，Standard 與 Pro 模型共用相同的風格池。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `style_id` | 所建立風格的唯一識別碼，可搭配相同輸出類型的所有 Recraft V4 與 V4.1 模型使用。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7b907a975ed88dcca6bf1e0431ef7a9b561852ca7263a4f3298df980fe9431e5`
