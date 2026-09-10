# Tripo：图像转多视图

使用 Tripo API 从单张输入图像生成主体的正面、左侧、背面和右侧视图。图像会被上传，启动多视图生成任务并轮询直至完成，随后返回四个生成的视图以及任务 ID。这是一项付费任务，费用约为 0.10 美元。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 主体的源图像，Tripo 据此生成正面、左侧、背面和右侧视图。即使提供的是批次图像，请求中也只使用一张图像。 | IMAGE | 是 | 单张图像 |

注意：此节点会调用 Tripo 的云端 API 并等待生成任务完成。典型任务大约需要 25 秒。认证通过节点的隐藏输入自动处理，因此无需在工作流中提供 Tripo API 密钥。此节点要求 Tripo 响应中包含全部四个视图 URL（`front_view_url`、`left_view_url`、`back_view_url`、`right_view_url`）；如果缺少任何视图，执行将失败并报错。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `多视图 task_id` | Tripo 为多视图图像生成请求返回的任务标识符。可用于引用已完成的任务，例如使用 Tripo: Edit Multiview 对视图进行精修时。 | MULTIVIEW_TASK_ID |
| `前方` | 生成的主体的正面视图。 | IMAGE |
| `左侧` | 生成的主体的左侧视图。 | IMAGE |
| `后方` | 生成的主体的背面视图。 | IMAGE |
| `右侧` | 生成的主体的右侧视图。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/zh.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`
