# 模型注意力後端

## 概述

ModelAttentionBackend 節點允許您為模型選擇一種稠密注意力實現。它將選定的注意力後端補丁到模型上，當可用時，可以是 PyTorch 注意力或 Comfy Kitchen 注意力。此節點在稀疏注意力無法使用或不支持時尤其有用，確保模型使用指定的稠密注意力機制運作。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 將使用選定的注意力後端補丁的模型。 | MODEL | 是 |  |
| `attention` | 將應用到模型的稠密注意力後端。可用的選項是 "pytorch attention" 和 "comfy kitchen attention"，如果後者環境中可用。 | STRING | 是 | "pytorch attention"<br> "comfy kitchen attention" (當可用) |

- "comfy kitchen attention" 選項使用量化的 INT8 注意力，並僅在 Nvidia 和 AMD GPU 上受支持。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型` | 應用選定注意力後端後的輸入模型。 | MODEL |

## 注意事項

- 如果選定的注意力後端不可用，節點將自動回退到使用 PyTorch 注意力並記錄警告。
- ModelAttentionBackend 節點為實驗性質，可能會在未來版本中發生變化。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
