# Tripo：補全網格部件

補全分段 3D 模型的各個部件，並修復網格中缺失或損壞的區域。此節點會接收 Tripo 網格分割結果的任務 ID，向 Tripo 請求補全作業，並等待作業完成。你可以選擇將作業限制在特定部件名稱。補全後的模型會以 GLB 檔案形式回傳。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `segment_task_id` | Tripo 網格分割任務的任務 ID。此任務所產生分割模型的各部件會被補全。連接前一個 Tripo 網格分割節點的 SEGMENT_TASK_ID 輸出。 | SEGMENT_TASK_ID | 是 | Single task ID |
| `part_names` | 要補全的部件名稱，以逗號分隔。留空會補全所有部件。預設值：空字串。名稱前後多餘的空格會被移除，重複的名稱會被忽略。 | STRING | 否 | Free text or empty |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 補全後模型的檔案名稱。此外輸出僅為向後相容性而存在。 | STRING |
| `模型 task_id` | 補全後的 Tripo 網格補全任務的任務 ID。可供其他需要模型任務 ID 的 Tripo 節點作為輸入使用。 | MODEL_TASK_ID |
| `GLB` | 已修復各部件後的補全 3D 模型，會下載為 GLB 檔案。 | GLB |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c5709231fa2e33e6f3c9b25669acca1d4ae9adb882b90210d703aeddc0d11ecc`
