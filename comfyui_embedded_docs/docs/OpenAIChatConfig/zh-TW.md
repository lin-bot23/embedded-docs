# OpenAI ChatGPT 進階選項

# OpenAI ChatGPT 高級選項

OpenAI ChatGPT 高級選項節點允許您為 OpenAI Chat 節點設定額外的配置。此節點提供高級設定，用於控制模型生成回應的方式，包括截斷行為、輸出長度限制和自定義指令。

## 概述

OpenAI ChatGPT 高級選項節點設計用於提升 OpenAI Chat 節點的功能，讓使用者可以指定高級配置選項。這些設定可以幫助調整模型的回應生成以符合特定需求。

## 輸入

| 參數名 | 描述 | 資料類型 | 是否必填 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `truncation` | 使用於模型回應的截斷策略。auto：如果此回應及其之前的回應的上下文超過模型的上下文視窗大小，模型將通過丟棄對話中間的輸入項目來截斷回應，以適應上下文視窗。disabled：如果模型回應將超過模型的上下文視窗大小，請求將會失敗並返回 400 錯誤（默認："auto"） | STRING | 是 | "auto"<br>"disabled" |
| `max_output_tokens` | 設定回應可以生成的代碼數量的上限，包括可見輸出代碼和推理代碼（默認：4096） | INT | 否 | 16 到 16384 |
| `instructions` | 指示模型如何生成回應的指令（支援多行輸入） | STRING | 否 | - |
| `reasoning_effort` | 模型在回答之前推理的程度。'default' 將選擇權留給模型。支援的等級因模型而異：GPT-6 Astra low-max、GPT-5.6 none-max（沒有最小值）、GPT-5.5 none-xhigh、GPT-5.5 Pro medium-xhigh、GPT-5 minimal-high、o-series low-high；GPT-4.1 沒有推理。不支援的等級在請求發送之前將被拒絕（默認："default"） | STRING | 否 | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | 包含指定設定以供 OpenAI Chat 節點使用的配置物件 | OPENAI_CHAT_CONFIG |

## 記錄

- `max_output_tokens` 參數設定總代碼數量的上限，包括可見輸出代碼和推理代碼。
- `reasoning_effort` 參數允許您指定模型在生成回應之前應該進行的推理等級。支援的等級根據所使用的模型而有所不同。
- `instructions` 參數可用於向模型提供詳細指令，以引導回應生成過程。
- `truncation` 參數決定模型是否應自動截斷超過上下文視窗大小的回應，或返回 400 錯誤。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/zh-TW.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
