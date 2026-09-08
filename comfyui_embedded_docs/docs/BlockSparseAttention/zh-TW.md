# Block Sparse Attention

## 概述

Block Sparse Attention 節點將塊稀疏注意力機制應用於 ComfyUI 模型，透過允許每個查詢塊只對選定的關鍵塊進行精確的注意力，從而減少注意力計算。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 將塊稀疏注意力應用於的 ComfyUI 模型。 | MODEL | 是 | N/A |
| `selection` | 選擇要參與注意力的關鍵塊的選擇方法。 | DYNAMIC_COMBO | 是 | 選項：Sol-Attn (自適應 tau), top-k (SLA), VSA (FastVideo) |
| `tau` | Sol-Attn (自適應 tau) 選擇中，分數分佈 sigmas 的閾值。 | FLOAT | 否 | 默認：1.3，最小：0.0，最大：4.0，步進：0.05 |
| `keep_percent` | top-k (SLA) 選擇中，每個查詢塊精確保持的關鍵塊的百分比。 | FLOAT | 否 | 默認：10.0，最小：0.5，最大：95.0，步進：0.5 |
| `start_percent` | 模型在計劃中使用稠密注意力的時間百分比。 | FLOAT | 否 | 默認：0.2，最小：0.0，最大：1.0，步進：0.01 |
| `end_percent` | 模型在計劃中使用稠密注意力的時間百分比。 | FLOAT | 否 | 默認：1.0，最小：0.0，最大：1.0，步進：0.01 |
| `dense_blocks` | 表示總是運行稠密注意力的 Transformer 塊的字符串。 | STRING | 否 | 默認："" |
| `min_tokens` | 模型使用稠密注意力的序列中最小 token 數量。 | INT | 否 | 默認：12288，最小：0，最大：1 << 20，步進：512 |
| `extra_tokens` | 每個查詢塊在其選定的塊之外，參與的額外最高分 token 數量。 | INT | 否 | 默認：256，最小：0，最大：256，步進：64 |
| `sink_conditioning` | 用於 sink condition 的 MiniMax-H3 condition rows。 | COMBO | 否 | 選項：exact_kv, exact_kv_and_rows, off |
| `verbose` | 是否啟用詳細記錄。 | BOOLEAN | 否 | 默認：False |

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 應用塊稀疏注意力後的 ComfyUI 模型。 | MODEL |

### 註釋

- `selection` 參數決定了如何選擇關鍵塊。選項包括：
  - Sol-Attn (自適應 tau)：每個查詢塊基於自適應閾值參與選定的關鍵塊子集。
  - top-k (SLA)：每個查詢塊精確保持固定百分比的關鍵塊。
  - VSA (FastVideo)：每個查詢塊精確保持固定百分比的視頻塊，使用 FastH3-VSA 的塊拼貼和粗略分支。
- `dense_blocks` 參數允許您指定總是運行稠密注意力的 Transformer 塊。
- `min_tokens` 參數設定了模型使用稠密注意力的序列中 token 的最小數量。
- `extra_tokens` 參數允許您指定每個查詢塊在其選定的塊之外，參與的額外最高分 token 數量。
- `sink_conditioning` 參數決定了用於 sink condition 的 MiniMax-H3 condition rows。
- `verbose` 參數啟用詳細記錄。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6a27aee45593883f5958ae1aac74a2077362742a0fdf74fc9dbfd68eddc6d259`
