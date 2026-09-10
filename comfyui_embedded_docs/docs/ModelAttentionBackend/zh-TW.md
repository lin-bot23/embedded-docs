# 模型注意力後端

此節點會為模型的注意力計算選取所需的密集注意力後端。它會複製指定的模型、套用所選後端，並回傳修補後的複本。與 Block Sparse Attention 搭配使用時，只要稀疏注意力未啟用或不受支援，就會使用此後端。若選取的後端無法使用，節點會自動改用 PyTorch attention。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要修補的模型。 | MODEL | 是 |  |
| `attention` | 要套用的密集注意力後端（預設值："pytorch attention"）。Comfy Kitchen attention 使用量化的 INT8 注意力，僅在 Nvidia 與 AMD GPU 上可用。若選取的後端無法使用，則會改用 PyTorch attention。 | COMBO | 是 | "pytorch attention"<br>"comfy kitchen attention" |

注意：僅在目前環境中可取得 Comfy Kitchen INT8 attention 模組時，才會顯示 "comfy kitchen attention" 選項。

## 輸出

| 輸出名 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `模型` | 已套用所選注意力後端的輸入模型複本。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
