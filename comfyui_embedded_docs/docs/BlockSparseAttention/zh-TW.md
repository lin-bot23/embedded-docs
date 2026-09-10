# 模型區塊稀疏注意力

## 概述

Block Sparse Attention 節點用於修改 ComfyUI 模型，以應用塊稀疏注意力機制。此機制透過允許每個查詢塊只關注鍵塊的子集，而不是關注所有可能的塊，從而減少計算負擔，對於長序列特別有益。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 將塊稀疏注意力應用到其上的 ComfyUI 模型。 | MODEL | 是 | N/A |
| `selection` | 用於確定要關注哪些鍵塊的方法。 | DYNAMIC_COMBO | 是 | 選項：sol-attn (自適應 tau), sla (top-k), vsa (Video Sparse Attention) |
| `tau` | sol-attn 方法中，分數分佈 sigmas 的閾值。 | FLOAT | 否 | 默認：1.3，最小：0.0，最大：4.0，步進：0.05 |
| `keep_percent` | sla 方法中，每個查詢塊精確保持的鍵塊百分比。 | FLOAT | 否 | 默認：10.0，最小：0.5，最大：95.0，步進：0.5 |
| `start_percent` | 稀疏注意力開始的百分比點。 | FLOAT | 否 | 默認：0.2，最小：0.0，最大：1.0，步進：0.01 |
| `end_percent` | 稀疏注意力結束的百分比點。 | FLOAT | 否 | 默認：1.0，最小：0.0，最大：1.0，步進：0.01 |
| `dense_blocks` | 表示總是運行密集注意力的 Transformer 塊的字符串。 | STRING | 否 | 默認："" |
| `min_tokens` | 模型使用密集注意力的序列中的最小 token 數量。 | INT | 否 | 默認：12288，最小：0，最大：1 << 20，步進：512 |
| `extra_tokens` | 每個查詢塊在其選定的塊之外關注的額外高分 token 數量。 | INT | 否 | 默認：256，最小：0，最大：256，步進：64 |
| `sink_conditioning` | 用於 sink condition 的 MiniMax-H3 condition rows。 | COMBO | 否 | 選項：exact_kv, exact_kv_and_rows, off |
| `verbose` | 啟用詳細記錄。 | BOOLEAN | 否 | 默認：False |

### 注意事項

- `selection` 參數允許您在選擇鍵塊的不同方法之間進行選擇：
  - `sol-attn`：使用自適應閾值，基於分數分佈選擇鍵塊。
  - `sla`：保持固定百分比的最高分鍵塊。
  - `vsa`：應用 Video Sparse Attention，該方法使用 3D 觀看立體體塊拼貼和學習的粗略注意力分支。
- `dense_blocks` 參數可用於指定應該總是使用密集注意力的 Transformer 塊。
- `min_tokens` 參數設定了使用密集注意力的序列中的最小 token 數量。
- `extra_tokens` 參數允許您指定每個查詢塊應該關注的額外高分 token 數量。
- `sink_conditioning` 參數僅與 MiniMax-H3 模型相關，並確定如何處理 condition rows。
- `verbose` 參數啟用詳細記錄，對於除錯可能很有用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型` | 應用塊稀疏注意力後的 ComfyUI 模型。 | MODEL |

### 續約和限制

- `sol-attn` 方法需要介於 0.0 和 4.0 之間的 `tau` 值。
- `sla` 方法需要介於 0.5 和 95.0 之間的 `keep_percent` 值。
- `vsa` 方法僅與 MiniMax-H3 模型兼容，並要求模型具有 `to_gate_compress` 層。
- `min_tokens` 參數必須是非負整數（設為 0 時所有注意力都保持稠密）。
- `extra_tokens` 參數必須是非負整數。
- `sink_conditioning` 選項僅適用於 MiniMax-H3 模型。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
