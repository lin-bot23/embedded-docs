# 儲存 3D（進階）

Save3DAdvanced 會將 3D 模型儲存至 ComfyUI 輸出目錄中的檔案，並建立已儲存場景的預覽。同時，它會將 3D 模型、模型在場景中的擺放位置、相機資訊與視埠尺寸傳遞至下游節點。當未連接模型擺放位置或相機資訊時，此節點會使用視埠狀態中儲存的值。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 來自上游 3D 節點的 3D 模型檔案。 | FILE3D | 是 | GLB<br>GLTF<br>FBX<br>OBJ<br>STL<br>USDZ<br>Any |
| `filename_prefix` | 用於已儲存檔案名稱的前置詞（預設："3d/ComfyUI"）。 | STRING | 是 | Free text |
| `viewport_state` | 包含相機與模型擺放資訊的視埠狀態，通常來自 Load 3D 節點。 | LOAD3D | 是 | - |
| `model_3d_info` | 場景中每個模型的擺放資訊：位置、旋轉與縮放（Y 軸向上的世界空間）。連接時會覆寫儲存在 `viewport_state` 中的模型擺放資訊。 | LOAD3DMODELINFO | 否 | - |
| `camera_info` | 視埠相機資訊：位置、凝視目標、縮放與類型。連接時會覆寫儲存在 `viewport_state` 中的相機資訊。 | LOAD3DCAMERA | 否 | - |
| `width` | 視埠的渲染寬度（像素）（預設：1024）。 | INT | 是 | 1 to 4096 |
| `height` | 視埠的渲染高度（像素）（預設：1024）。 | INT | 是 | 1 to 4096 |

注意：`model_3d_info` 與 `camera_info` 為選用。當任一輸入未連接時，此節點會改用儲存在 `viewport_state` 中的對應值。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_3d` | 從輸入端傳遞而出的 3D 模型檔案。 | FILE3D |
| `model_3d_info` | 場景中每個模型的擺放資訊：位置、旋轉與縮放（Y 軸向上的世界空間）。 | LOAD3DMODELINFO |
| `camera_info` | 視埠相機資訊：位置、凝視目標、縮放與類型。 | LOAD3DCAMERA |
| `width` | 從輸入端傳遞而出的渲染寬度值。 | INT |
| `height` | 從輸入端傳遞而出的渲染高度值。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`
