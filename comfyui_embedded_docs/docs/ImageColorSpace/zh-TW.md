# Convert Image Color Space

## 概述

ImageColorSpace 節點將圖像在不同的顏色空間之間進行轉換，包括 sRGB、HDR（Rec.2020 HLG）和 HDR PQ（Rec.2020 PQ）。它支持在批次中縮窄過度亮度並壓縮超出顏色範圍的顏色，僅在 RGB 通道上運作，alpha 通道則保持不變。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要轉換的輸入圖像。 | IMAGE | 是 | 任何有效的圖像格式。 |
| `source` | 輸入像素的顏色空間。 | COMBO | 是 | <br> "sRGB" <br> "HDR" <br> "HDR PQ" |
| `destination` | 輸出像素的顏色空間。 | COMBO | 是 | <br> "sRGB" <br> "HDR" <br> "HDR PQ" |

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 在指定輸出顏色空間中的轉換後圖像。 | IMAGE |

## 註釋

- 此節點使用 203-nit SDR 白色和 1000-nit HLG 參考顯示器進行轉換。
- 轉換是在 float32 上計算的，並返回中間設備和數據類型。
- 直接 alpha 不會進行顏色轉換。
- 此節點支持 sRGB、HDR（Rec.2020 HLG）和 HDR PQ（Rec.2020 PQ）顏色空間之間的轉換。
- 此節點進行縮窄調色映射並壓縮超出顏色範圍的顏色，以確保轉換的準確性。
- 轉換僅使用 RGB 通道，alpha 通道（如果存在）則保持不變。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f0d38c6f5b524752a99d51b1a87f0e65c07f3ba36ecb0066d8d10c5b5032d36f`
