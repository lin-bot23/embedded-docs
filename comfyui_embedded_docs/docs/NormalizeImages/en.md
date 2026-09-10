# Normalize Image Colors

This node adjusts the pixel values of an input image using a mathematical normalization process. It subtracts a specified mean value from each pixel and then divides the result by a specified standard deviation. This is a common preprocessing step to prepare image data for other machine learning models.

## Overview

The Normalize Images node normalizes the colors of an input image by adjusting its pixel values based on a mean and standard deviation. This process is useful for standardizing image data before applying machine learning algorithms.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image`   | The input image to be normalized. | IMAGE | Yes | - |
| `mean`    | Mean value for normalization. | FLOAT | No | 0.0 - 1.0 (default: 0.5) |
| `std`     | Standard deviation for normalization. | FLOAT | No | 0.001 - 1.0 (default: 0.5) |

The `mean` and `std` parameters are used to normalize the pixel values of the input image. The default values for both parameters are set to 0.5, which is a common choice for normalization.

Note: When the input image includes an alpha (transparency) channel, the alpha channel is not normalized. It is kept unchanged in the output because alpha stores transparency rather than color.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `image`     | The resulting image after the normalization process has been applied. | IMAGE |

The output from the Normalize Images node is the normalized image. The pixel values are adjusted according to the specified mean and standard deviation, and the alpha channel (if present) is preserved.

## Note

The Normalize Images node is designed to handle any batch size of images, making it suitable for batch processing tasks.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/en.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
