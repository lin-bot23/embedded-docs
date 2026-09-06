# MiniMax H3 Primer-Último Fotograma a Video

Este nodo genera un video a partir de una imagen de primer fotograma y, opcionalmente, de una imagen de último fotograma, utilizando los modelos MiniMax H3. El selector `model` cambia la configuración y las restricciones de generación que se aplican, y la relación de aspecto del video generado sigue la de las imágenes suministradas.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo que se usará para la generación de video. Al seleccionar un modelo, se muestran sus ajustes específicos a continuación. | DYNAMIC_COMBO | Sí | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `first_frame` | Imagen del primer fotograma para el video. El video generado sigue la relación de aspecto de esta imagen. | IMAGE | Sí | - |
| `last_frame` | Imagen opcional del último fotograma para el video. Cuando se proporciona, el video se genera desde el primer fotograma hacia este último fotograma. | IMAGE | No | - |
| `seed` | Semilla aleatoria. La misma solicitud con la misma semilla genera resultados similares, aunque no se garantiza que sean idénticos. Incluye una opción "control after generate". Predeterminado: 42. | INT | Sí | 0 a 4294967295 |
| `watermark` | Indica si se debe añadir una marca de agua AIGC al video. Este es un parámetro avanzado. Solo es compatible con el modelo `MiniMax H3`. Predeterminado: False. | BOOLEAN | Sí | True<br>False |

### Entradas de MiniMax H3

Estos ajustes se muestran cuando se selecciona `MiniMax H3` en el selector `model`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para la generación de video. Debe contener al menos un carácter que no sea un espacio en blanco. | STRING | Sí | Texto multilínea |
| `resolution` | Resolución del video de salida. | COMBO | Sí | "768P"<br>"2K" |
| `duration` | Duración del video de salida en segundos. Predeterminado: 5. | INT | Sí | 4 a 15 |

### Entradas de MiniMax H3 Max y MiniMax H3 Max Turbo

Estos ajustes se muestran cuando se selecciona `MiniMax H3 Max` o `MiniMax H3 Max Turbo` en el selector `model`. Ambos modelos exponen los mismos ajustes.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para la generación de video. No debe estar vacío ni contener solo espacios en blanco, y está limitado a 50 000 caracteres. | STRING | Sí | Texto multilínea |
| `resolution` | Resolución del video de salida. Predeterminado: 768P. | COMBO | Sí | "480P"<br>"768P" |
| `duration` | Duración del video de salida en segundos. Predeterminado: 5. | INT | Sí | 5 a 15 |
| `prompt_expansion_mode` | Cuánto esfuerzo se invierte en reescribir el prompt antes de la generación. Predeterminado: balanced. | COMBO | Sí | "balanced"<br>"quality" |

**Notas sobre las restricciones:**

- El prompt debe contener texto: se rechazan los prompts vacíos o que contengan solo espacios en blanco.
- Cualquier imagen de fotograma suministrada debe tener al menos 256 píxeles de ancho y 256 píxeles de alto, con una relación de aspecto de ancho a alto entre 0,4 y 2,5 (aproximadamente de 2:5 a 5:2). Este requisito se aplica a `first_frame` y, cuando se proporciona, a `last_frame`.
- Cuando se omite `last_frame`, el video se genera únicamente a partir del primer fotograma.
- El video de salida sigue la relación de aspecto de las imágenes suministradas.
- `watermark` solo es compatible con `MiniMax H3`. Si se habilita con `MiniMax H3 Max` o `MiniMax H3 Max Turbo`, se producirá un error.
- La duración va de 4 a 15 segundos para `MiniMax H3`, y de 5 a 15 segundos para `MiniMax H3 Max` y `MiniMax H3 Max Turbo`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `video` | El video generado a partir del primer fotograma y del último fotograma opcional, utilizando el modelo MiniMax H3 seleccionado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `6eaf895e6e9e46b9a1efb1dd13e951040e12e865cc73d7741ab7546f5f8f9ec0`
