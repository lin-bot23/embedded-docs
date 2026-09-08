# HiDream-O1 參考圖像

此節點將參考圖片附加至正向與負向條件，供下游節點使用以引導生成。參考圖片按照其輸入插槽的數字順序套用。如果沒有連接任何參考圖片，正向與負向條件會原樣通過。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 要附加參考圖片的正向條件。 | CONDITIONING | 是 | - |
| `負向` | 要附加參考圖片的負向條件。 | CONDITIONING | 是 | - |
| `參考圖像` | 參考圖片依數字插槽順序使用。提供圖片時，圖片會附加至正向與負向條件。 | IMAGE | 否 | 0 到 100 張圖片（`image_1` 至 `image_100`） |

**關於 `images` 參數的說明：** 這是一個自動擴充（autogrow）輸入，提供編號插槽 `image_1` 至 `image_100`。圖片依數字插槽順序使用。此輸入為可選：若未連接任何參考圖片，節點會原樣回傳 `positive` 與 `negative` 條件。連接圖片時，同一組參考圖片會附加至兩個輸出，且負向條件會在附加圖片前先被標記為負向。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正向` | 已附加參考圖片的正向條件。 | CONDITIONING |
| `負向` | 已附加參考圖片的負向條件。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/zh-TW.md)

---
**Source fingerprint (SHA-256):** `07f9f0ea19957523e95d04b9086dc994807bb0cd5262fe798dc784c1ecb4920d`
