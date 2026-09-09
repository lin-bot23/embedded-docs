# LTXVSeparateGeneratedKeyframes

## 概述

LTXV 分离生成的关键帧节点从采样的潜在和条件中移除生成的关键帧，允许在空间上采样视频潜在之前进行单独处理。它设计用于在空间上采样之前使用，不应在 LTXV 裁剪引导之后运行，因为它将生成的关键帧视为可丢弃的引导并丢弃它们。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 移除生成关键帧元数据的正条件。 | CONDITIONING | 是 | N/A |
| `negative` | 移除生成关键帧元数据的负条件。 | CONDITIONING | 是 | N/A |
| `latent` | 移除生成关键帧的视频潜在。 | LATENT | 是 | N/A |
| `keyframes_to_batch` | 将关键帧作为单帧潜在的一批返回。不使用则获取一个多帧潜在，这是潜在上采样器和稍后添加生成关键帧所期望的。 | BOOLEAN | 否 | 默认：False |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 移除生成关键帧元数据的正条件。 | CONDITIONING |
| `negative` | 移除生成关键帧元数据的负条件。 | CONDITIONING |
| `latent` | 移除生成关键帧的视频潜在。 | LATENT |
| `keyframes` | 被剥离的关键帧，带有 generated_keyframe_indices 和 generated_keyframe_num_frames 标签。将这些输入到稍后的添加生成关键帧以初始化新槽位，或到生成关键帧到引导以将其固定为冻结图像引导（如果画布长度改变，则索引会被重新映射）。 | LATENT |

## 注意事项

- `keyframes_to_batch` 参数确定关键帧是作为单帧潜在的一批返回，还是作为多帧潜在返回。
- 节点确保在进一步处理之前从条件和潜在中移除生成的关键帧。
- `keyframes` 输出可用于初始化生成关键帧的新槽位或将它们固定为冻结图像引导。
- 如果潜在不包含生成关键帧或关键帧不符合预期的格式，节点将引发 `ValueError`。
- 节点假定生成的关键帧是使用 LTXV 添加生成关键帧节点添加的，并且与当前潜在兼容。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/zh.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
