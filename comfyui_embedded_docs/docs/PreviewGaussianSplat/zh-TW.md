# 預覽 Splat

PreviewGaussianSplat 節點會在預覽視窗中顯示 3D 高斯潑濺（Gaussian Splat）檔案，而不會將其儲存到 ComfyUI 的輸出目錄。它接受各種高斯潑濺格式的 3D 模型檔案，儲存一份暫時副本以供預覽，並將模型資料傳遞給工作流程進行後續處理。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 高斯潑濺 3D 檔案。 | FILE3D | 是 | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | 關於 3D 模型的選用中繼資料資訊。若未連接，節點會使用來自 `viewport_state` 的模型資訊。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 3D 檢視區的目前狀態，包含相機與模型資訊。 | LOAD3D | 是 | - |
| `camera_info` | 用於預覽的選用相機資訊。若未連接，節點會使用來自 `viewport_state` 的相機資訊。 | LOAD3DCAMERA | 否 | - |
| `width` | 預覽渲染的寬度（像素）。（預設值：1024） | INT | 是 | 1 至 4096 |
| `height` | 預覽渲染的高度（像素）。（預設值：1024） | INT | 是 | 1 至 4096 |

注意：若未提供 `camera_info` 或 `model_3d_info`，節點會改用儲存在 `viewport_state` 中的相機與模型資訊。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `model_3d` | 輸入的 3D 高斯潑濺檔案，原封不動地傳遞出去。 | FILE3D |
| `model_3d_info` | 關於 3D 模型的中繼資料資訊，可來自輸入或衍生自檢視區狀態。 | LOAD3DMODELINFO |
| `camera_info` | 用於預覽的相機資訊，可來自輸入或衍生自檢視區狀態。 | LOAD3DCAMERA |
| `width` | 預覽渲染的寬度。 | INT |
| `height` | 預覽渲染的高度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`
