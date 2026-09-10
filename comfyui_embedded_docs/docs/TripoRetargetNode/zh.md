# Tripo: 重定向绑定模型

TripoRetargetNode 将预设动画应用于现有的已绑定骨骼的 3D 模型。它接收先前已绑定骨骼的模型的任务 ID，向 Tripo API 发送重定向请求，并下载生成的动画文件。动画模型可以以 GLB 或 FBX 格式返回，并可选择包含网格几何体和可选的原地播放。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `原始模型任务ID` | 要重定向的先前已绑定骨骼的 3D 模型的任务 ID。引用的任务必须是绑定任务。 | RIG_TASK_ID | 是 | - |
| `动画` | 要应用于已绑定骨骼模型的动画预设。`preset:*` 动画适用于两种绑定模型。`preset:biped:*` 动画是为模型 v1.0-20240301 的绑定制作的；v2.5 绑定仅接受 chop、climb、dive、fall、hurt、idle、jump、run、shoot、slash、turn 和 walk。 | COMBO | 是 | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>以及 UI 中显示的其他 `"preset:biped:*"` 选项 |
| `out_format` | 输出文件格式；结果会出现在匹配的输出上。（默认值：glb） | COMBO | 否 | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | 在导出中包含网格；关闭则仅导出动画骨架。（默认值：True） | BOOLEAN | 否 | True<br>False |
| `animate_in_place` | 原地播放动画，不产生根位移。（默认值：False） | BOOLEAN | 否 | True<br>False |
| `auth_token_comfy_org` | 用于 Comfy.org API 访问的身份验证令牌（隐藏参数）。 | AUTH_TOKEN_COMFY_ORG | 否 | - |
| `api_key_comfy_org` | 用于 Comfy.org 服务访问的 API 密钥（隐藏参数）。 | API_KEY_COMFY_ORG | 否 | - |
| `unique_id` | 用于跟踪操作的唯一标识符（隐藏参数）。 | UNIQUE_ID | 否 | - |

注意：`preset:*` 组中的动画适用于两种绑定模型。`preset:biped:*` 组中的动画是为模型 v1.0-20240301 的绑定制作的；v2.5 绑定仅接受 chop、climb、dive、fall、hurt、idle、jump、run、shoot、slash、turn 和 walk。如果引用的绑定是使用 Mixamo 规格创建的，并且模型版本以 `v1.0` 开头，则重定向调用会失败并报错。请求的输出格式必须是 GLB 或 FBX；如果服务返回任何其他文件类型，节点会引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `模型文件` | 生成的动画 3D 模型文件（仅用于向后兼容）。 | STRING |
| `重定向任务ID` | 用于跟踪重定向操作的任务 ID。 | RETARGET_TASK_ID |
| `GLB` | GLB 格式的动画 3D 模型。当 `out_format` 为 glb 时填充。 | FILE3DGLB |
| `FBX` | FBX 格式的动画 3D 模型。当 `out_format` 为 fbx 时填充。 | FILE3DFBX |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/zh.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`
