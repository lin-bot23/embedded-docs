# YUV 轉 RGB

ImageYUVToRGB 節點將 YUV 色彩空間的影像轉換為 RGB 色彩空間。它接受三個分別代表 Y（亮度）、U（藍色投影）和 V（紅色投影）分量的獨立輸入影像，並將它們組合成單張 RGB 影像。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | Range |
| --- | --- | --- | --- | --- |
| `Y` | Y（亮度）分量輸入影像 | IMAGE | 是 | - |
| `U` | U（藍色投影）分量輸入影像 | IMAGE | 是 | - |
| `V` | V（紅色投影）分量輸入影像 | IMAGE | 是 | - |

**注意：** 三個輸入影像（Y、U 和 V）必須同時提供，且尺寸應相容，才能正確進行轉換。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 轉換後的 RGB 影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/zh-TW.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
