# LTXVGeneratedKeyframesToGuides

```markdown
# LTXV Generated Keyframes to Guides

## Overview

The LTXV Generated Keyframes to Guides node pins generated keyframes from an earlier stage as frozen image guides on a later canvas. It decodes the keyframes as standalone frames, resizes them if needed, and writes them with a noise mask of 0 to prevent further denoising. The recorded indices are scaled from the canvas they were generated on to the target canvas, and you can override the frame indices to set positions explicitly.

## Inputs

| Parameter                 | Description                                                                 | Data Type | Required | Range |
|---------------------------|-----------------------------------------------------------------------------|-----------|----------|-------|
| `positive`                | Positive conditioning with the keyframes pinned as image guides.             | CONDITIONING | Yes      |       |
| `negative`                | Negative conditioning with the keyframes pinned as image guides.             | CONDITIONING | Yes      |       |
| `vae`                     | The VAE model to use for decoding the keyframes.                           | MODEL      | Yes      |       |
| `latent`                  | The target video latent to add the guides to, e.g., the temporally upscaled one. | LATENT     | Yes      |       |
| `keyframes`               | The keyframes output of LTXV Separate Generated Keyframes, which carries the pixel frame index each keyframe was generated at. | LATENT     | Yes      |       |
| `strength`                | Guide strength. 1.0 is a hard pin; lower values relax it.                   | FLOAT      | Yes      | 0.0 - 10.0 |
| `override_frame_indices` | Optional — pin at these pixel frames instead of the recorded (or auto-scaled) positions. Provide one index per keyframe. Leave empty to reuse recorded positions, or to scale them when the target canvas is a different length (e.g., after temporal x2). | STRING    | No       |       |

## Outputs

| Output Name | Description                                                                 | Data Type |
|-------------|-----------------------------------------------------------------------------|-----------|
| `positive`  | Positive conditioning with the keyframes pinned as image guides.             | CONDITIONING |
| `negative`  | Negative conditioning with the keyframes pinned as image guides.             | CONDITIONING |
| `latent`    | Target video latent with the keyframes added as frozen guides.               | LATENT     |

## Notes

- The `strength` parameter controls how strongly the keyframes are pinned as guides. A value of 1.0 creates a hard pin, while lower values relax the pinning.
- The `override_frame_indices` parameter allows you to specify the exact pixel frames where the keyframes should be pinned. If left empty, the node will use the recorded positions or scale them if necessary.
- The node assumes that the `keyframes` latent contains the pixel frame index for each keyframe. If this is not the case, the node will raise a `ValueError`.
- The node only supports a batch size of 1. Each guide is encoded from one image, so it cannot differ across batch elements.
- The node will raise a `ValueError` if the `samples` tensor in the `latent` input is not a 5D tensor or if the batch size is not 1.
- The node will raise a `ValueError` if the `samples` tensor in the `keyframes` input is not a 5D tensor or if the batch size is not 1.
- The node will raise a `ValueError` if the shape of the `samples` tensor in the `keyframes` input does not match the shape of the `samples` tensor in the `latent` input after resizing.
- The node will raise a `ValueError` if the `strength` parameter is outside the range of 0.0 to 10.0.
- The node will raise a `ValueError` if the `override_frame_indices` parameter is not a comma-separated list of integers or if the number of indices does not match the number of keyframes.
- The node will raise a `ValueError` if any of the indices in the `override_frame_indices` parameter are outside the range of 1 to the number of pixel frames in the target canvas.
- The node will raise a `ValueError` if the maximum index in the `override_frame_indices` parameter is greater than the number of pixel frames in the target canvas.
```

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/en.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
