# Tripo: 纹理化模型

此节点在源码中标记为已弃用（旧版）；显示名称为 "Tripo: Texture model (Legacy)"。现有文档的参数表与当前源码仍然一致；以下保留这些参数表，并在概述中说明其旧版状态。

Tripo: Texture model (Legacy) 节点通过 Tripo API 为现有的 Tripo 3D 模型添加纹理。它接收由另一个 Tripo 节点创建的模型的任务 ID，并在纹理任务完成后返回带纹理的 GLB 或 FBX 模型。你可以控制材质贴图、纹理质量、对齐方式和种子，并通过文本提示、风格图像或参考图像来引导纹理。此节点是纹理工具的旧版版本。

## 输入

### 通用输入

| 参数 | 说明 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `模型任务ID` | 要添加纹理的模型的 Tripo 任务 ID。接受模型任务 ID 和分割任务 ID。 | MODEL_TASK_ID, SEGMENT_TASK_ID | 是 | - |
| `纹理` | 已忽略：此节点始终生成纹理。为兼容旧工作流而保留。（默认值：True） | BOOLEAN | 否 | true<br>false |
| `PBR` | PBR 材质贴图（基础色、金属度、粗糙度、法线）；关闭后生成纯色纹理。（默认值：True） | BOOLEAN | 否 | true<br>false |
| `纹理种子` | 纹理生成的随机种子。（默认值：42） | INT | 否 | 0 – 2147483647 |
| `纹理质量` | 纹理分辨率质量：detailed = HD 纹理，extreme = 8K Ultra 纹理。（默认值："standard"）。大致费用：standard $0.10，detailed $0.20，extreme $0.30。 | COMBO | 否 | "standard"<br>"detailed"<br>"extreme" |
| `纹理对齐` | 用于将生成的纹理与模型对齐的方法。（默认值："original_image"） | COMBO | 否 | "original_image"<br>"geometry" |
| `texture_prompt` | 可选的纹理工序文本引导。对于导入的模型（Tripo: Import Model）实际上是必需的，因为这类模型没有可用于推断颜色的源图像。不能与参考图像同时使用。（默认值：""） | STRING | 否 | - |
| `model_version` | 纹理模型：v3.0 用于由 v3.x 生成的网格，v2.5 用于由 v2.5 生成的网格。（默认值：v3.0_20250812） | COMBO | 否 | 有多个可用选项 |
| `style_image` | 用于纹理艺术风格的参考图像。仅与 `texture_prompt` 一起使用。 | IMAGE | 否 | - |
| `reference` | 用于引导纹理的参考图像。不能与 `texture_prompt` 或 `style_image` 同时使用。（默认值："none"） | DYNAMIC_COMBO | 否 | "none"<br>"image"<br>"multiview" |
| `part_names` | 来自 Tripo: Segment Model 的逗号分隔部件名称，用于指定要添加纹理的部件。留空则为每个部件添加纹理。（默认值：""） | STRING | 否 | - |

### `image` 参考输入

当 `reference` 设置为 `"image"` 时，这些输入可用。

| 参数 | 说明 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | 纹理应遵循的单个参考图像。 | IMAGE | 是 | - |

### `multiview` 参考输入

当 `reference` 设置为 `"multiview"` 时，这些输入可用。

| 参数 | 说明 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image_front` | 前视图（0°）。 | IMAGE | 是 | - |
| `image_left` | 左视图（90°）。 | IMAGE | 是 | - |
| `image_back` | 后视图（180°）。 | IMAGE | 是 | - |
| `image_right` | 右视图（270°）。 | IMAGE | 是 | - |

**注意：** `"image"` 和 `"multiview"` 参考模式不能与非空的 `texture_prompt` 或 `style_image` 同时使用。`style_image` 输入要求 `texture_prompt` 非空。当 `texture_prompt` 留空时，源模型必须已经拥有自己的源图像（例如由 text-to-model、image-to-model、multiview-to-model 或更早的纹理工序生成的模型）。不携带源图像的模型——例如导入、分割、已完成或重拓扑的模型——必须使用 `texture_prompt` 添加纹理；只有 Tripo API 自身生成的模型才接受参考图像。`part_names` 输入可以留空，以便为每个部件添加纹理。

## 输出

| 输出名称 | 说明 | 数据类型 |
|-------------|-------------|-----------|
| `模型文件` | 生成的模型文件（仅用于向后兼容）。 | STRING |
| `模型任务ID` | 已完成的纹理生成任务的任务 ID，可用作其他 Tripo 节点的输入。 | MODEL_TASK_ID |
| `GLB` | 生成的 GLB 格式带纹理模型。当源为四边形网格或 FBX 导入时为空。 | FILE3DGLB |
| `FBX` | 生成的 FBX 格式带纹理模型。Tripo 对四边形网格和 FBX 导入返回 FBX；其他情况为空。 | FILE3DFBX |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/zh.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`
