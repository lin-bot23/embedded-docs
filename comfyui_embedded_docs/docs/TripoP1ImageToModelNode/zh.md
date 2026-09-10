# Tripo P1：图像转模型

Tripo P1: Image to Model 使用 Tripo P1 API 将单张 2D 图像转换为 3D 模型。它针对生成低多边形、可用于游戏的网格进行了优化，并可选择仅生成几何体网格，或生成带 PBR 贴图的纹理模型。完成的模型会以 GLB 文件返回。

## 输入

### 通用输入

这些参数始终可用。

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `输出模式` | 选择结果类型。`"Geometry only"` 返回未贴图的网格；`"Textured"` 会添加颜色/PBR 贴图，并显示额外的纹理设置。 | DYNAMIC_COMBO | 是 | `"Geometry only"`<br>`"Textured"` |
| `图像` | 用于生成 3D 模型的源 2D 图像。必须提供单张图像；如果未提供，节点会报错。 | IMAGE | 是 | - |
| `启用图像自动修复` | 预处理输入图像，以获得更好的生成质量。（默认：False） | BOOLEAN | 否 | True<br>False |
| `面数限制` | 目标面数，48-20000。-1 表示让 Tripo 自适应选择。（默认：-1） | INT | 否 | -1 to 20000 |
| `模型种子` | 用于几何生成的种子，以便复现结果。（默认：42） | INT | 否 | 0 to 2147483647 |
| `自动缩放` | 将输出缩放到接近真实世界的米制尺寸。（默认：False） | BOOLEAN | 否 | True<br>False |
| `导出 UV` | 生成期间进行 UV 展开。关闭可加快仅几何体生成速度。（默认：True） | BOOLEAN | 否 | True<br>False |
| `压缩几何体` | 应用 meshopt 几何压缩（EXT_meshopt_compression）。文件更小，但 ComfyUI 的 3D 预览无法显示它们；编辑前请先解压。（默认：False） | BOOLEAN | 否 | True<br>False |

### Geometry only 输入

无额外参数。输出为未贴图的网格。

### Textured 输入

当 `output_mode` 设置为 `"Textured"` 时，会出现这些参数。

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `pbr` | 包含 PBR 贴图。开启时，基础纹理也会被强制开启。（默认：True） | BOOLEAN | 是 | True<br>False |
| `texture_quality` | `detailed` = HD 纹理，`extreme` = 8K Ultra 纹理。（默认：`"standard"`） | COMBO | 是 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | 优先考虑对源图像的视觉保真度，或与网格几何体对齐。（默认：`"original_image"`） | COMBO | 是 | `"original_image"`<br>`"geometry"` |
| `orientation` | 旋转输出以匹配源图像。仅适用于带纹理模式。（默认：`"default"`） | COMBO | 是 | `"default"`<br>`"align_image"` |
| `texture_seed` | 用于纹理生成的种子，以便复现带纹理结果。（默认：42） | INT | 是 | 0 to 2147483647 |

注意：当 `output_mode` 为 `"Geometry only"` 时，请求中会禁用纹理生成。在 `"Textured"` 模式下，始终会请求颜色纹理；禁用 `pbr` 会移除 PBR 贴图，但保留基础颜色纹理；而启用 `pbr` 会同时强制开启基础纹理。`texture_alignment` 和 `orientation` 仅在 `"Textured"` 模式下可用。

## 输出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `模型文件` | 包含生成的模型文件名的字符串（`<task_id>.glb`）。仅为向后兼容而保留。 | STRING |
| `模型任务 ID` | Tripo API 为已完成的生成任务返回的唯一任务 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。 | FILE3DGLB |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/zh.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`
