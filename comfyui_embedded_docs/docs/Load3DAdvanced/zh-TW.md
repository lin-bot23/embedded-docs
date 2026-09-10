# 載入 3D（進階）

Load 3D (Advanced) 節點可從 ComfyUI 的 `input/3d` 目錄載入 3D 模型檔案，並提供模型資料，以及在 3D 檢視器視埠狀態中所捕捉到的模型放置與相機資訊。此節點支援常見的 3D 檔案格式，並可讓您設定視埠的渲染寬度與高度（以像素為單位）。此節點為實驗性功能。

## 輸入

| 參數 | 說明 | 資料型態 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_file` | 要載入的 3D 模型檔案。選取「none」以略過載入模型檔案。 | COMBO | 是 | `"none"`<br>在 `input/3d` 目錄中可用的 3D 模型檔案 |
| `viewport_state` | 目前的視埠狀態，包含來自 3D 檢視器的相機與模型資訊。 | LOAD3D | 是 | - |
| `width` | 以像素為單位的視埠渲染寬度（預設：1024）。 | INT | 是 | 最小值：1<br>最大值：4096<br>預設值：1024<br>步長：1 |
| `height` | 以像素為單位的視埠渲染高度（預設：1024）。 | INT | 是 | 最小值：1<br>最大值：4096<br>預設值：1024<br>步長：1 |

**參數附註：**
- `model_file` 參數只會列出具有下列副檔名的檔案：.gltf、.glb、.obj、.fbx、.stl
- 檔案必須放在 ComfyUI 安裝的 `input/3d` 目錄中；也會搜尋子資料夾，並會顯示相對於輸入目錄的檔案路徑
- 如果 `model_file` 為「none」，則不會載入任何模型資料，且 `model_3d` 輸出將為空
- 如果 `model_file` 設定為不存在的檔案，節點會傳回驗證錯誤："Invalid 3D model file: {model_file}"

## 輸出

| 輸出名 | 說明 | 資料型態 |
|-------------|-------------|-----------|
| `model_3d` | 已載入的 3D 模型檔案（glb/obj/stl 等）。如果未選取任何模型檔案，則為空。 | FILE3DANY |
| `model_3d_info` | 場景中每個模型的放置資訊：位置、旋轉與縮放（Y 軸向上的世界空間）。 | LOAD3DMODELINFO |
| `camera_info` | 視埠相機資訊：位置、注視目標、縮放與類型。 | LOAD3DCAMERA |
| `width` | 以像素為單位的視埠渲染寬度。 | INT |
| `height` | 以像素為單位的視埠渲染高度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c79c53dde0c8b3afb7df7b972df749f5040c92d48b47e355c4497d9b0cbf1c22`
