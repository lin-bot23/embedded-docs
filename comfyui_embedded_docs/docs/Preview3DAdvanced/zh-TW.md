# 3D 預覽（進階）

此節點在 UI 中顯示 3D 模型預覽，而不會將檔案儲存到 ComfyUI 輸出目錄。它會將模型儲存到暫時檔案，並向下游傳遞模型資料、模型資訊、相機資訊和預覽尺寸，以供進一步處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 來自上游 3D 節點的 3D 模型檔案。 | FILE3D | 是 | GLB、GLTF、FBX、OBJ、STL、USDZ 或任何支援的 3D 格式 |
| `model_3d_info` | 選用的模型資訊中繼資料。進階選項。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 目前的視埠狀態，包含相機與模型資訊。 | LOAD3D | 是 | - |
| `camera_info` | 3D 視圖的選用相機設定。進階選項。 | LOAD3DCAMERA | 否 | - |
| `寬度` | 預覽的寬度（像素）。預設值：1024。 | INT | 是 | 1 至 4096 |
| `高度` | 預覽的高度（像素）。預設值：1024。 | INT | 是 | 1 至 4096 |

注意：當 `camera_info` 或 `model_3d_info` 未連接時，其值將在可行時從 `viewport_state` 取得。若 `viewport_state` 不含相機資訊，則 `camera_info` 為 None。若 `viewport_state` 沒有模型資訊，則 `model_3d_info` 預設為空清單。若 `viewport_state` 不是字典，則將其視為空。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 從輸入傳遞的 3D 模型檔案。 | FILE3D |
| `camera_info` | 來自輸入或視埠狀態的模型資訊中繼資料。 | LOAD3DMODELINFO |
| `model_3d_info` | 來自輸入或視埠狀態的相機設定。 | LOAD3DCAMERA |
| `寬度` | 預覽的寬度（像素）。 | INT |
| `高度` | 預覽的高度（像素）。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `46c14d6242cbcabd457e13ae193427bb4c1fed55e81e568d50719fff0f1a95a0`
