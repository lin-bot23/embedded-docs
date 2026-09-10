# OpenAI ChatGPT

此節點會從 OpenAI 模型產生文字回應。它會將您的文字提示，以及可選的圖片或檔案，傳送給 OpenAI 模型，並傳回產生的文字回應。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 提供給模型的文字輸入，用於產生回應（預設為空字串）。 | STRING | 是 | - |
| `persist_context` | 此參數已棄用，且沒有任何效果（預設為 False）。 | BOOLEAN | 是 | - |
| `model` | 用於產生回應的模型（預設為 `gpt-5`）。 | COMBO | 是 | `gpt-6-astra`<br>`gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | 可選的圖片，作為提供給模型的上下文。若要包含多張圖片，可使用「Batch Images」節點。 | IMAGE | 否 | - |
| `files` | 可選的檔案，作為提供給模型的上下文。接受來自「OpenAI Chat Input Files」節點的輸入。 | OPENAI_INPUT_FILES | 否 | - |
| `advanced_options` | 可選的模型設定。接受來自「OpenAI Chat Advanced Options」節點的輸入。 | OPENAI_CHAT_CONFIG | 否 | - |

注意：當所連接的 `advanced_options` 設定中指定了推理強度時，所選的 `model` 必須支援該強度值。例如，gpt-4.1 系列模型不支援任何推理強度，`gpt-5.5` 支援 none、low、medium、high 和 xhigh，而 `gpt-5.5-pro` 支援 medium、high 和 xhigh。如果所選模型不支援該推理強度，節點會引發錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output_text` | 由 OpenAI 模型產生的文字回應。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `687a6b1110518a2eaf23e240f43991b4ff91d6f01cae6c3ef55bcdac810e7a89`
