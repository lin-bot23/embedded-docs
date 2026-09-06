# 解析度選擇器

Resolution Selector 節點會依據所選的寬高比與目標總解析度（以百萬像素為單位）計算像素寬度和高度。此節點有助於為其他節點（例如 Empty Latent Image 節點）產生一致的尺寸。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `長寬比` | 輸出尺寸的寬高比（預設值：`"1:1 (Square)"`）。 | COMBO | 是 | `"1:1 (Square)"`<br>`"2:3 (Portrait Photo)"`<br>`"3:2 (Photo)"`<br>`"3:4 (Portrait Standard)"`<br>`"4:3 (Standard)"`<br>`"9:16 (Portrait Widescreen)"`<br>`"16:9 (Widescreen)"`<br>`"21:9 (Ultrawide)"` |
| `百萬像素` | 目標總百萬像素數。在正方形比例下，1.0 MP 約等於 1024x1024（預設值：1.0）。 | FLOAT | 是 | 0.1 - 16.0 (step: 0.1) |
| `預覽` | 計算後輸出解析度的即時預覽。此唯讀控制項會自動更新，不接受使用者輸入。 | RESOLUTION_PREVIEW | 否 | N/A |
| `倍數` | 要將所選解析度設定為此數值的最接近倍數（預設值：8）。 | INT | 否 | 8 - 128 (step: 4) |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `寬度` | 計算出的像素寬度，並取整至最接近所選倍數的值。 | INT |
| `高度` | 計算出的像素高度，並取整至最接近所選倍數的值。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dd4c7f977ed69a873a48da4b01c5c8f0b6563cfd743740235fc0ad5762579697`
