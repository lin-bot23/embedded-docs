# LTXVAddLatentGuide

## 概述

LTXV 添加潛在導引節點將已編碼的潛在量作為導引，允許使用來自早期階段的導引而不是圖像。此節點避免 VAE 解碼/編碼迴圈，並能將空間較小的導引擴散到稀疏網格上，以覆蓋目標畫布。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 正向條件輸入。 | CONDITIONING | 是 | N/A |
| `negative` | 負向條件輸入。 | CONDITIONING | 是 | N/A |
| `vae` | 要使用的 VAE 模型。 | MODEL | 是 | N/A |
| `latent` | 導引所釘定的目標影片潛在量。 | LATENT | 是 | N/A |
| `guiding_latent` | 導引潛在量。其空間大小必須在兩個軸向上都能被目標的大小整除相同的整數；等大小釘定保持原狀，半大小作為 x2 IC-LoRA 參考處理。 | LATENT | 是 | N/A |
| `latent_idx` | 導引開始的潛在框架索引，以潛在框架計數，而不是像素框架。負值將導引放置在潛在開始之前的框架上，不從其結束處反向計數。 | INT | 是 | -9999 到 9999 |
| `strength` | 限制在 1.0。擴散導引使用負去噪掩罩標記其填充位置，以便模型將其丟棄；大於 1.0 的值將使保留位置變為負值，整個導引將被丟棄。使用 attention_mask 來放大超過 1.0 的值。 | FLOAT | 是 | 0.0 到 1.0，步長 0.01 |
| `attention_mask` | 可選的像素空間空間掩罩。通過自注意力控制每個區域的條件影響，乘以強度。 | MASK | 否 | N/A |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 正向條件輸出。 | CONDITIONING |
| `negative` | 負向條件輸出。 | CONDITIONING |
| `latent` | 應用導引的潛在輸出。 | LATENT |

## 記錄

- `guiding_latent` 的空間大小必須在兩個軸向上都能被 `latent` 的大小整除相同的整數。
- `latent_idx` 參數允許在潛在框架內精確放置導引。
- `strength` 參數控制導引的強度，值大於 1.0 需要使用 `attention_mask` 以避免負位置。
- `attention_mask` 參數是可選的，但可以用來精調導引在圖像特定區域的影響。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/zh-TW.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
