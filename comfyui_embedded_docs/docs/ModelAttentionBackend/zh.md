# 模型注意力后端

## 概述

ModelAttentionBackend 节点允许您为模型选择一个密集注意力实现。它将选定的注意力后端修补到模型中，当可用时可以是 PyTorch 注意力或 Comfy Kitchen 注意力。当稀疏注意力不可用或不支持时，此节点特别有用，确保模型以指定的密集注意力机制运行。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 将使用选定的注意力后端修补的模型。 | MODEL | 是 |  |
| `attention` | 要应用于模型的密集注意力后端。可用的选项是 "pytorch attention" 和当环境中有可用时 "comfy kitchen attention"。 | STRING | 是 | "pytorch attention"<br> "comfy kitchen attention" (当可用时) |

- "comfy kitchen attention" 选项使用量化 INT8 注意力，并且仅在 Nvidia 和 AMD GPU 上受支持。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `模型` | 应用了选定的注意力后端的输入模型。 | MODEL |

## 注意

- 如果选定的注意力后端不可用，节点将自动回退到使用 PyTorch 注意力并记录一条警告。
- ModelAttentionBackend 节点是实验性的，未来版本中可能会有所变化。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/zh.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
