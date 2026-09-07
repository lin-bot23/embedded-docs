# Normalize Image Colors

This node adjusts the pixel values of an input image using a mathematical normalization process. It subtracts a specified mean value from each pixel and then divides the result by a specified standard deviation. This is a common preprocessing step to prepare image data for other machine learning models. If the input image has an alpha channel, the alpha channel is passed through unchanged so transparency is preserved.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `image` | The input image to be normalized. | IMAGE | Yes | - |
| `mean` | Mean value for normalization (default: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `std` | Standard deviation for normalization (default: 0.5). | FLOAT | No | 0.001 - 1.0 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `image` | The resulting image after the normalization process has been applied. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/en.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842d1e56d478b89e87c1d014fcaad01894a7a2f4a21fa17b83f`
