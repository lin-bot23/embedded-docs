# LTXVAddLatentGuide

```markdown
# LTXV 添加潜在引导

## 概述

LTXV 添加潜在引导节点将已编码的潜在变量作为引导，允许使用来自早期阶段的引导而不是图像。此节点避免了 VAE 解码/编码往返，并且可以将空间上较小的引导扩展到稀疏网格上，以覆盖目标画布。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 正向条件输入。 | CONDITIONING | 是 | N/A |
| `negative` | 负向条件输入。 | CONDITIONING | 是 | N/A |
| `vae` | 要使用的 VAE 模型。 | MODEL | 是 | N/A |
| `latent` | 引导附加到的目标视频潜在变量。 | LATENT | 是 | N/A |
| `guiding_latent` | 引导潜在变量。其空间大小必须在两个轴上都能被目标的大小整除相同的整数；相同大小则按原样固定，半大小被视为 x2 IC-LoRA 参考。 | LATENT | 是 | N/A |
| `latent_idx` | 从中开始引导的潜在帧索引，按潜在帧计算，而不是像素帧。负值将引导放置在潜在变量开始之前的帧上，而不是从其末尾回退计算。 | INT | 是 | -9999 到 9999 |
| `strength` | 限制在 1.0。扩展的引导使用负去噪掩码标记其填充位置，以便模型丢弃它们；超过 1.0 的值会使保留的位置变为负数，整个引导将被丢弃。使用 attention_mask 替代放大超过 1.0 的值。 | FLOAT | 是 | 0.0 到 1.0，步长 0.01 |
| `attention_mask` | 可选的像素空间空间掩码。通过自注意力控制每个区域的条件影响，乘以强度。 | MASK | 否 | N/A |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 正向条件输出。 | CONDITIONING |
| `negative` | 负向条件输出。 | CONDITIONING |
| `latent` | 应用了引导的潜在变量输出。 | LATENT |

## 注意事项

- `guiding_latent` 的空间大小必须在两个轴上都能被 `latent` 的大小整除相同的整数。
- `latent_idx` 参数允许在潜在帧内精确放置引导。
- `strength` 参数控制引导的强度，值超过 1.0 需要使用 `attention_mask` 以避免出现负数位置。
- `attention_mask` 参数是可选的，但可用于微调图像特定区域的引导影响。
```

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/zh.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
