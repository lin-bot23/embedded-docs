# ByteDance Imagen a Video

# Nodo ByteDance: Imagen a Vídeo

El nodo ByteDance: Imagen a Vídeo genera un vídeo a partir de una imagen de entrada y un texto de sugerencia utilizando la API de ByteDance. Crea una secuencia de vídeo que visualmente representa la descripción proporcionada, con opciones para personalizar la resolución, el aspecto, la duración y otros parámetros de la salida.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | El modelo ByteDance a utilizar para la generación de vídeo. Las opciones disponibles son: <br>`"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` | STRING | Sí | Como se lista arriba |
| `prompt` | El texto de sugerencia utilizado para generar el vídeo. Debe tener al menos 1 carácter después de quitar los espacios en blanco. | STRING | Sí | - |
| `imagen` | La primera imagen a ser utilizada para el vídeo. La imagen debe estar entre 300x300 y 6000x6000 píxeles, con un aspecto entre 0.4 y 2.5. | IMAGE | Sí | - |
| `resolución` | La resolución del vídeo de salida. Las opciones disponibles son: <br>`"480p"`<br>`"720p"`<br>`"1080p"` | STRING | Sí | Como se lista arriba |
| `relación_de_aspecto` | El aspecto del vídeo de salida. Las opciones disponibles son: <br>`"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | STRING | Sí | Como se lista arriba |
| `duración` | La duración del vídeo de salida en segundos. Para el modelo `seedance-1-5-pro-251215`, la duración mínima soportada es de 4 segundos. | INT | Sí | 3 - 12 |
| `semilla` | Semilla a utilizar para la generación. Opcional, con un valor predeterminado de 0. | INT | No | 0 - 2147483647 |
| `cámara_fija` | Especifica si se debe fijar la cámara. La plataforma adjunta una instrucción para fijar la cámara a su sugerencia, pero no garantiza el efecto real. Opcional, con un valor predeterminado de Falso. | BOOLEAN | No | - |
| `marca_de_agua` | Si se debe agregar una marca de agua "Generado por IA" al vídeo. Opcional, con un valor predeterminado de Falso. | BOOLEAN | No | - |
| `generate_audio` | Este parámetro se ignora para cualquier modelo excepto `seedance-1-5-pro-251215`. Opcional, con un valor predeterminado de Falso. | BOOLEAN | No | - |

**Nota:** El texto de sugerencia no debe contener las siguientes palabras (sin distinción de mayúsculas y minúsculas): `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Estos parámetros se configuran a través de sus entradas dedicadas.

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `output` | El archivo de vídeo generado basado en los parámetros de imagen de entrada y sugerencia. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `9f4ad18642533689f9c664f2ca6a4ce8e92c8698754cdf9b6bb2d2735bc80415`
