# OpenAI ChatGPT

此節點從 OpenAI 模型生成文字回應。它接受文字提示，並可選地使用圖片或文件作為上下文，然後將此信息發送到 OpenAI 模型以生成文字回應。

## Inputs

| 參數 | 描述 | 資料類型 | 必要 | 范圍 |
|------|------|----------|------|-------|
| `prompt` | 將輸入到模型的文字，用於生成回應。這是您希望模型回應的文字。 | STRING | 是 | - |
| `persist_context` | 此參數已棄用並無作用。為了後向相容性而包含，但並不影響節點的行為。 | BOOLEAN | 否 | - |
| `model` | 用於生成回應的模型。從可用的 OpenAI 模型中選擇。 | COMBO | 是 | gpt-6-astra<br>gpt-5.6-sol<br>gpt-5.6-terra<br>gpt-5.6-luna<br>gpt-5.5-pro<br>gpt-5.5<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br>gpt-4.1<br>gpt-4.1-mini<br>gpt-4.1-nano<br>o4-mini<br>o3<br>o1-pro<br>o1 |
| `images` | 用作模型上下文的可選圖片。若要包含多個圖片，可以使用批量圖片節點。 | IMAGE | 否 | - |
| `files` | 用作模型上下文的可選文件。接受從 OpenAI Chat Input Files 節點的輸入。 | OPENAI_INPUT_FILES | 否 | - |
| `advanced_options` | 用於模型的可選配置。接受從 OpenAI Chat Advanced Options 節點的輸入。 | OPENAI_CHAT_CONFIG | 否 | - |

## Outputs

| 輸出名稱 | 描述 | 資料類型 |
|----------|------|-----------|
| `output_text` | 由 OpenAI 模型生成的文字回應。這是基於輸入提示和上下文生成的文字。 | STRING |

## 記錄

- `persist_context` 參數已棄用並無作用。為了後向相容性而包含，但應該不使用。
- `images` 輸入可用於向模型提供額外的上下文。若提供多個圖片，應使用批量圖片節點將其連接。
- `files` 輸入允許您以文件的形式提供額外的上下文。這些文件應從 OpenAI Chat Input Files 節點連接。
- `advanced_options` 輸入允許對模型的行為進行更詳細的配置。這應從 OpenAI Chat Advanced Options 節點連接。
- 使用此節點的價格取決於選擇的模型。費用是基於模型使用的代碼數量計算的。具體費用將在節點的 UI 中顯示。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `687a6b1110518a2eaf23e240f43991b4ff91d6f01cae6c3ef55bcdac810e7a89`
