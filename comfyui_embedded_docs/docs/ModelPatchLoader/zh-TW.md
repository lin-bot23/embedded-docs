# 模型修補載入器

ModelPatchLoader 節點會從 `model_patches` 資料夾載入模型修補檔案，並將其準備好用於工作流程中。它會自動偵測檔案中包含的修補類型、建立相符的架構、載入已儲存的權重，並將所有內容包裝成模型修補器（ModelPatcher），以便套用到其他模型。它支援多種特殊修補格式，包括額外的 ControlNet 分支、特徵嵌入模型、適配器及類似模組。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `名稱` | 要從 model_patches 目錄載入的模型修補檔檔名。請從清單中選取其中一個可用的修補檔案。 | COMBO | 是 | 動態產生自 model_patches 資料夾中所有模型修補檔案的清單 |

注意：此節點標記為實驗性質。修補類型會從檔案內容自動偵測，因此無需手動選擇類型。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL_PATCH` | 載入的模型修補已包裝在 ModelPatcher 中，可套用至工作流程中的模型 | MODEL_PATCH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `069f40b1f108ecd74fc58c12aa2f74edff07f743aa1ed6352ff7bcf0c39341d4`
