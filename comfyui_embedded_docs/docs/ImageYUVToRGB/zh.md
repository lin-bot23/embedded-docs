# 图像YUV到RGB

ImageYUVToRGB 节点可将 YUV 色彩空间的图像转换为 RGB 色彩空间。它接收三张独立的输入图像，分别代表 Y（亮度）、U（蓝色投影）和 V（红色投影）分量，并将它们组合成一张 RGB 图像。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `Y` | Y（亮度）分量输入图像 | IMAGE | 是 | - |
| `U` | U（蓝色投影）分量输入图像 | IMAGE | 是 | - |
| `V` | V（红色投影）分量输入图像 | IMAGE | 是 | - |

**注意：** 三张输入图像（Y、U 和 V）必须同时提供，并且尺寸应兼容，才能正确转换。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 转换后的 RGB 图像 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/zh.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
