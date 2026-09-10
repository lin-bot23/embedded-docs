# Pixal3DConditioning

此节点为 Trellis2 3D 生成流程准备图像条件。它通过 DINOv3 视觉模型以两种分辨率从输入图像中提取视觉特征，将其整理为各阶段的特征图（可选地通过 NAF 模型增强），并与根据水平视场角得出的相机数据相结合。该节点输出一对正负条件，其中负向条件使用清零特征，用于无分类器引导。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `clip 视觉模型` | DINOv3 ViT-L/16 ClipVision。 | CLIP_VISION | 是 | — |
| `图像` | 来自 ImageCropToMask 的预处理图像（用于 Pixal3D 时设置 pad_factor=1.1）。 | IMAGE | 是 | — |
| `相机水平视场角` | 水平视场角（以度为单位，显示名称：fov）。连接 MoGeGeometryToFOV（axis='horizontal', unit='degrees'）可获取逐图像 FoV（与上游默认一致）。默认值：49.13。 | FLOAT | 是 | 1.0 – 170.0 |

注意：`camera_angle_x` 值会在内部转换为弧度，并用于计算投影变换矩阵所需的相机距离。当提供的视觉模型包含 NAF 组件时，该节点还会为形状阶段和纹理阶段额外生成高分辨率特征图。

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `正面` | 包含从图像导出的特征图和投影数据的正向条件，用于 Trellis2 生成。 | CONDITIONING |
| `负面` | 包含清零特征张量的负向条件，用于无分类器引导。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/zh.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
