# Pixal3DConditioning

```markdown
# Pixal3DConditioning

## 概述

Pixal3DConditioning 节点旨在为 Trellis2 3D 生成流程准备图像条件。它使用 DINOv3 视觉模型从输入图像中提取两个分辨率的视觉特征。然后，这些特征被组织成每个阶段的特征图，可以选择性地通过 NAF 模型进行增强。节点还结合了由水平视野得到的相机数据来计算投影变换矩阵。它输出一个正条件对，包含从图像派生的特征图和投影数据，以及一个负条件对，具有零化的特征张量，用于无分类器引导。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `clip 视觉模型` | 用于特征提取的 DINOv3 ViT-L/16 ClipVision 模型。 | CLIP_VISION | 是 | — |
| `图像` | 来自 ImageCropToMask 节点的预处理图像，用于 Pixal3D，pad_factor 为 1.1。 | IMAGE | 是 | — |
| `相机水平视场角` | 以度为单位的水平视野。此参数可以连接到 MoGeGeometryToFOV 节点以实现每张图像的视野。默认值：49.13。 | FLOAT | 是 | 1.0 – 170.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `正面` | 包含用于 Trellis2 生成从图像派生的特征图和投影数据的正条件输出。 | CONDITIONING |
| `负面` | 包含零化特征张量的负条件输出，用于无分类器引导。 | CONDITIONING |

注意：`camera_angle_x` 值在内部转换为弧度并用于计算投影变换矩阵的相机距离。当提供的视觉模型包含 NAF 组件时，节点还会为形状和纹理阶段生成高分辨率特征图。
```

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/zh.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
