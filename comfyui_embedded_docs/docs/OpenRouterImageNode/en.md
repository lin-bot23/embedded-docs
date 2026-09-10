# OpenRouterImageNode

This node generates or edits images through OpenRouter using Microsoft's MAI-Image-2.6 models. It supports text-to-image generation as well as image-guided editing with up to five reference images, in seven aspect ratios at either 1K or 1.5K resolution.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The OpenRouter image model used to generate the image. Selecting a model reveals the model-specific options listed below. | DYNAMIC_COMBO | Yes | `microsoft/mai-image-2.6`<br>`microsoft/mai-image-2.6-flash` |

### Mai Image 2.6 and Mai Image 2.6 Flash Inputs

Shared by both model options (`microsoft/mai-image-2.6` and `microsoft/mai-image-2.6-flash`), which expose the same set of parameters.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Describes the image to generate, or the edit to apply to the reference images. Up to 20000 characters. Default: `""` (empty). At least 1 character is required after removing surrounding whitespace. | STRING | Yes | 1 to 20000 characters |
| `aspect_ratio` | Aspect ratio of the generated image, also applied when reference images are connected. Default: `"1:1"`. | COMBO | Yes | `"1:1"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"` |
| `resolution` | Output size tier. 1K is about 1 megapixel (1:1 is 1024x1024, 16:9 is 1360x768); 1.5K is about 2.3 megapixels (1:1 is 1536x1536, 16:9 is 2048x1152). Default: `"1K"`. | COMBO | Yes | `"1K"`<br>`"1.5K"` |
| `seed` | Seed to determine if the node should re-run; the API has no seed, so actual results are nondeterministic regardless of this value. Default: `42`. | INT | Yes | 0 to 2147483647 |

### Reference Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image_1` ... `image_5` | Growable slot: connect 1 to 5 reference images for image-guided editing; a batched input counts once per image. Slots are optional and can be left empty (minimum 0 connected). | IMAGE | No | 0 to 5 images |

**Notes:**

- A maximum of 5 reference images is supported in total across all connected slots; a batched input counts once per image.
- The `prompt` must contain at least 1 character after surrounding whitespace is removed, and cannot exceed 20000 characters.
- Reference images are sent as PNG data and are limited to a total of 2048 x 2048 pixels.
- The `aspect_ratio` setting is applied to the output even when reference images are connected.
- The seed value does not affect the API result; it only determines whether the node re-runs.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `IMAGE` | The generated or edited image. If the service returns several images, they are combined into a single batched IMAGE output. An error is raised if no image is returned or if a returned image cannot be decoded. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterImageNode/en.md)

---
**Source fingerprint (SHA-256):** `f21dd6fa421065b48b270c89ce7b0d55bcf685d71db0c8360cf5d5a4d5ca1b51`
