# ImageYUVToRGB

ImageYUVToRGBノードは、YUV色空間の画像をRGB色空間に変換します。このノードは、Y（輝度）、U（青色差成分）、V（赤色差成分）を表す3つの個別の入力画像を受け取り、それらを1つのRGB画像に合成します。

## 入力

| パラメータ | 説明 | データ型 | 必須 | 範囲 |
| --- | --- | --- | --- | --- |
| `Y` | Y（輝度）成分の入力画像 | IMAGE | はい | - |
| `U` | U（青色差成分）の入力画像 | IMAGE | はい | - |
| `V` | V（赤色差成分）の入力画像 | IMAGE | はい | - |

**注:** 3つの入力画像（Y、U、V）はすべて同時に指定する必要があり、正しく変換するには互換性のあるサイズが必要です。

## 出力

| 出力名 | 説明 | データ型 |
| --- | --- | --- |
| `output` | 変換されたRGB画像 | IMAGE |

> このドキュメントは AI によって生成されました。エラーを見つけた場合や改善のご提案がある場合は、ぜひ貢献してください！ [GitHub で編集](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/ja.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
