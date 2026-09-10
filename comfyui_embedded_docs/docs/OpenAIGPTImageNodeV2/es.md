# OpenAI GPT Image 2

Este nodo genera imágenes mediante la API GPT Image de OpenAI. Es compatible con cinco modelos — `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5` y `gpt-image-1` —, permite adjuntar imágenes de referencia para la edición de imágenes y puede usar una máscara para especificar qué partes de una imagen se deben reemplazar.

## Entradas

### Entradas comunes

Estas entradas siempre están visibles.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo OpenAI GPT Image que se usará. Al seleccionar un modelo, se muestran parámetros adicionales específicos de ese modelo. | DYNAMIC_COMBO | Sí | `"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Indicación de texto para GPT Image (predeterminado: `""`). | STRING | Sí | N/A |
| `n` | Cuántas imágenes generar (predeterminado: `1`). | INT | Sí | 1 a 8 |
| `semilla` | Semilla para la reproducibilidad (predeterminado: `0`). Aún no implementada en el backend. | INT | Sí | 0 a 2147483647 |

### Entradas de gpt-image-2.5-flare y gpt-image-2.5-sunburst

Estas entradas aparecen cuando `model` se establece en `gpt-image-2.5-flare` o `gpt-image-2.5-sunburst`. Ambos modelos comparten el mismo conjunto de parámetros.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `tamaño` | Tamaño de la imagen. Seleccione "Custom" para usar el ancho y el alto personalizados (predeterminado: `"auto"`). | COMBO | Sí | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `ancho_personalizado` | Se usa solo cuando `model.size` es "Custom". Debe ser un múltiplo de 16 (predeterminado: `1024`). | INT | No | 480 a 3840 (paso 16) |
| `altura_personalizada` | Se usa solo cuando `model.size` es "Custom". Debe ser un múltiplo de 16 (predeterminado: `1024`). | INT | No | 480 a 3840 (paso 16) |
| `fondo` | Devuelve la imagen con o sin fondo (predeterminado: `"auto"`). | COMBO | Sí | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `calidad` | Calidad de la imagen; afecta al costo y al tiempo de generación (predeterminado: `"low"`). | COMBO | Sí | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Imágenes de referencia opcionales para la edición de imágenes. Hasta 16 imágenes. Consulte Entradas de referencia para más detalles. | IMAGE | No | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (las áreas blancas se reemplazarán). Requiere exactamente una imagen de referencia. | MASK | No | N/A |

### Entradas de gpt-image-2

Estas entradas aparecen cuando `model` se establece en `gpt-image-2`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `tamaño` | Tamaño de la imagen. Seleccione "Custom" para usar el ancho y el alto personalizados (predeterminado: `"auto"`). | COMBO | Sí | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `ancho_personalizado` | Se usa solo cuando `model.size` es "Custom". Debe ser un múltiplo de 16 (predeterminado: `1024`). | INT | No | 480 a 3840 (paso 16) |
| `altura_personalizada` | Se usa solo cuando `model.size` es "Custom". Debe ser un múltiplo de 16 (predeterminado: `1024`). | INT | No | 480 a 3840 (paso 16) |
| `fondo` | Devuelve la imagen con o sin fondo (predeterminado: `"auto"`). | COMBO | Sí | `"auto"`<br>`"opaque"` |
| `calidad` | Calidad de la imagen; afecta al costo y al tiempo de generación (predeterminado: `"low"`). | COMBO | Sí | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imágenes de referencia opcionales para la edición de imágenes. Hasta 16 imágenes. Consulte Entradas de referencia para más detalles. | IMAGE | No | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (las áreas blancas se reemplazarán). Requiere exactamente una imagen de referencia. | MASK | No | N/A |

### Entradas de gpt-image-1.5 y gpt-image-1

Estas entradas aparecen cuando `model` se establece en `gpt-image-1.5` o `gpt-image-1`. Ambos modelos comparten el mismo conjunto de parámetros.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `tamaño` | Tamaño de la imagen (predeterminado: `"auto"`). | COMBO | Sí | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `fondo` | Devuelve la imagen con o sin fondo (predeterminado: `"auto"`). | COMBO | Sí | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `calidad` | Calidad de la imagen; afecta al costo y al tiempo de generación (predeterminado: `"low"`). | COMBO | Sí | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imágenes de referencia opcionales para la edición de imágenes. Hasta 16 imágenes. Consulte Entradas de referencia para más detalles. | IMAGE | No | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (las áreas blancas se reemplazarán). Requiere exactamente una imagen de referencia. | MASK | No | N/A |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model.images` | Ranura ampliable: conecte de 1 a N elementos (p. ej., `image_1`...`image_16`); hasta 16 imágenes de referencia para todos los modelos. | IMAGE | No | 1 a 16 |
| `model.mask` | Máscara opcional para inpainting (las áreas blancas se reemplazarán). Requiere exactamente una imagen de referencia. | MASK | No | N/A |

**Restricciones y limitaciones de los parámetros:**

- Cuando `model.size` es "Custom" (solo para `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` y `gpt-image-2`), `model.custom_width` y `model.custom_height` deben ser múltiplos de 16, el lado más largo no debe superar 3840, la relación de aspecto no debe exceder 3:1 y el número total de píxeles debe estar entre 655 360 y 8 294 400.
- `model.mask` requiere exactamente una imagen de referencia en `model.images`: no puede usarse sin una imagen ni con más de una imagen.
- Cuando se usa `model.mask`, su altura y anchura deben coincidir con la altura y anchura de la imagen de referencia.
- Cuando se proporciona `model.images`, el nodo funciona en modo de edición de imágenes; sin `model.images`, genera imágenes solo a partir de la indicación.
- Las imágenes de referencia y la máscara se reducen de escala antes de enviarse a la API.
- Los niveles de calidad `"xhigh"` y `"max"` solo están disponibles para `gpt-image-2.5-flare` y `gpt-image-2.5-sunburst`.
- La opción de fondo `"transparent"` está disponible para `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-1.5` y `gpt-image-1`, pero no para `gpt-image-2`.
- El parámetro `seed` no está implementado actualmente en el backend.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `image` | La imagen o imágenes generadas. Todas las imágenes devueltas se apilan en un solo lote; si sus dimensiones difieren, se redimensionan para que coincidan con la primera imagen. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `4f77b79f9f432a1f2e0fd814012aebe7cc42a8aa983ee9a61f3b32984bf65148`
