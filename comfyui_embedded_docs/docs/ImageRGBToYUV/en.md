# Image RGB to YUV

The ImageRGBToYUV node converts an RGB image into the YUV color space. It splits the image into three components — Y (luminance, or brightness), U (blue-difference chroma), and V (red-difference chroma) — and returns each component as a separate image of the same size as the input.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image` | The input RGB image to convert to YUV. If the image contains an alpha channel, only the first three (RGB) channels are used. | IMAGE | Yes | - |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `Y` | The luminance (brightness) component of the YUV color space | IMAGE |
| `U` | The blue-difference chroma component of the YUV color space | IMAGE |
| `V` | The red-difference chroma component of the YUV color space | IMAGE |

Each output has the same width, height, and number of channels as the input image. The corresponding Y, U, or V component is repeated across all channels so that every output is returned as a standard image.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/en.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
