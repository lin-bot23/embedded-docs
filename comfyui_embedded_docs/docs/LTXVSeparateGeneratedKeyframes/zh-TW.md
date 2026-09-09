# LTXVSeparateGeneratedKeyframes

```markdown
# LTXV 分離生成的關鍵幀

## 概述

LTXV 分離生成的關鍵幀節點從採樣的潛在變數和條件中移除生成的關鍵幀，允許在空間上提升視頻潛在變數之前進行分離處理。它設計用於在空間上提升之前使用，並不應在 LTXV 剪裁導向後運行，因為它將生成的關鍵幀視為可棄導向並丟棄它們。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 移除生成的關鍵幀元數據的正向條件。 | CONDITIONING | 是 | N/A |
| `negative` | 移除生成的關鍵幀元數據的負向條件。 | CONDITIONING | 是 | N/A |
| `latent` | 移除生成的關鍵幀的視頻潛在變數。 | LATENT | 是 | N/A |
| `keyframes_to_batch` | 返回關鍵幀作為單一畫面潛在變數的批次。留空以獲得一個多畫面潛在變數，這是潛在提升器和稍後的添加生成的關鍵幀所期望的。 | BOOLEAN | 否 | 默認: False |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 移除生成的關鍵幀元數據的正向條件。 | CONDITIONING |
| `negative` | 移除生成的關鍵幀元數據的負向條件。 | CONDITIONING |
| `latent` | 移除生成的關鍵幀的視頻潛在變數。 | LATENT |
| `keyframes` | 被去除的關鍵幀，標籤為 generated_keyframe_indices 和 generated_keyframe_num_frames。將這些輸入到稍後的添加生成的關鍵幀以初始化新插槽，或到生成的關鍵幀到導向以將其固定為凍結圖像導向（如果画布長度改變，索引將重新映射）。 | LATENT |

## 記錄

- `keyframes_to_batch` 參數決定關鍵幀是返回為單一畫面潛在變數的批次還是返回為一個多畫面潛在變數。
- 節點確保在進行任何進一步處理之前，從條件和潛在變數中移除生成的關鍵幀。
- `keyframes` 輸出可以用於初始化生成關鍵幀的新插槽或將其固定為凍結圖像導向。
- 如果潛在變數不包含生成的關鍵幀或如果關鍵幀不匹配預期的格式，節點將引發 `ValueError`。
- 節點假設生成的關鍵幀是使用 LTXV 添加生成的關鍵幀節點添加的，並且與當前的潛在變數相兼容。
```

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/zh-TW.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
