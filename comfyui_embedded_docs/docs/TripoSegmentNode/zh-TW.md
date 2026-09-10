# Tripo：分割模型

此節點會將 3D 模型分割成個別部件。它會將模型傳送至 Tripo 分割服務，等待作業完成，並以 GLB 格式回傳分割後的模型，以及以逗號分隔的部件名稱清單。這些部件名稱會饋入下游步驟，例如 Tripo: Complete Mesh Parts、Tripo: Retopology 和 Tripo: Convert model。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 要分割成部件的 3D 模型任務 ID。 | MODEL_TASK_ID | 是 | N/A |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 分割後 GLB 模型的輸出檔案名稱，格式為 `<task_id>.glb`。僅為向後相容性而保留。 | STRING |
| `segment task_id` | 產生此結果的分割作業任務 ID。 | SEGMENT_TASK_ID |
| `GLB` | 分割後的 3D 模型，以 GLB 檔案表示。 | GLB |
| `part_names` | 以逗號分隔的部件名稱。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`
