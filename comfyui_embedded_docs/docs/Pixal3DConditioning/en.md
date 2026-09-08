# Pixal3DConditioning

```markdown
# Pixal3DConditioning

## Overview

The Pixal3DConditioning node is designed to prepare image conditioning for the Trellis2 3D generation pipeline. It utilizes a DINOv3 vision model to extract visual features from the input image at two resolutions. These features are then organized into per-stage feature maps, which can be optionally enhanced with a NAF model. The node also incorporates camera data derived from the horizontal field of view to compute the projection transform matrix. It outputs a positive conditioning pair that includes the image-derived feature maps and projection data, as well as a negative conditioning pair with zeroed feature tensors for classifier-free guidance.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | The DINOv3 ViT-L/16 ClipVision model used for feature extraction. | CLIP_VISION | Yes | — |
| `image` | The preprocessed image from the ImageCropToMask node, intended for Pixal3D with a pad_factor of 1.1. | IMAGE | Yes | — |
| `camera_angle_x` | The horizontal field of view in degrees. This parameter can be wired to a MoGeGeometryToFOV node for a per-image field of view. Default: 49.13. | FLOAT | Yes | 1.0 – 170.0 |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | The positive conditioning output containing the image-derived feature maps and projection data for Trellis2 generation. | CONDITIONING |
| `negative` | The negative conditioning output with zeroed feature tensors, used for classifier-free guidance. | CONDITIONING |

Note: The `camera_angle_x` value is converted to radians internally and used to compute the camera distance for the projection transform matrix. When the supplied vision model includes a NAF component, the node also produces high-resolution feature maps for the shape and texture stages.
```

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/en.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
