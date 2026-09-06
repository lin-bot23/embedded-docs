# OpenAI Sora - 影片

OpenAIVideoSora2 節點使用 OpenAI 的 Sora 模型生成影片。它會根據文字提示與選用的輸入參考影像建立影片內容，然後將生成的影片作為輸出。此節點支援不同的影片長度與解析度，端視所選的模型而定。

**棄用通知：** OpenAI 將於 2026 年 9 月停止提供 Sora v2 API。屆時此節點將從 ComfyUI 中移除。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 OpenAI Sora 模型（預設："sora-2"） | COMBO | 是 | "sora-2"<br>"sora-2-pro" |
| `prompt` | 引導文字；若提供了輸入影像則可留空（預設：空白） | STRING | 是 | - |
| `size` | 生成影片的解析度（預設："1280x720"） | COMBO | 是 | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duration` | 生成影片的持續時間（秒）（預設：8） | COMBO | 是 | 4<br>8<br>12 |
| `image` | 選用的輸入參考影像，用於影片生成（穿搭、角色、場景參考等）；僅支援單一影像 | IMAGE | 否 | - |
| `seed` | 用於決定節點是否重新執行的種子；無論種子值為何，實際結果都是非確定性的（預設：0） | INT | 否 | 0 至 2147483647 |

**限制與注意事項：**

- "sora-2" 模型僅支援 "720x1280" 與 "1280x720" 解析度；"1024x1792" 與 "1792x1024" 選項僅適用於 "sora-2-pro" 模型
- 連接影像時，必須恰好包含一張影像；連接多張影像會觸發錯誤
- 無論種子值為何，結果都是非確定性的

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 由 OpenAI Sora 生成的影片檔案 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
