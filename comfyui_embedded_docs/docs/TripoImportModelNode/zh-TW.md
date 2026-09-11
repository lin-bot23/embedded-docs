# Tripo：匯入模型

此節點將外部 3D 模型匯入 Tripo，以便 Tripo 後處理節點（例如 Texture、Rig 和 Convert）可以使用它。該節點會將檔案上傳至 Tripo，並傳回一個任務 ID，用於識別匯入的模型，供這些節點使用。建議使用 GLB，因為紋理僅在內嵌於檔案中時才會保留，而對匯入的模型進行紋理處理需要紋理提示詞。此節點可免費使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 要匯入的 3D 模型（GLB / FBX / OBJ / STL，最高 150 MB）。OBJ 和 STL 檔案不含內嵌紋理。 | FILE3D | 是 | GLB<br>FBX<br>OBJ<br>STL<br>任何 3D 格式 |

**注意：** 僅支援 GLB、FBX、OBJ 和 STL 格式。GLTF (.gltf) 無法匯入，因為它會參照外部檔案；請改為匯出單一檔案的 GLB。模型檔案必須為 150 MB 或更小。建議使用 GLB，因為紋理只有在內嵌於檔案中時才能在匯入後保留。OBJ 和 STL 檔案不含內嵌紋理。對匯入的模型進行紋理處理需要紋理提示詞。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model task_id` | 用於識別匯入模型的任務 ID，可搭配 Tripo 後處理節點使用 | MODEL_TASK_ID |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bf91e964c5705f7377868dd06bbf5d57b41cc3607fc377cd45886d3d6c5ceddc`
