# LTXV 上下文視窗

此節點用於在取樣期間為類似 LTXV 的模型設定上下文視窗。它將影片生成過程劃分為多個重疊視窗，以管理記憶體使用並提升時間一致性。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 在取樣期間要套用上下文視窗的模型。 | MODEL | 是 | - |
| `context_length` | 以真實幀為單位的上下文視窗長度。必須為 8*n + 1。（預設：145） | INT | 是 | 最小值：1<br>最大值：nodes.MAX_RESOLUTION<br>步長：8 |
| `context_overlap` | 以真實幀為單位的上下文視窗重疊。（預設：40） | INT | 是 | 最小值：0<br>步長：8 |
| `context_schedule` | 隨取樣步驟而變化的上下文視窗排程演算法。（預設：UNIFORM_STANDARD） | COMBO | 是 | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | 上下文視窗的步幅；僅適用於均勻排程。（預設：1） | INT | 否 | 最小值：1 |
| `closed_loop` | 是否閉合上下文視窗的迴圈；僅適用於迴圈式排程。（預設：False） | BOOLEAN | 否 | True<br>False |
| `fuse_method` | 用於融合上下文視窗的方法。（預設：PYRAMID） | COMBO | 是 | 選項來自 comfy.context_windows.ContextFuseMethods.LIST_STATIC |
| `freenoise` | 是否套用 FreeNoise 雜訊重排，以改善視窗混合。（預設：True） | BOOLEAN | 否 | True<br>False |
| `retain_first_frame` | 在每個上下文視窗中保留第一個潛在幀（可能有助於保留初始參考）。（預設：False） | BOOLEAN | 否 | True<br>False |
| `split_conds_to_windows` | 是否根據區域索引將多個條件（由 ConditionCombine 建立）拆分到每個視窗。（預設：False） | BOOLEAN | 否 | True<br>False |

**注意：** `context_length` 參數必須遵循公式 8*n + 1，其中 n 為正整數。節點會自動透過將真實幀轉換為潛在幀來調整數值，以符合此要求。`context_overlap` 也會從真實幀轉換為潛在幀（除以 8）。

## 輸出

| 輸出名 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `MODEL` | 已套用上下文視窗以供取樣使用的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/zh-TW.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`
