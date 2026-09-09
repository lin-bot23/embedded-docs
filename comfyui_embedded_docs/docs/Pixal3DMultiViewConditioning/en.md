# Pixal3DMultiViewConditioning

## Overview

The Pixal3D Multi-View Conditioning node is a fixed orbit rig that generates front, left, back, and right views of an object at 90-degree intervals. It is used to create framed views for Pixal3D applications, where the object spans approximately 1/1.1 of the frame at its widest, maintaining the same scale in every view.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision with bundled NAF weights. | MODEL | Yes | N/A |
| `fov` | Horizontal FOV in degrees of the views as framed. | FLOAT | Yes | 1.0 - 170.0 |
| `front` | Square view of the object's front side, with alpha or on a black background. | IMAGE | Yes | N/A |
| `left` | Square view of the object's left side, with alpha or on a black background. | IMAGE | Optional | N/A |
| `back` | Square view of the object's back side, with alpha or on a black background. | IMAGE | Optional | N/A |
| `right` | Square view of the object's right side, with alpha or on a black background. | IMAGE | Optional | N/A |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | The positive conditioning output for the Pixal3D Multi-View Conditioning node. | CONDITIONING |
| `negative` | The negative conditioning output for the Pixal3D Multi-View Conditioning node. | CONDITIONING |

## Notes

- The `fov` parameter controls the horizontal field of view of the views as framed. A value of 20 degrees is typical for rig renders and most multi-view generators.
- The first connected view (front, left, back, right order) is considered the front, and the mesh is posed to this view.
- If no front view is provided, a warning is logged, and the mesh will be posed with the first connected view as its front.
- The node assumes that the views are square and framed like the rig. The object should span about 1/1.1 of the frame at its widest, and the same scale should be maintained in every view.
- The node outputs two Conditioning objects, one for the positive and one for the negative conditioning. These can be used to condition Pixal3D models or other nodes that accept Conditioning inputs.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/en.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`
