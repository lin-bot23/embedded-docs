# Tripo：分割模型

此节点将 3D 模型拆分为各个独立部件。它将模型发送至 Tripo 分割服务，等待任务完成，然后以 GLB 格式返回分割后的模型，并附带一个以逗号分隔的部件名称列表。这些部件名称将用于后续步骤，例如 Tripo: Complete Mesh Parts、Tripo: Retopology 和 Tripo: Convert model。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 取值范围 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 待分割为多个部件的 3D 模型的任务 ID。 | MODEL_TASK_ID | 是 | N/A |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model_file` | 分割后 GLB 模型的输出文件名，格式为 `<task_id>.glb`。仅为向后兼容而保留。 | STRING |
| `segment task_id` | 生成该结果的分割任务的任务 ID。 | SEGMENT_TASK_ID |
| `GLB` | 分割后的 3D 模型，以 GLB 文件形式提供。 | GLB |
| `part_names` | 以逗号分隔的部件名称。 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/zh.md)

---
**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`
