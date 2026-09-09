# LTXVSeparateGeneratedKeyframes

## Overview

The LTXV Separate Generated Keyframes node removes generated keyframes from a sampled latent and conditioning, allowing for separate handling before spatially upscaling the video latent. It is designed to be used before spatial upscaling and should not be run after LTXV Crop Guides, as it treats generated keyframes as disposable guides and drops them.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `positive` | Positive conditioning with generated-keyframe metadata removed. | CONDITIONING | Yes | N/A |
| `negative` | Negative conditioning with generated-keyframe metadata removed. | CONDITIONING | Yes | N/A |
| `latent` | Video latent with the generated keyframes stripped. | LATENT | Yes | N/A |
| `keyframes_to_batch` | Return the keyframes as a batch of single-frame latents. Leave off to get them as one multi-frame latent, which is what the latent upsampler and a later Add Generated Keyframes expect. | BOOLEAN | No | default: False |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | Positive conditioning with generated-keyframe metadata removed. | CONDITIONING |
| `negative` | Negative conditioning with generated-keyframe metadata removed. | CONDITIONING |
| `latent` | Video latent with the generated keyframes stripped. | LATENT |
| `keyframes` | The peeled keyframes, labeled with generated_keyframe_indices and generated_keyframe_num_frames. Feed these to a later Add Generated Keyframes to initialize new slots, or to Generated Keyframes To Guides to pin them as frozen image guides (indices are remapped if the canvas length changed). | LATENT |

## Notes

- The `keyframes_to_batch` parameter determines whether the keyframes are returned as a batch of single-frame latents or as one multi-frame latent.
- The node ensures that the generated keyframes are removed from the conditioning and the latent before any further processing.
- The `keyframes` output can be used to initialize new slots for generated keyframes or to pin them as frozen image guides.
- The node raises a `ValueError` if the latent does not contain generated keyframes or if the keyframes do not match the expected format.
- The node assumes that the generated keyframes were added using the LTXV Add Generated Keyframes node and that they are compatible with the current latent.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/en.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
