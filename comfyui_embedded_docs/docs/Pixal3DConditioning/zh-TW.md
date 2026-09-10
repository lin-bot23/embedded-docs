# Pixal3DConditioning

此節點為 Trellis2 3D 生成管線準備影像條件。它使用 DINOv3 視覺模型以兩種解析度從輸入影像中提取視覺特徵，將它們組織成每個階段的特徵圖（可選地使用 NAF 模型增強），並將它們與從水平視野推導出的攝影機資料結合。它輸出一對正向和負向條件，其中負向條件使用零化特徵進行無分類器引導。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision。 | CLIP_VISION | 是 | — |
| `圖像` | 來自 ImageCropToMask 的預處理影像（對於 Pixal3D，pad_factor=1.1）。 | IMAGE | 是 | — |
| `camera_angle_x` | 水平 FOV，以度為單位（顯示名稱：fov）。連接 MoGeGeometryToFOV（axis='horizontal', unit='degrees'）以獲得每張影像的 FoV（與上游預設值一致）。預設值：49.13。 | FLOAT | 是 | 1.0 – 170.0 |

注意：`camera_angle_x` 值在內部轉換為弧度，並用於計算投影變換矩陣的攝影機距離。當提供的視覺模型包含 NAF 元件時，節點還會為形狀和紋理階段產生高解析度特徵圖。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `正向` | 正向條件，包含從影像推導出的特徵圖和 Trellis2 生成的投影資料。 | CONDITIONING |
| `負向` | 負向條件，使用零化特徵張量，用於無分類器引導。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
