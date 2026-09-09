# LTXVAddGeneratedKeyframes

```markdown
# LTXV 添加生成的关键帧

## 概述

LTXV 添加生成的关键帧节点将详细关键帧附加到视频潜在数据上。每个关键帧代表一个跨越单个像素帧的潜在帧，这些帧与视频一起去噪，但不属于解码输出的一部分。位置由 interval_frames 参数确定，该参数指定了自动放置的像素帧步长。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 关键帧附加到的正条件。 | CONDITIONING | 是 | N/A |
| `negative` | 关键帧附加到的负条件。 | CONDITIONING | 是 | N/A |
| `vae` | 仅用于读取潜在尺度因子。 | VAE | 是 | N/A |
| `latent` | 普通的 5D 视频潜在数据，用于生成与关键帧一起的关键帧。在 Concat AV Latent 之前添加它们。 | LATENT | 是 | N/A |
| `interval_frames` | 自动放置的像素帧步长。默认 24 大约是每秒一个关键帧，在 24 fps 的情况下。占用像素将被跳过。当 frame_indices 设置时被忽略。 | INT | 否 | 1-1024 |
| `keyframes` | 可选内容，用于初始化新的关键帧。从较早的 Separate（相同的空间大小）或普通视频潜在数据连接关键帧，以在每个新槽中复制最近的帧（例如，在时间上采样之后）。这些帧仍然会被去噪，不会作为引导固定。除非 frame_indices 设置，否则忽略关键帧潜在数据上的记录索引。只有当采样开始低于 sigma 1 时才有效。 | LATENT | 否 | N/A |
| `frame_indices` | 可选的像素帧索引。留空以从 interval_frames 在当前画布上放置。当设置时，此列表是放置位置（按顺序匹配连接的关键帧）。允许最后一个帧；帧 0 不允许（它已经是一个独立的标记）。 | STRING | 否 | N/A |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 附加了生成关键帧注意力的正条件。 | CONDITIONING |
| `negative` | 附加了生成关键帧注意力的负条件。 | CONDITIONING |
| `latent` | 在 T 上附加了生成关键帧的视频潜在数据。 | LATENT |

## 注意事项

- `interval_frames` 参数确定视频中关键帧的间隔。值越大，关键帧越少，帧率越低。
- `keyframes` 输入允许您使用现有的关键帧或视频潜在数据初始化新的关键帧。如果提供，这些关键帧将被去噪并附加到视频潜在数据上。
- `frame_indices` 参数允许您指定关键帧应放置的确切像素帧索引。如果提供，则忽略 `interval_frames` 参数。
- `positive` 和 `negative` 输出包含附加了生成关键帧注意力的条件，可用于进一步处理或分析。
- `latent` 输出包含附加了生成关键帧的视频潜在数据，可用于进一步处理或分析。
```

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/zh.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
