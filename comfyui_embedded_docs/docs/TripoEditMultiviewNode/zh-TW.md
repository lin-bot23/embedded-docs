# Tripo：編輯多視角

使用針對每個視圖的個別文字指令，編輯 Tripo: Image to Multiview 結果的視圖。沒有指令的視圖會保持不變。編輯後的影像旨在連接到 Tripo: Multiview to Model 以建立 3D 模型；已編輯的多視圖組合無法再次編輯。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `multiview_task_id` | 要編輯其視圖的 Tripo: Image to Multiview 結果的工作 ID。必須來自 Tripo: Image to Multiview 節點。 | MULTIVIEW_TASK_ID | 是 | Task ID |
| `front_prompt` | 描述要套用至前視圖編輯的文字指令。為空時，前視圖會保持不變。預設：空字串。 | STRING | 否 | Multiline text |
| `left_prompt` | 描述要套用至左視圖編輯的文字指令。為空時，左視圖會保持不變。預設：空字串。 | STRING | 否 | Multiline text |
| `back_prompt` | 描述要套用至後視圖編輯的文字指令。為空時，後視圖會保持不變。預設：空字串。 | STRING | 否 | Multiline text |
| `right_prompt` | 描述要套用至右視圖編輯的文字指令。為空時，右視圖會保持不變。預設：空字串。 | STRING | 否 | Multiline text |

注意：四個提示參數（`front_prompt`、`left_prompt`、`back_prompt`、`right_prompt`）中至少要有一個包含非空文字；只有空白的文字會被視為空，如果所有提示參數皆為空，此節點會引發錯誤。

注意：每個具有編輯指令的視圖費用約為 0.05 USD。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `前方` | 編輯後的前視圖影像。 | IMAGE |
| `左側` | 編輯後的左視圖影像。 | IMAGE |
| `後方` | 編輯後的後視圖影像。 | IMAGE |
| `右側` | 編輯後的右視圖影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db8b0a3ffe4332fcbcaac4da0d7b07217d01d2f05526750540f6036293e013ab`
