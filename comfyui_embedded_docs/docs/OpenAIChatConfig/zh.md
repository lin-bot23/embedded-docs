# OpenAI ChatGPT 高级选项

OpenAIChatConfig 节点可让您定义用于控制 OpenAI Chat 节点如何生成响应的高级选项。您可以设置截断策略、限制输出 token 数量、提供自定义指令，并选择模型在回答前应进行多少推理。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `截断` | 用于模型响应的截断策略。auto：如果当前响应与此前响应的上下文超过模型的上下文窗口大小，模型将截断响应，通过丢弃对话中部的输入项来使其适应上下文窗口。disabled：如果模型响应将超过模型的上下文窗口大小，请求将失败并返回 400 错误（默认值："auto"） | COMBO | 是 | "auto"<br>"disabled" |
| `Token输出上限` | 响应可生成的 token 数量上限，包括可见输出 token 和推理 token（默认值：4096） | INT | 否 | 16到16384 |
| `指令` | 有关模型如何生成响应的指令（支持多行输入） | STRING | 否 | - |
| `reasoning_effort` | 模型在回答前进行多少推理。"default" 将选择权留给模型。支持的级别因模型而异：GPT-6 Astra 支持 low 到 max，GPT-5.6 支持 none 到 max（无 minimal），GPT-5.5 支持 none 到 xhigh，GPT-5.5 Pro 支持 medium 到 xhigh，GPT-5 支持 minimal 到 high，o-series 支持 low 到 high；GPT-4.1 不支持推理。不支持的级别会在请求发送前被拒绝。（默认值："default"） | COMBO | 否 | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

注意：虽然 API 规范中将 `top_p` 和 `temperature` 列为属性，但并非所有模型都支持它们，因此未将它们作为输入公开。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | 包含指定设置的配置对象，用于 OpenAI Chat 节点 | OPENAI_CHAT_CONFIG |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/zh.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
