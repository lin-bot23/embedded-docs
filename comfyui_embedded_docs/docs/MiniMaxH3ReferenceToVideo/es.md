# MiniMax H3 Referencia a Video

MiniMax H3 Reference to Video crea el condicionamiento de texto y el latente vacío de audio-video necesarios para la generación de video de MiniMax H3 a partir de referencias. Se proporciona un prompt y, opcionalmente, imágenes, videos y clips de audio de referencia; el nodo codifica estas referencias en un condicionamiento que el modelo puede usar al generar. El prompt se refiere a las referencias mediante las etiquetas `<Picture i>`, `<Video k>` y `<Audio j>`.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP utilizado para tokenizar el prompt y codificar los medios de referencia en tokens de condicionamiento. | CLIP | Sí | |
| `vae` | VAE de video utilizado para codificar imágenes de referencia y fotogramas de video de referencia. Sin él, las imágenes y videos de referencia solo condicionan el codificador de texto. | VAE | No | |
| `audio_vae` | VAE de audio utilizado para codificar el audio de referencia. El audio se remuestrea a la frecuencia de muestreo del VAE de audio (32 kHz por defecto). Sin él, el audio de referencia solo condiciona el codificador de texto. | VAE | No | |
| `prompt` | Prompt de texto para el video. Los medios de referencia se pueden indicar con las etiquetas `<Picture i>`, `<Video k>` y `<Audio j>` (numeración desde 1 por tipo). Admite prompts multilínea y dinámicos. | STRING | Sí | |
| `ancho` | Ancho del video generado en píxeles (predeterminado: 1344). | INT | Sí | 32 a 16384 (paso 32) |
| `alto` | Altura del video generado en píxeles (predeterminado: 768). | INT | Sí | 32 a 16384 (paso 32) |
| `duración` | Número de fotogramas a 24 fps; 124 = ~5 s, el rango de entrenamiento es ~124-362 (predeterminado: 124). | INT | Sí | 5 a 3600 (paso 17) |
| `tamaño_imagen_ref` | Redimensionado de las imágenes de referencia. `match` reduce cada imagen de referencia únicamente, manteniendo la relación de aspecto, al área de píxeles de la generación; `max` usa el borde corto de 2048 píxeles del pipeline de referencia para obtener la mejor fidelidad de identidad. Los tokens de referencia atraviesan cada paso de muestreo, por lo que `max` puede ser varias veces más lento (predeterminado: `match`). | COMBO | Sí | `"match"`<br>`"max"` |
| `imágenes_ref` | Entrada ampliable: conecta hasta 9 imágenes de referencia (`ref_image_1` ... `ref_image_9`). Las imágenes de referencia se reducen a un borde corto de 2048 píxeles si son más grandes y nunca se amplían. | IMAGE | No | 0 a 9 |
| `videos_ref` | Entrada ampliable: conecta hasta 3 videos de referencia (`ref_video_1` ... `ref_video_3`). Fotogramas de video de referencia a 24 fps (2-15 s). | IMAGE | No | 0 a 3 |
| `audios_video_ref` | Entrada ampliable: conecta hasta 3 bandas sonoras (`ref_video_audio_1` ... `ref_video_audio_3`). Banda sonora del video de referencia con el mismo número. | AUDIO | No | 0 a 3 |
| `audios_ref` | Entrada ampliable: conecta hasta 3 clips de audio de referencia independientes (`ref_audio_1` ... `ref_audio_3`). | AUDIO | No | 0 a 3 |

Notas:

- El prompt se refiere a los medios de referencia con etiquetas numeradas desde 1 por tipo: `<Picture i>` para imágenes, `<Video k>` para videos y `<Audio j>` para audio. Las referencias se presentan al modelo en un orden fijo: imágenes, luego videos (con la etiqueta `<Audio j>` de cada banda sonora justo antes de su `<Video k>`), y a continuación el audio independiente.
- Una banda sonora conectada a `ref_video_audio_N` se utiliza con el video de referencia conectado a `ref_video_N`.
- Los videos de referencia deben contener al menos 5 fotogramas (~0,2 segundos a 24 fps); de lo contrario, el nodo genera un error. Los fotogramas que exceden la `length` solicitada se recortan, y el número restante de fotogramas se ajusta a un valor compatible con el modelo.
- La `length` solicitada se alinea a un número de fotogramas compatible con el modelo antes de que se cree el latente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `positivo` | Condicionamiento que contiene el prompt codificado. Cuando se proporcionan medios de referencia y los VAE correspondientes, también contiene el contenido codificado de imagen, video y audio de referencia utilizado por el modelo MiniMax H3. | CONDITIONING |
| `latent` | Latente vacío de audio-video con los valores `width`, `height` y `length` (número de fotogramas) solicitados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/es.md)

---
**Source fingerprint (SHA-256):** `47df0d6d13cb02aa4f69b50a7f8d0f6c1639c1fb5e0f69bf8fc57dd4cb752db8`
