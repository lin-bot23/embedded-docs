# 預覽音訊

Preview Audio 節點可讓您直接在 ComfyUI 介面中聆聽音訊，而無需將其儲存至輸出目錄。它接收音訊資料作為輸入，驗證其存在，並在顯示臨時音訊播放器的同時將其傳遞，以便您能聽到結果。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 要預覽的音訊資料。如果輸入為 None，節點會引發 ValueError，這可能發生在來源影片沒有音訊軌道時。 | AUDIO | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `audio` | 未經修改地從輸入傳遞過來的音訊資料。 | AUDIO |
| `ui` | 在介面中顯示音訊播放器小工具以預覽音訊。 | UI |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`
