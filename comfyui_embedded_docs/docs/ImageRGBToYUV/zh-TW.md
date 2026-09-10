# RGB 轉 YUV

ImageRGBToYUV 節點將 RGB 影像轉換為 YUV 色彩空間。它會將影像拆分為三個分量 — Y（亮度）、U（藍色色差色度）和 V（紅色色差色度）— 並將每個分量作為與輸入影像相同尺寸的獨立影像回傳。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 要轉換為 YUV 的輸入 RGB 影像。如果影像包含 alpha 通道，則只會使用前三個 (RGB) 通道。 | IMAGE | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `Y` | YUV 色彩空間的亮度（明度）分量 | IMAGE |
| `U` | YUV 色彩空間的藍色色差色度分量 | IMAGE |
| `V` | YUV 色彩空間的紅色色差色度分量 | IMAGE |

每個輸出與輸入影像具有相同的寬度、高度和通道數量。對應的 Y、U 或 V 分量會重複到所有通道中，因此每個輸出都以標準影像形式回傳。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
