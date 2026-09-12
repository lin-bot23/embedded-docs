# 创建视频

Create Video 节点将一系列图像合成为视频。您可以设置播放速度（以帧/秒为单位），可选添加音频，并选择生成视频的压缩格式、位深度和色彩空间。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `图像` | 用于创建视频的图像。 | IMAGE | 是 | - |
| `帧率` | 视频播放速度的帧/秒（默认值：30.0）。 | FLOAT | 是 | 1.0 - 120.0 |
| `音频` | 要添加到视频的音频。 | AUDIO | 否 | - |
| `bit_depth` | 自动模式对 sRGB 使用 8 位，对 HDR 和 HDR PQ 使用 10 位。显式选择 8 位和 10 位与色彩空间无关。（默认值："auto"） | COMBO | 否 | `"auto"`<br>8<br>10 |
| `color_space` | 输入图像的色彩空间。HDR 选择 BT.2020/HLG，HDR PQ 选择 BT.2020/PQ。（默认值："sRGB"） | COMBO | 否 | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `codec` | 可选地立即编码视频。None 将图像保持为张量形式；Auto 使用 H.264。（默认值："none"） | COMBO | 否 | `"none"`<br>视频编解码器列表中可用的视频编解码器选项（例如 `"auto"` 和其他受支持的编解码器） |

注意：当 `bit_depth` 设置为 `"auto"` 时，节点会自动对 HDR 和 HDR PQ 色彩空间使用 10 位，对 sRGB 使用 8 位。

注意：`codec` 参数是一个高级选项。当其保留为 `"none"` 时，输出保持张量形式；选择任何其他编解码器都会立即编码视频。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 包含输入图像和可选音频的生成视频。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/zh.md)

---
**Source fingerprint (SHA-256):** `9274559caabbafbcaad47883bf017967f9685f155ea1031e66cf22ee8d0d14c3`
