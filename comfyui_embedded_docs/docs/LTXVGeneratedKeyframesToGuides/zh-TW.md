# LTXVGeneratedKeyframesToGuides

```markdown
# LTXV 生成關鍵幀至導向

## 概述

LTXV 生成關鍵幀至導向節點將早期階段的生成關鍵幀作為凍結圖像導向，固定在後續的畫布上。它將關鍵幀解碼為獨立幀，如果需要則調整大小，並使用 0 的噪聲掩罩寫入，以防止進一步去噪。記錄的索引會從生成它的畫布縮放到目標畫布，並可以覆蓋幀索引以明確設置位置。

## 輸入

| 參數名                 | 描述                                                                 | 資料類型 | 必需 | 范圍 |
|---------------------------|-----------------------------------------------------------------------------|-----------|----------|-------|
| `positive`                | 將關鍵幀固定為圖像導向的正向條件。                             | CONDITIONING | 是      |       |
| `negative`                | 將關鍵幀固定為圖像導向的負向條件。                             | CONDITIONING | 是      |       |
| `vae`                     | 用於解碼關鍵幀的 VAE 模型。                                   | MODEL      | 是      |       |
| `latent`                  | 要添加導向的目標視頻潛在值，例如，時空上掃描的版本。 | LATENT     | 是      |       |
| `keyframes`               | LTXV 分離生成關鍵幀的關鍵幀輸出，其中包含每個關鍵幀生成的像素幀索引。 | LATENT     | 是      |       |
| `strength`                | 導向強度。1.0 是一個硬固定；較低的值會放鬆它。                   | FLOAT      | 是      | 0.0 - 10.0 |
| `override_frame_indices` | 選擇性 —— 在這些像素幀上固定，而不是使用記錄的（或自動縮放的）位置。每個關鍵幀提供一個索引。留空以重用記錄的位置，或在目標畫布長度不同時（例如，時空 x2 之後）縮放它們。 | STRING    | 否       |       |

## 輸出

| 輸出名 | 描述                                                                 | 資料類型 |
|-------------|-----------------------------------------------------------------------------|-----------|
| `positive`  | 將關鍵幀固定為圖像導向的正向條件。                             | CONDITIONING |
| `negative`  | 將關鍵幀固定為圖像導向的負向條件。                             | CONDITIONING |
| `latent`    | 添加關鍵幀作為凍結導向的目標視頻潛在值。                           | LATENT     |

## 註釋

- `strength` 參數控制關鍵幀作為導向的固定程度。1.0 創建一個硬固定，而較低的值會放鬆固定。
- `override_frame_indices` 參數允許您指定關鍵幀應該固定的確切像素幀。如果留空，節點將使用記錄的位置或根據需要縮放它們。
- 節點假設 `keyframes` 潛在值包含每個關鍵幀的像素幀索引。如果情況不是這樣，節點將引發 `ValueError`。
- 節點僅支持 1 個批大小。每個導向都從一個圖像編碼，所以它不能在批處理元素之間有所不同。
- 如果 `latent` 输入中的 `samples` 矩陣不是 5D 矩陣或批大小不是 1，節點將引發 `ValueError`。
- 如果 `keyframes` 输入中的 `samples` 矩陣不是 5D 矩陣或批大小不是 1，節點將引發 `ValueError`。
- 如果 `keyframes` 输入中的 `samples` 矩陣的形状在調整大小後與 `latent` 输入中的 `samples` 矩陣的形状不匹配，節點將引發 `ValueError`。
- 如果 `strength` 參數超出 0.0 到 10.0 的範圍，節點將引發 `ValueError`。
- 如果 `override_frame_indices` 參數不是逗號分隔的整數列表或索引數量與關鍵幀數量不匹配，節點將引發 `ValueError`。
- 如果 `override_frame_indices` 參數中的任何索引超出目標畫布中像素幀的範圍，節點將引發 `ValueError`。
- 如果 `override_frame_indices` 參數中的最大索引大於目標畫布中像素幀的數量，節點將引發 `ValueError`。
```

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
