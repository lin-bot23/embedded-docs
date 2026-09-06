# 預覽點雲

Preview Point Cloud 節點可讓您在 ComfyUI 介面中檢視 3D 點雲檔案，而無需將其儲存至 ComfyUI 的輸出目錄。它會將點雲暫存到暫存位置，並在 3D 預覽視窗中顯示，同時將模型資料、模型資訊、相機資訊及預覽尺寸傳遞出去以供後續處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 點雲檔案（.ply） | FILE3D | 是 | - |
| `model_3d_info` | 關於 3D 模型的資訊 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 3D 視埠的目前狀態 | LOAD3D | 是 | - |
| `camera_info` | 用於 3D 檢視的相機資訊 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽視窗的寬度（預設：1024） | INT | 是 | 1 至 4096 |
| `height` | 預覽視窗的高度（預設：1024） | INT | 是 | 1 至 4096 |

注意：`model_3d_info` 和 `camera_info` 是可選的進階輸入。當它們未連接時，節點會使用 `viewport_state` 中儲存的對應值。點雲檔案會寫入 ComfyUI 的暫存目錄，而非輸出目錄。這是一個輸出（終端）節點，因此主要用於在介面中顯示預覽。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 點雲模型資料 | FILE3D |
| `model_3d_info` | 關於 3D 模型的資訊 | LOAD3DMODELINFO |
| `camera_info` | 用於 3D 檢視的相機資訊 | LOAD3DCAMERA |
| `width` | 預覽視窗的寬度 | INT |
| `height` | 預覽視窗的高度 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a0b13d9d5658343a6a7c25408d5e5cd9249c92264b76aa448a6553b370f4d782`
