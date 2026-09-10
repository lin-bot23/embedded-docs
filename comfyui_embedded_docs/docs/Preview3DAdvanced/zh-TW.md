# 3D 預覽（進階）

此節點會在 UI 中顯示 3D 模型預覽，而不會將檔案儲存到 ComfyUI 的輸出目錄。它會將模型儲存到暫存檔，並將模型資料、模型資訊、相機資訊及預覽尺寸傳遞給下游節點，以利後續處理。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 來自上游 3D 節點的 3D 模型檔案。 | FILE3D | 是 | GLB、GLTF、FBX、OBJ、STL、USDZ 或任何支援的 3D 格式 |
| `model_3d_info` | 每個模型在場景中的放置：位置、旋轉與縮放（Y 軸朝上的世界空間）。可選。進階選項。 | LOAD3DMODELINFO | 否 | - |
| `viewport_state` | 目前的視口狀態，包含相機與模型資訊。 | LOAD3D | 是 | - |
| `camera_info` | 視口相機資訊：位置、注視目標、縮放與類型。可選。進階選項。 | LOAD3DCAMERA | 否 | - |
| `寬度` | 視口的渲染寬度（像素）。預設值：1024。 | INT | 是 | 1 到 4096 |
| `高度` | 視口的渲染高度（像素）。預設值：1024。 | INT | 是 | 1 到 4096 |

注意：當未連接 `camera_info` 或 `model_3d_info` 時，若有可用的 `viewport_state`，其值會從 `viewport_state` 取得。若 `viewport_state` 中不含相機資訊，則 `camera_info` 為 None。若 `viewport_state` 中不含模型資訊，則 `model_3d_info` 預設為空列表。若 `viewport_state` 不是字典，則將其視為空值。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 來自上游 3D 節點的 3D 模型檔案（glb/obj/stl 等），原樣傳遞。 | FILE3D |
| `camera_info` | 每個模型在場景中的放置：位置、旋轉與縮放（Y 軸朝上的世界空間）。使用輸入值；若無輸入值，則回退至 `viewport_state` 中儲存的值。 | LOAD3DMODELINFO |
| `model_3d_info` | 視口相機資訊：位置、注視目標、縮放與類型。使用輸入值；若無輸入值，則回退至 `viewport_state` 中儲存的值。 | LOAD3DCAMERA |
| `寬度` | 視口的渲染寬度（像素）。 | INT |
| `高度` | 視口的渲染高度（像素）。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f2d3d35ed35fe68edebcde8fd8421d26850b04e3ae5b7147f1020c8ed904c480`
