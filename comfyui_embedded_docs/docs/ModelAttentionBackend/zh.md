# 模型注意力后端

此节点用于选择模型在进行注意力计算时所使用的密集注意力后端。它会克隆给定模型，应用所选后端，并返回修补后的克隆。当与 Block Sparse Attention 一起使用时，只要稀疏注意力未激活或不支持，就会使用此后端。如果所选后端不可用，节点会自动回退到 PyTorch attention。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 取值范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要修补的模型。 | MODEL | 是 |  |
| `attention` | 要应用的密集注意力后端（默认值："pytorch attention"）。Comfy Kitchen attention 使用量化的 INT8 注意力，并且仅在 Nvidia 和 AMD GPU 上可用。如果所选后端不可用，将使用 PyTorch attention 作为回退。 | COMBO | 是 | "pytorch attention"<br>"comfy kitchen attention" |

注意：仅当当前环境中存在 Comfy Kitchen INT8 attention 模块时，才会列出 "comfy kitchen attention" 选项。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `模型` | 输入模型的克隆，并已应用所选的注意力后端。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/zh.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
