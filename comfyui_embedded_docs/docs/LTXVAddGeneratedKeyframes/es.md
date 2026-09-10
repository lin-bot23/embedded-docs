# LTXVAddGeneratedKeyframes

## Resumen

El nodo LTXV Agregar Keyframes Generados añade detalles de keyframes a un video latente. Cada keyframe representa un solo cuadro latente de tokens que abarca un solo cuadro de píxeles, que se suaviza con el video y no forma parte de la salida decodificada. La ubicación se determina por el parámetro interval_frames, que especifica el paso de cuadro de píxeles para el autoajuste.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `positive` | Condicionamiento positivo al que se adjuntan los keyframes. | CONDITIONING | Sí | N/A |
| `negative` | Condicionamiento negativo al que se adjuntan los keyframes. | CONDITIONING | Sí | N/A |
| `vae` | Únicamente utilizado para leer los factores de escala latentes. | VAE | Sí | N/A |
| `latent` | Latente de video plano 5D al que se generan keyframes junto. Añádalo antes de Concat AV Latent. | LATENT | Sí | N/A |
| `interval_frames` | Paso de cuadro de píxeles para el autoajuste. El valor predeterminado 24 es aproximadamente un keyframe por segundo a 24 fps. Los píxeles ocupados se saltan. Se ignora cuando frame_indices está configurado. | INT | No | 1-1024 |
| `keyframes` | Contenido opcional para inicializar los nuevos keyframes. Conecte keyframes de un Separar (tamaño espacial similar) o un latente de video plano para copiar el cuadro más cercano en cada nuevo espacio (por ejemplo, después de un upscale temporal). Estos aún se suavizan, no se fijan como guías. Los índices grabados en un latente de keyframes se ignoran a menos que frame_indices esté configurado. Solo tiene efecto cuando se comienza a muestrear por debajo de sigma 1. | LATENT | No | N/A |
| `frame_indices` | Índices de cuadro de píxeles opcionales. Deje en blanco para ubicar desde interval_frames en el lienzo actual. Cuando se configura, esta lista es la ubicación (los keyframes conectados se coinciden en orden). El último cuadro está permitido; el cuadro 0 no (ya es un token autónomo). | STRING | No | N/A |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `positive` | Condicionamiento positivo con atención de keyframes generados adjunta. | CONDITIONING |
| `negative` | Condicionamiento negativo con atención de keyframes generados adjunta. | CONDITIONING |
| `latent` | Latente de video con keyframes generados añadidos en T. | LATENT |

## Notas

- El parámetro `interval_frames` determina el espaciado de los keyframes en el video. Un valor más alto resulta en menos keyframes y una tasa de cuadros más baja.
- La entrada `keyframes` le permite inicializar los nuevos keyframes con keyframes existentes o un latente de video. Si se proporciona, estos keyframes se suavizarán y se añadirán al latente de video.
- El parámetro `frame_indices` le permite especificar los índices de cuadro de píxeles exactos donde deben ubicarse los keyframes. Si se proporciona, se ignora el parámetro `interval_frames`.
- Las salidas `positive` y `negative` contienen el condicionamiento con atención de keyframes generados adjunta, que se puede utilizar para procesamiento o análisis adicionales.
- La salida `latent` contiene el latente de video con keyframes generados añadidos en T, que se puede utilizar para procesamiento o análisis adicionales.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/es.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
