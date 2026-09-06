# ImageRGBToYUV

# Conversión de Imagen RGB a YUV

El nodo ImageRGBToYUV realiza una conversión de espacio de color desde RGB a YUV. Toma una imagen RGB como entrada y produce tres imágenes separadas que representan los canales YUV: Y (luminancia), U (diferencia de azul) y V (diferencia de rojo).

## Entradas

| Parámetro | Descripción | Tipo de Datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `imagen` | La imagen RGB de entrada que debe ser convertida al espacio de color YUV. Esta debe ser una imagen de 3 canales. | IMAGEN | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `Y`         | El canal Y representa la luminancia (brillo) de la imagen. | IMAGEN |
| `U`         | El canal U representa el componente de croma de diferencia de azul. | IMAGEN |
| `V`         | El canal V representa el componente de croma de diferencia de rojo. | IMAGEN |

Las imágenes de salida tendrán las mismas dimensiones que la imagen de entrada.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/es.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
