# 切換

Switch 節點會根據布林條件在兩個可能的輸入之間進行選擇。當 `switch` 啟用（true）時，會將 `on_true` 輸入傳遞到輸出；當停用（false）時，則會傳遞 `on_false`。只有被選取的分支會被評估，因此另一個輸入不需要連線。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `切換` | 決定要傳遞哪一個輸入的布林條件。啟用（true）時，會選取 `on_true` 輸入；停用（false）時，則會選取 `on_false` 輸入。 | BOOLEAN | 是 |  |
| `為假時` | 當 `switch` 停用（false）時，要傳遞到輸出的資料。只有在 `switch` 為 false 時才需要此輸入。 | MATCH_TYPE | 否 |  |
| `為真時` | 當 `switch` 啟用（true）時，要傳遞到輸出的資料。只有在 `switch` 為 true 時才需要此輸入。 | MATCH_TYPE | 否 |  |

**關於輸入需求的說明：** `on_false` 與 `on_true` 輸入是條件式必要的。節點僅在 `switch` 為 true 時要求 `on_true` 輸入，並僅在 `switch` 為 false 時要求 `on_false` 輸入。兩個輸入都必須具有相同的資料類型，且必須與輸出的資料類型相符。如果選取的輸入未連線，節點就不會輸出任何值。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `輸出` | 被選取的資料。當 `switch` 為 true 時，此為 `on_true` 輸入的值；當 `switch` 為 false 時，此為 `on_false` 輸入的值。 | MATCH_TYPE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
