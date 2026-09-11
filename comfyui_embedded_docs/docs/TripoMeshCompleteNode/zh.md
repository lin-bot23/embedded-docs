# Tripo：补全网格部件

补全已分割 3D 模型的各个部件，并修复网格中缺失或损坏的区域。它接收 Tripo 网格分割结果的任务 ID，向 Tripo 请求补全作业，并等待其完成。你可以选择将处理范围限制为特定的部件名称。补全后的模型以 GLB 文件的形式返回。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `segment_task_id` | Tripo 网格分割任务的任务 ID。该任务所得分割模型的各个部件将被补全。请连接前一个 Tripo 网格分割节点的 SEGMENT_TASK_ID 输出。 | SEGMENT_TASK_ID | 是 | Single task ID |
| `part_names` | 要补全的部件名称，以逗号分隔。留空则补全所有部件。默认值：空字符串。名称周围的多余空格会被移除，重复的名称会被忽略。 | STRING | No | Free text or empty |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model_file` | 补全后模型的文件名。此输出仅为向后兼容而保留。 | STRING |
| `模型 task_id` | 已完成的 Tripo 网格补全任务的任务 ID。可作为需要模型任务 ID 的其他 Tripo 节点的输入。 | MODEL_TASK_ID |
| `GLB` | 已补全并修复各部件后的 3D 模型，以 GLB 文件形式下载。 | GLB |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/zh.md)

---
**Source fingerprint (SHA-256):** `c5709231fa2e33e6f3c9b25669acca1d4ae9adb882b90210d703aeddc0d11ecc`
