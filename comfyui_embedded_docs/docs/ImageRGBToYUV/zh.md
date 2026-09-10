# 图像RGB到YUV

ImageRGBToYUV 节点将 RGB 图像转换到 YUV 颜色空间。它会将图像分解为三个分量——Y（亮度）、U（蓝色差色度）和 V（红色差色度）——并将每个分量作为与输入图像尺寸相同的独立图像返回。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `图像` | 要转换为 YUV 的输入 RGB 图像。如果图像包含 alpha 通道，则仅使用前三个（RGB）通道。 | IMAGE | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `Y` | YUV 颜色空间的亮度分量 | IMAGE |
| `U` | YUV 颜色空间的蓝色差色度分量 | IMAGE |
| `V` | YUV 颜色空间的红色差色度分量 | IMAGE |

每个输出的宽度、高度和通道数与输入图像一致。相应的 Y、U 或 V 分量会在所有通道中重复，因此每个输出都会以标准图像形式返回。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/zh.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
