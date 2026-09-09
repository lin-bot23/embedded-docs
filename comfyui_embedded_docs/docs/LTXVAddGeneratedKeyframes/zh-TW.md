# LTXVAddGeneratedKeyframes

```markdown
# LTXV 添加生成的關鍵幀

## 概述

LTXV 添加生成的關鍵幀節點將詳細關鍵幀附加到視頻潛在變數上。每個關鍵幀代表一個潛在的像素幀的 token，這些 token 會與視頻進行去噪，但不屬於解碼輸出的部分。位置由 interval_frames 參數決定，該參數指定了像素幀步進以進行自動放置。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 關鍵幀附加到的正向條件。 | CONDITIONING | 是 | N/A |
| `negative` | 關鍵幀附加到的負向條件。 | CONDITIONING | 是 | N/A |
| `vae` | 只用於讀取潛在尺度因子。 | VAE | 是 | N/A |
| `latent` | 普通的五維視頻潛在變數，用於與之一起生成關鍵幀。在合併 AV 潛在變數之前添加它們。 | LATENT | 是 | N/A |
| `interval_frames` | 像素幀步進以進行自動放置。默認值 24 約為每秒一個關鍵幀，在 24 fps 下。佔用的像素會被跳過。當 frame_indices 設定時，將忽略。 | INT | 否 | 1-1024 |
| `keyframes` | 可選內容，用於初始化新關鍵幀。從早期的分離（相同的空間大小）或普通視頻潛在變數連接關鍵幀，以在每個新槽位中複製最近的幀（例如，在時空上掃後）。這些仍然會去噪，不會作為參考。在關鍵幀潛在變數上記錄的索引將被忽略，除非 frame_indices 設定。只有當樣本採樣開始於 sigma 1 以下時才有效。 | LATENT | 否 | N/A |
| `frame_indices` | 可選的像素幀索引。留空以從 interval_frames 在當前畫布上放置。當設定時，此列表是放置位置（連接的關鍵幀將按順序匹配）。最後一幀是允許的；第 0 幀不是（它已經是一個獨立的 token）。 | STRING | 否 | N/A |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 附加了生成關鍵幀注意力的正向條件。 | CONDITIONING |
| `negative` | 附加了生成關鍵幀注意力的負向條件。 | CONDITIONING |
| `latent` | 在 T 上附加了生成關鍵幀的視頻潛在變數。 | LATENT |

## 註釋

- `interval_frames` 參數決定了視頻中關鍵幀的間隔。較高的值會導致關鍵幀更少，並降低幀率。
- `keyframes` 輸入允許您使用現有的關鍵幀或視頻潛在變數初始化新關鍵幀。如果提供，這些關鍵幀將會去噪並附加到視頻潛在變數上。
- `frame_indices` 參數允許您指定關鍵幀應該放置的確切像素幀索引。如果提供，將忽略 `interval_frames` 參數。
- `positive` 和 `negative` 輸出包含附加了生成關鍵幀注意力的條件，可以用於進一步處理或分析。
- `latent` 輸出包含附加了生成關鍵幀的視頻潛在變數，可以用於進一步處理或分析。
```

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/zh-TW.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
