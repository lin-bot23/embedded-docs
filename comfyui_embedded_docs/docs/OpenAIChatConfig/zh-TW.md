# OpenAI ChatGPT 進階選項

**OpenAIChatConfig 節點可讓您定義進階選項，以控制 OpenAI Chat 節點產生回應的方式。您可以設定截斷策略、限制輸出 token 數量、提供自訂指示，以及選擇模型在回答前應進行多少推理。**

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `truncation` | 用於模型回應的截斷策略。auto：如果此回應及先前回應的上下文超過模型的上下文視窗大小，模型將透過捨棄對話中間的輸入項目來截斷回應，以符合上下文視窗。disabled：如果模型回應將超過模型的上下文視窗大小，請求將失敗並返回 400 錯誤（預設值："auto"） | COMBO | 是 | "auto"<br>"disabled" |
| `max_output_tokens` | 回應可產生的 token 數量上限，包含可見輸出 token 與推理 token（預設值：4096） | INT | 否 | 16 to 16384 |
| `instructions` | 提供給模型如何產生回應的指示（支援多行輸入） | STRING | 否 | - |
| `reasoning_effort` | 模型在回答前的推理程度。「default」將選擇權留給模型。支援的程度依模型而異：GPT-6 Astra low-max、GPT-5.6 none-max（無 minimal）、GPT-5.5 none-xhigh、GPT-5.5 Pro medium-xhigh、GPT-5 minimal-high、o-series low-high；GPT-4.1 不進行推理。不支援的程度會於請求送出前被拒絕。（預設值："default"） | COMBO | 否 | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

注意：雖然 `top_p` 與 `temperature` 在 API 規格中被列為屬性，但它們並非所有模型都支援，因此未公開作為輸入。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | 包含指定設定的設定物件，供 OpenAI Chat 節點使用 | OPENAI_CHAT_CONFIG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/zh-TW.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
