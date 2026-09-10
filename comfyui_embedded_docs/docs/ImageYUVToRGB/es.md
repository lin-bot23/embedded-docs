# ImageYUVToRGB

El nodo ImageYUVToRGB convierte imágenes en espacio de color YUV a espacio de color RGB. Toma tres imágenes de entrada separadas que representan los componentes Y (luminancia), U (proyección de azul) y V (proyección de rojo) y las combina en una única imagen RGB.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `Y` | Imagen de entrada del componente Y (luminancia) | IMAGE | Sí | - |
| `U` | Imagen de entrada del componente U (proyección de azul) | IMAGE | Sí | - |
| `V` | Imagen de entrada del componente V (proyección de rojo) | IMAGE | Sí | - |

**Nota:** Las tres imágenes de entrada (Y, U y V) deben proporcionarse juntas y deben tener dimensiones compatibles para una conversión adecuada.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | La imagen RGB convertida | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/es.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
