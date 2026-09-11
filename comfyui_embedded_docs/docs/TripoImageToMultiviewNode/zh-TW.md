# Tripo：影像轉多視角

使用 Tripo API 從單一輸入影像產生主體的正面、左側、背面與右側視圖。系統會上傳影像、啟動多視圖生成任務並持續輪詢直到完成，然後將四個產生的視圖連同任務 ID 一併回傳。此為付費任務，費用約為 0.10 美元。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 主體的來源影像，Tripo 會據此產生正面、左側、背面與右側視圖。即使提供批次影像，請求也只會使用單一張影像。 | IMAGE | 是 | 單一影像 |

注意：此節點會呼叫 Tripo 的雲端 API，並等待生成任務完成。典型任務約需 25 秒。身分驗證會透過節點的隱藏輸入自動處理，因此工作流程中不需要提供 Tripo API 金鑰。此節點要求 Tripo 回應中包含全部四個視圖 URL（`front_view_url`、`left_view_url`、`back_view_url`、`right_view_url`）；若有任何視圖缺失，執行會失敗並發生錯誤。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `多視角 task_id` | Tripo 針對多視圖影像生成請求所傳回的任務識別碼。可用於參照已完成的任務，例如使用 Tripo: Edit Multiview 精修這些視圖時。 | MULTIVIEW_TASK_ID |
| `前方` | 所產生主體的正面視圖。 | IMAGE |
| `左側` | 所產生主體的左側視圖。 | IMAGE |
| `後方` | 所產生主體的背面視圖。 | IMAGE |
| `右側` | 所產生主體的右側視圖。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`
