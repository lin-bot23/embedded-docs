# YUV 轉 RGB

# 圖像 YUV 轉 RGB

ImageYUVToRGB 節點設計用於將圖像從 YUV 颜色空間轉換為 RGB 颜色空間。它通過取三個分離的輸入圖像來完成這項工作，這些圖像分別代表圖像的 Y（亮度）、U（藍色投影）和 V（紅色投影）通道。然後，這些通道使用顏色空間轉換技術合併成單一個 RGB 圖像。

## 概述

ImageYUVToRGB 節點通過合併 Y、U 和 V 通道將 YUV 圖像轉換為 RGB 圖像。這對於需要在這兩種標準之間進行顏色空間轉換的應用程序非常有用。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|------|------|----------|------|------|
| `Y`  | Y 通道輸入圖像，代表亮度信息。 | IMAGE | 是 | - |
| `U`  | U 通道輸入圖像，代表藍色色差。 | IMAGE | 是 | - |
| `V`  | V 通道輸入圖像，代表紅色色差。 | IMAGE | 是 | - |

**注意：** Y、U 和 V 通道必須一起提供，並應具有相同的尺寸，以確保正確的轉換。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|----------|------|-----------|
| `output` | YUV 到 RGB 轉換後的結果 RGB 圖像。 | IMAGE |

輸出圖像將具有與輸入的 Y、U 和 V 圖像相同的尺寸，但將顏色信息表示在 RGB 颜色空間中。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/zh-TW.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
