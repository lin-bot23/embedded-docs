# ImageYUVToRGB

# Conversión de Imagen YUV a RGB

El nodo ImageYUVToRGB está diseñado para convertir imágenes del espacio de color YUV al espacio de color RGB. Lo hace tomando tres imágenes de entrada separadas que representan los canales Y (luminancia), U (proyección de azul) y V (proyección de rojo) de la imagen. Estos canales se combinan luego en una imagen RGB utilizando una técnica de conversión de espacio de color.

## Resumen

El nodo ImageYUVToRGB convierte imágenes YUV a imágenes RGB combinando los canales Y, U y V. Esto es útil para aplicaciones que requieren la conversión de espacio de color entre estos dos estándares.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `Y`       | La imagen de entrada del canal Y, que representa la información de luminancia. | IMAGEN | Sí | - |
| `U`       | La imagen de entrada del canal U, que representa la diferencia de color azul. | IMAGEN | Sí | - |
| `V`       | La imagen de entrada del canal V, que representa la diferencia de color rojo. | IMAGEN | Sí | - |

**Nota:** Los canales Y, U y V deben proporcionarse juntos y deben tener las mismas dimensiones para asegurar una conversión correcta.

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `output`    | La imagen RGB resultante después de la conversión YUV a RGB. | IMAGEN |

La imagen de salida tendrá las mismas dimensiones que las imágenes de entrada Y, U y V, pero con la información de color representada en el espacio de color RGB.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/es.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
