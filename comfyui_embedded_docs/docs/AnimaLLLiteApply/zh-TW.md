# 套用 Anima LLLite

AnimaLLLiteApply 將輕量級的動畫修補程式套用到擴散模型上，實現可控的影像到影像生成，並可調整強度與時間。它會將預先配置的模型修補程式與輸入影像及選用的遮罩整合，透過修改模型的注意力層與 MLP 層來影響生成過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用修補程式的基本擴散模型 | MODEL | 是 | |
| `model_patch` | 要套用的預先配置動畫修補程式 | MODEL_PATCH | 是 | |
| `image` | 用於引導生成的參考影像。僅使用前 3 個色彩通道 (RGB) | IMAGE | 是 | |
| `strength` | 修補程式的效果強度（預設值：1.0） | FLOAT | 是 | -10.0 至 10.0 |
| `start_percent` | 修補程式開始生效時的去噪流程百分比（預設值：0.0） | FLOAT | 是 | 0.0 至 1.0 |
| `end_percent` | 修補程式停止生效時的去噪流程百分比（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 |
| `mask` | 選用遮罩，用於將修補程式效果限制在影像的特定區域 | MASK | 否 | |

**參數約束說明：** 若 `model_patch` 具有 4 個輸入通道，且未提供 `mask`，系統會自動建立一個零遮罩以符合影像尺寸。若 `model_patch` 沒有 4 個輸入通道，`mask` 參數會被忽略並設定為 `None`。此節點在 ComfyUI 中標記為實驗性。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 套用動畫修補程式後的擴散模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `48e455b767509a5a8c329365d5ffded86d6f4545d575c9fdc5ffbaf4da7c2287`
