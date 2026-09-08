# Pixal3DConditioning

```markdown
# Pixal3DConditioning

## 概述

Pixal3DConditioning 節點設計用於為 Trellis2 3D 生成流程準備圖像條件。它使用 DINOv3 圖像模型從輸入圖像中提取兩種解析度的視覺特徵。這些特徵然後被組織成每階段的特徵圖，並可選性地使用 NAF 模型進行強化。此節點還結合從水平視場角取得的相機數據來計算投影轉換矩陣。它輸出一個正條件對，包含從圖像中導出的特徵圖和投影數據，以及一個負條件對，具有置零的特徵張量，用於無分類器的導向。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | 用於特徵提取的 DINOv3 ViT-L/16 ClipVision 模型。 | CLIP_VISION | 是 | — |
| `圖像` | 從 ImageCropToMask 節點來的預處理圖像，用於 Pixal3D，並具有 pad_factor 為 1.1。 | IMAGE | 是 | — |
| `camera_angle_x` | 以度為單位的水平視場角。此參數可以連接到 MoGeGeometryToFOV 節點以獲得每張圖像的視場角。默認值：49.13。 | FLOAT | 是 | 1.0 – 170.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `正向` | 包含 Trellis2 生成所需的從圖像中導出的特徵圖和投影數據的正條件輸出。 | CONDITIONING |
| `負向` | 用於無分類器導向的具有置零特徵張量的負條件輸出。 | CONDITIONING |

注意：`camera_angle_x` 值在內部轉換為弧度並用於計算投影轉換矩陣的相機距離。當提供的視覺模型包含 NAF 成分時，此節點還會為形狀和紋理階段生產高解析度特徵圖。
```

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
