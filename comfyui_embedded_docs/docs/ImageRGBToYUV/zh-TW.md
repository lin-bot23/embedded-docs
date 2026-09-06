# RGB 轉 YUV

# 圖像 RGB 至 YUV 轉換

ImageRGBToYUV 節點進行從 RGB 至 YUV 的顏色空間轉換。它接受一個 RGB 圖像作為輸入，並輸出三個分開的圖像，分別代表 YUV 頻道：Y（亮度）、U（藍色差異）和 V（紅色差異）。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|------|------|----------|------|-------|
| `影像` | 要轉換至 YUV 顏色空間的輸入 RGB 圖像。這應該是一個 3 個頻道的圖像。 | IMAGE | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|----------|------|-----------|
| `Y`      | Y 頻道代表圖像的亮度（亮度）。 | IMAGE |
| `U`      | U 頻道代表藍色差異色度組分。 | IMAGE |
| `V`      | V 頻道代表紅色差異色度組分。 | IMAGE |

輸出圖像將與輸入圖像具有相同的尺寸。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
