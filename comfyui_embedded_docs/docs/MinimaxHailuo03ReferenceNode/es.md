# MiniMax H3 Referencia a Video

Este nodo genera un video utilizando los modelos MiniMax H3, condicionado por imágenes, videos y audio de referencia. Las referencias se mencionan en el prompt según su orden de conexión: "Image 1", "Image 2", "Video 1", "Audio 1", etc. Hay dos modelos disponibles: "MiniMax H3" y "MiniMax H3 Max".

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | Modelo a usar para la generación de video (por defecto: "MiniMax H3"). Seleccionar "MiniMax H3" proporciona las entradas de generación y referencia de MiniMax H3 a continuación. Seleccionar "MiniMax H3 Max" proporciona las entradas de generación y referencia de MiniMax H3 Max a continuación. | DYNAMIC_COMBO | Sí | "MiniMax H3"<br>"MiniMax H3 Max" |
| `seed` | Semilla aleatoria. La misma solicitud con la misma semilla produce resultados similares, aunque no se garantiza que sean idénticos (por defecto: 42). | INT | Sí | 0 a 4294967295 |
| `watermark` | Si se debe añadir una marca de agua AIGC al video (por defecto: false). Solo es compatible con el modelo MiniMax H3. | BOOLEAN | No | true<br>false |

### Entradas de MiniMax H3

Estas entradas están disponibles cuando se selecciona "MiniMax H3" como modelo.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt de texto para la generación de video. Los medios de referencia pueden mencionarse por su orden, por ejemplo "Image 1", "Image 2", "Video 1" o "Audio 1". | STRING | Sí | Mínimo 1 carácter |
| `resolution` | Resolución del video de salida (por defecto: "768P"). | COMBO | Sí | "768P"<br>"2K" |
| `ratio` | Relación de aspecto del video de salida (por defecto: "adaptive"). | COMBO | Sí | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Duración del video de salida en segundos (por defecto: 5). | INT | Sí | 4 a 15 |

### Entradas de MiniMax H3 Max

Estas entradas están disponibles cuando se selecciona "MiniMax H3 Max" como modelo.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt de texto para la generación de video. Los medios de referencia pueden mencionarse por su orden, por ejemplo "Image 1", "Image 2", "Video 1" o "Audio 1". | STRING | Sí | De 1 a 50000 caracteres |
| `resolution` | Resolución del video de salida (por defecto: "768P"). | COMBO | Sí | "480P"<br>"768P" |
| `ratio` | Relación de aspecto del video de salida (por defecto: "adaptive"). | COMBO | Sí | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Duración del video de salida en segundos (por defecto: 5). | INT | Sí | 5 a 15 |
| `prompt_expansion_mode` | Cuánto esfuerzo se dedica a reescribir el prompt antes de la generación (por defecto: "balanced"). | COMBO | Sí | "balanced"<br>"quality" |
| `reference_detail` | Nivel de detalle con el que se envían las imágenes de referencia. "high" las envía al mayor tamaño que usa el modelo (hasta 2048 píxeles en el lado corto); "standard" las reduce a un máximo de 2048x1024 para reducir el costo de referencia (por defecto: "standard"). | COMBO | Sí | "high"<br>"standard" |

### Entradas de referencia

Estas entradas de referencia son compartidas por ambos modelos. Cada una es una ranura ampliable.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `reference_images` | Ranura ampliable: conecte hasta 9 elementos (`image_1`...`image_9`). Imágenes de referencia de sujeto o estilo, mencionadas en el prompt como "Image 1"..."Image 9" en orden de conexión. Hasta 9 imágenes. | IMAGE | No | De 0 a 9 imágenes |
| `reference_videos` | Ranura ampliable: conecte hasta 3 elementos (`video_1`...`video_3`). Videos de referencia de movimiento o escena, mencionados en el prompt como "Video 1"..."Video 3" en orden de conexión. Hasta 3 videos, de 2 a 15 segundos cada uno, con un total de 15 segundos. | VIDEO | No | De 0 a 3 videos |
| `reference_audios` | Ranura ampliable: conecte hasta 3 elementos (`audio_1`...`audio_3`). Referencias de audio, mencionadas en el prompt como "Audio 1"..."Audio 3" en orden de conexión. Hasta 3 clips, de 2 a 15 segundos cada uno, con un total de 15 segundos. No se puede usar sin una imagen o video de referencia. | AUDIO | No | De 0 a 3 clips |

### Restricciones de los parámetros

- Se requiere al menos una imagen de referencia o un video de referencia. El audio de referencia por sí solo no se acepta.
- Cada imagen de referencia debe tener una relación de aspecto entre aproximadamente 0.4 y 2.5 (2:5 a 5:2) y un mínimo de 256 píxeles de ancho y alto.
- Cada video de referencia debe tener una duración de entre 2 y 15 segundos, con una velocidad de fotogramas entre 23.976 y 60 FPS. La duración total de todos los videos de referencia no puede superar los 15 segundos.
- Cada clip de audio de referencia debe tener una duración de entre 2 y 15 segundos. La duración total de todos los clips de audio de referencia no puede superar los 15 segundos.
- Cuando se selecciona "MiniMax H3 Max", el ajuste `watermark` debe estar desactivado.
- Cuando se selecciona "MiniMax H3 Max", el número total de archivos de referencia (imágenes, videos y audio combinados) no puede superar 12.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/es.md)

---
**Source fingerprint (SHA-256):** `b77eedb1f7757e60518c04484f1cc24c27cf6886b3ae31c15207ea49fd436a73`
