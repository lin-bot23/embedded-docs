# Tripo: 绑定模型

此节点接收现有的 Tripo 3D 模型，并创建其绑定骨骼版本，也就是说模型会获得骨架，从而可以制作动画。你提供要绑定骨骼的模型的任务 ID，选择绑定版本、骨架类型、骨骼命名风格和输出文件格式，节点会将任务发送到 Tripo，等待其完成，然后返回下载的结果。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `原始模型任务ID` | 要绑定骨骼的原始 3D 模型的任务 ID。这通常是之前 Tripo 模型生成节点生成的 ID。 | MODEL_TASK_ID | 是 | - |
| `model_version` | 要使用的绑定模型版本。v1.0：仅支持类人（双足）角色，90 多个动画预设。v2.5：非类人生物（四足、六足、八足、鸟类、蛇形、水生）。默认值：`v1.0-20240301`。 | COMBO | 否 | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | 骨架类型。"auto" 会先运行 Tripo 的免费绑定检查，并使用推荐的类型。默认值："auto"。 | COMBO | 否 | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | 骨骼命名：Tripo 原生或兼容 Mixamo。Tripo 无法将其动画预设重定向到使用 mixamo 规范制作的 v1.0 绑定骨骼上；请使用 tripo for Tripo: Retarget rigged model。默认值："tripo"。 | COMBO | 否 | "tripo"<br>"mixamo" |
| `out_format` | 输出文件格式；结果会出现在匹配的输出上。默认值："glb"。 | COMBO | 否 | "glb"<br>"fbx" |

**注意：** v1.0 模型版本（`v1.0-20240301`）仅支持双足骨架。如果与该版本一起使用非双足 `rig_type`，节点会报错，并提示你改用 `v2.5-20260210`。

**注意：** 当 `rig_type` 为 "auto" 时，Tripo 会先检查模型是否可绑定骨骼，并选择推荐的骨架类型。如果 Tripo 报告模型无法绑定骨骼，节点会失败并报错。

**注意：** 该节点期望 Tripo 返回 GLB 或 FBX 文件。如果 Tripo 返回任何其他文件类型，节点会报错。

**注意：** 只有与 `out_format` 匹配的输出会被填充：当 `out_format` 为 "glb" 时填充 `GLB`，当 `out_format` 为 "fbx" 时填充 `FBX`。另一个 3D 输出为空。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `模型文件` | 生成的绑定骨骼模型文件名（任务 ID 加格式扩展名）。仅为向后兼容而保留。 | STRING |
| `绑定任务ID` | 用于跟踪绑定骨骼生成过程的任务 ID。 | RIG_TASK_ID |
| `GLB` | 绑定骨骼后的 GLB 3D 模型。当 `out_format` 为 "glb" 时填充。 | FILE3DGLB |
| `FBX` | 绑定骨骼后的 FBX 3D 模型。当 `out_format` 为 "fbx" 时填充。 | FILE3DFBX |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/zh.md)

---
**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`
