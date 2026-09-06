# LTXV 時長預測器

此節點使用透過 ModelPatchLoader 載入的 LTX 2.4 時長預測頭，針對文字提示預測自然的鏡頭時長，然後將結果對齊到 VAE 的 8k+1 幀網格。預測會使用所選幀率以及最小和最大時長限制，轉換為幀數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於預處理文字嵌入並執行時長預測頭的模型。 | MODEL | 是 | N/A |
| `positive` | 提供提示詞的文字嵌入與後設資料以進行時長預測的條件數據。 | CONDITIONING | 是 | N/A |
| `duration_head` | 透過 ModelPatchLoader 載入的 LTX 2.4 時長預測頭。必須是 LTX 時長預測頭。 | MODEL_PATCH | 是 | N/A |
| `frame_rate` | 用來將秒轉換為幀的幀率，單位為每秒幀數（預設：24.0）。 | FLOAT | 是 | 1.0 至 120.0 |
| `min_seconds` | 將預測轉換為幀數時使用的最小時長，單位為秒（預設：1.0）。 | FLOAT | 是 | 0.5 至 120.0 |
| `max_seconds` | 將預測轉換為幀數時使用的最大時長，單位為秒（預設：20.0）。 | FLOAT | 是 | 0.5 至 120.0 |

注意：`duration_head` 輸入必須是包含 LTX 時長預測頭的模型補丁。若所連接的模型補丁不是 LTX 時長預測頭，此節點會拋出 ValueError。僅使用第一個 conditioning 條目——如果 `positive` 包含多個提示的批次，此節點只評估第一個。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `num_frames` | 預測時長轉換成的幀數，並對齊到 VAE 的 8k+1 幀網格。 | INT |
| `seconds` | 原始（未限制）預測時長（以秒為單位）。這是對齊到幀網格之前的值。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a4abb43128b8fe396e4c986d75028aea6bfdd9bb6fda07e24c88f8e04a61669e`
