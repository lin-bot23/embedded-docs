# Convert Image Color Space

The ImageColorSpace node converts images between sRGB (Rec.709), HDR (Rec.2020 HLG), and HDR PQ (Rec.2020 PQ) color spaces. When narrowing the color space, it tone-maps excess luminance across the batch and compresses out-of-gamut colors. Conversions are computed in float32, and any alpha channel is passed through unchanged.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image` | The input image to be converted. | IMAGE | Yes | Any valid image. |
| `source` | Color space of the input pixels. Default: "sRGB". | COMBO | Yes | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `destination` | Color space of the output pixels. Set the save node to this same color space. Default: "sRGB". | COMBO | Yes | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `image` | The converted image in the specified destination color space. | IMAGE |

## Notes

- The node uses a 203-nit SDR white level and a 1000-nit HLG reference display for conversions.
- Conversions are computed in float32 and return the intermediate device and dtype.
- Straight alpha is not color-transformed; only the RGB channels are converted.
- If `source` and `destination` are the same, no color transformation is applied — the image is only moved to the intermediate device and dtype.
- When narrowing the color space, the node tone-maps excess luminance across the whole batch (sharing one white point so exposure does not change frame by frame) and compresses out-of-gamut colors.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/en.md)

---
**Source fingerprint (SHA-256):** `f0d38c6f5b524752a99d51b1a87f0e65c07f3ba36ecb0066d8d10c5b5032d36f`
