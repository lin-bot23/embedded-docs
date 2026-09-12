# 转换图像色彩空间

ImageColorSpace 节点可在 sRGB（Rec.709）、线性 Rec.709、HDR（Rec.2020 HLG）和 HDR PQ（Rec.2020 PQ）色彩空间之间转换图像。转换为 SDR 输出或从 HDR PQ 转换为 HDR 时，它会在整个批次中对超出亮度进行色调映射，并压缩超出色域的颜色；linear 输出与 linear 转 HDR 的转换则会在不做色调映射的情况下保留扩展值。转换以 float32 计算，任何 alpha 通道都会原样传递。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要转换的输入图像。 | IMAGE | 是 | 任意有效图像。 |
| `source` | 输入像素的色彩空间。默认值："sRGB"。 | COMBO | 是 | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |
| `destination` | 输出像素的色彩空间。将保存节点设置为相同的色彩空间。默认值："sRGB"。 | COMBO | 是 | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 在指定目标色彩空间中转换后的图像。 | IMAGE |

## 说明

- 线性 1.0 使用与 sRGB 相同的 203-nit 参考白；HLG 使用 1000-nit 参考显示。
- 线性输出和线性到 HDR 的转换会保留扩展值，而不进行色调映射。
- SDR 输出和 PQ 到 HLG 的转换会在整个批次中对超出亮度进行色调映射（共享一个白点，因此曝光不会逐帧变化），并压缩超出色域的颜色。
- 转换以 float32 计算，并返回中间设备和 dtype。
- Straight alpha 不进行色彩变换；仅转换 RGB 通道。
- 如果 `source` 和 `destination` 相同，则不会应用色彩变换——图像只会移动到中间设备和 dtype。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/zh.md)

---
**Source fingerprint (SHA-256):** `04ae447a9f9805341e31755ad0fa56746ac0371fa2cb9bda95df3879c9dbead7`
