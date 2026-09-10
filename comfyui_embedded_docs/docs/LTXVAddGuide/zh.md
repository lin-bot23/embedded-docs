# LTXV添加指导

LTXVAddGuide 节点通过编码输入图像或视频，并将其作为关键帧合并到 conditioning 数据中，从而向潜在序列添加视频 conditioning 引导。它通过 VAE 编码器处理输入，并将生成的潜在表示策略性地放置在指定的帧位置，同时使用关键帧信息更新正向和负向 conditioning。该节点处理帧对齐约束，并允许控制 conditioning 影响的强度。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `正向` | 将使用关键帧引导修改的正向 conditioning 输入 | CONDITIONING | 是 | - |
| `负向` | 将使用关键帧引导修改的负向 conditioning 输入 | CONDITIONING | 是 | - |
| `vae` | 用于编码输入图像/视频帧的 VAE 模型 | VAE | 是 | - |
| `潜在空间` | 将接收 conditioning 帧的输入潜在序列 | LATENT | 是 | - |
| `图像` | 用于对潜在视频进行条件化的图像或视频。必须为 8*n + 1 帧。如果视频不是 8*n + 1 帧，则会被裁剪到最接近的 8*n + 1 帧。 | IMAGE | 是 | - |
| `帧索引` | 开始 condition 的帧索引。对于单帧图像或包含 1-8 帧的视频，任何 `frame_idx` 值均可接受。对于包含 9 帧及以上的视频，`frame_idx` 必须能被 8 整除，否则将向下舍入到最接近的 8 的倍数。负值从视频末尾开始计数。（默认值：0） | INT | 是 | -9999到9999 |
| `强度` | conditioning 影响的强度，其中 1.0 表示应用完整 conditioning，0.0 表示不应用 conditioning（默认值：1.0） | FLOAT | 是 | 0.0到10.0 |
| `attention_mask` | 可选的像素空间空间掩码。通过自注意力控制每个区域的 conditioning 影响，并与 `strength` 相乘。 | MASK | 否 | - |
| `iclora_parameters` | 可选的 IC-LoRA 参数，来自“获取 IC-LoRA 参数”节点。用于根据特定 IC-LoRA 的要求调整引导处理（例如，具有 `reference_downscale_factor` > 1 的 IC-LoRA）。当链式连接时，每个 LTXVAddGuide 仅使用与其连接的参数。 | IC_LORA_PARAMETERS | 否 | - |

**注意：** 输入图像/视频的帧数必须符合 8*n + 1 模式（例如，1、9、17、25 帧）。如果输入超出此模式，将自动裁剪到最接近的有效帧数。

**关于 `iclora_parameters` 的说明：** 当使用的 IC-LoRA 参数的 `reference_downscale_factor` 大于 1 时，潜在空间维度（宽度和高度）必须能被该因子整除。如果不满足此条件，节点将报错。

**注意：** 编码后的引导帧必须能适合所选帧位置处的潜在序列。如果 conditioning 帧超过潜在序列的长度，节点将报错。

**注意：** 不支持向包含音频和视频通道的潜在表示添加引导，否则将报错。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `正向` | 已使用关键帧引导信息更新的正向 conditioning | CONDITIONING |
| `负向` | 已使用关键帧引导信息更新的负向 conditioning | CONDITIONING |
| `潜在空间` | 已包含 conditioning 帧并更新噪声掩码的潜在序列 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/zh.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
