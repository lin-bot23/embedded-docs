# ByteDance Primer-Último-Fotograma a Video

# ByteDance First-Last-Frame to Video

Este nodo genera un video utilizando un texto de indicación junto con los primeros y últimos cuadros de una imagen. Crea una transición suave entre los dos cuadros, resultando en una secuencia de video completa. El nodo ofrece una gama de opciones para personalizar la resolución, relación de aspecto, duración y parámetros adicionales de generación del video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | El modelo a utilizar para la generación de video. Seleccione de las opciones disponibles (por defecto: `"seedance-1-5-pro-251215"`). | COMBO | Sí | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"` |
| `prompt` | El texto de indicación utilizado para generar el video. Este indicación no debe contener parámetros específicos como resolución, relación de aspecto, duración, seed, camerafixed o watermark. | STRING | Sí | - |
| `primer_fotograma` | El primer cuadro a ser utilizado para el video. La imagen debe estar entre 300x300 y 6000x6000 píxeles y tener un relación de aspecto entre 0.4 y 2.5. | IMAGE | Sí | - |
| `último_fotograma` | El último cuadro a ser utilizado para el video. La imagen debe estar entre 300x300 y 6000x6000 píxeles y tener un relación de aspecto entre 0.4 y 2.5. | IMAGE | Sí | - |
| `resolución` | La resolución del video de salida. Elija de las opciones disponibles (por defecto: `"480p"`). | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `relación_de_aspecto` | El relación de aspecto del video de salida. Seleccione de las opciones disponibles (por defecto: `"adaptive"`). | COMBO | Sí | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duración` | La duración del video de salida en segundos (por defecto: 5). Para el modelo `seedance-1-5-pro-251215`, la duración mínima soportada es de 4 segundos. | INT | Sí | 3 - 12 |
| `semilla` | La semilla a utilizar para la generación (por defecto: 0). Este parámetro es opcional. | INT | No | 0 - 2147483647 |
| `cámara_fija` | Especifica si se debe fijar la cámara en el video. La plataforma adjunta una instrucción para fijar la cámara a su indicación, pero el efecto real no está garantizado (por defecto: Falso). | BOOLEAN | No | - |
| `marca_de_agua` | Determina si se debe agregar una marca de agua "Generado por IA" al video (por defecto: Falso). | BOOLEAN | No | - |
| `generate_audio` | Este parámetro se ignora para todos los modelos excepto `seedance-1-5-pro-251215` (por defecto: Falso). | BOOLEAN | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output` | El archivo de video generado. | VIDEO |

## Notas

- El parámetro `model` determina las capacidades y limitaciones del proceso de generación de video.
- El indicación `prompt` debe ser creativo y claro, ya que guiará la generación del video.
- Las imágenes `first_frame` y `last_frame` deben ser representativas del contenido deseado del video.
- Los parámetros `resolution` y `aspect_ratio` afectarán la calidad y dimensiones finales del video de salida.
- El parámetro `duration` establece la longitud del video, con un mínimo de 3 segundos y un máximo de 12 segundos.
- El parámetro `seed` es opcional y puede ser utilizado para la reproducibilidad del proceso de generación de video.
- El parámetro `camera_fixed` es una opción avanzada que puede no siempre resultar en el efecto esperado.
- El parámetro `watermark` puede ser utilizado para agregar una marca de agua al video, indicando que fue generado por una IA.
- El parámetro `generate_audio` se ignora actualmente para todos los modelos excepto `seedance-1-5-pro-251215`.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `ae0f3a34a21baad7f04f6917e98d16dc64496479a050896869ec6693a9a9ebaf`
