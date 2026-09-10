# 加载3D（高级）

Load 3D (Advanced) 节点从 ComfyUI 的 `input/3d` 目录中加载 3D 模型文件，并提供模型数据，以及 3D 查看器视口状态中捕获的模型放置和相机信息。它支持常见的 3D 文件格式，并允许您以像素为单位设置视口的渲染宽度和高度。此节点为实验性功能。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model_file` | 要加载的 3D 模型文件。选择“none”可跳过加载模型文件。 | COMBO | 是 | `"none"`<br>`input/3d` 目录中可用的 3D 模型文件 |
| `viewport_state` | 当前视口状态，包含来自 3D 查看器的相机和模型信息。 | LOAD3D | 是 | - |
| `width` | 视口的渲染宽度（像素，默认值：1024）。 | INT | 是 | 最小值：1<br>最大值：4096<br>默认值：1024<br>步长：1 |
| `height` | 视口的渲染高度（像素，默认值：1024）。 | INT | 是 | 最小值：1<br>最大值：4096<br>默认值：1024<br>步长：1 |

**参数说明：**
- `model_file` 参数仅列出具有以下扩展名的文件：.gltf、.glb、.obj、.fbx、.stl
- 文件必须放置在 ComfyUI 安装目录的 `input/3d` 目录中；也会搜索子文件夹，文件路径相对于输入目录显示
- 如果 `model_file` 为“none”，则不会加载模型数据，`model_3d` 输出将为空
- 如果 `model_file` 设置为不存在的文件，节点将返回验证错误：“Invalid 3D model file: {model_file}”

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `model_3d` | 已加载的 3D 模型文件（glb/obj/stl 等）。如果未选择模型文件则为空。 | FILE3DANY |
| `model_3d_info` | 场景中每个模型的放置信息：位置、旋转和缩放（Y 轴向上的世界空间）。 | LOAD3DMODELINFO |
| `camera_info` | 视口相机信息：位置、注视目标、缩放和类型。 | LOAD3DCAMERA |
| `width` | 视口的渲染宽度（像素）。 | INT |
| `height` | 视口的渲染高度（像素）。 | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/zh.md)

---
**Source fingerprint (SHA-256):** `c79c53dde0c8b3afb7df7b972df749f5040c92d48b47e355c4497d9b0cbf1c22`
