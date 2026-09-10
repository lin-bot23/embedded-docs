# Convert Image Color Space

## Resumen

El nodo ImageColorSpace convierte imágenes entre diferentes espacios de color, incluyendo sRGB, HDR (Rec.2020 HLG) y HDR PQ (Rec.2020 PQ). Soporta la reducción del exceso de luminancia en el tono de mapa a través del lote y la compresión de colores fuera del gamut, y opera únicamente en canales RGB, con los canales alfa pasados sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `image` | La imagen de entrada que debe ser convertida. | IMAGE | Sí | Cualquier formato de imagen válido. |
| `source` | El espacio de color de los píxeles de entrada. | COMBO | Sí | <br> "sRGB" <br> "HDR" <br> "HDR PQ" |
| `destination` | El espacio de color de los píxeles de salida. | COMBO | Sí | <br> "sRGB" <br> "HDR" <br> "HDR PQ" |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `image` | La imagen convertida en el espacio de color de salida especificado. | IMAGE |

## Notas

- El nodo utiliza una pantalla de referencia de 203 nit SDR blanca y una pantalla HLG de 1000 nit para las conversiones.
- Las conversiones se calculan en float32 y devuelven el dispositivo intermedio y el tipo de datos.
- El canal alfa se pasa sin cambios.
- El nodo admite conversiones entre los espacios de color sRGB, HDR (Rec.2020 HLG) y HDR PQ (Rec.2020 PQ).
- El nodo realiza un tono de mapa de reducción y comprime los colores fuera del gamut para asegurar conversiones precisas.
- Se utilizan los canales RGB para las conversiones, y el canal alfa (si está presente) se pasa sin cambios.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/es.md)

---
**Source fingerprint (SHA-256):** `f0d38c6f5b524752a99d51b1a87f0e65c07f3ba36ecb0066d8d10c5b5032d36f`
