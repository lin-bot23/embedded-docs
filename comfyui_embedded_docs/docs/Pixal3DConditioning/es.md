# Pixal3DConditioning

```markdown
# Pixal3DConditioning

## Resumen

El nodo Pixal3DConditioning está diseñado para preparar la condición de imágenes para el flujo de generación 3D de Trellis2. Utiliza el modelo de visión DINOv3 para extraer características visuales de la imagen de entrada en dos resoluciones. Estas características se organizan en mapas de características por etapa, que pueden mejorarse opcionalmente con un modelo NAF. El nodo también incorpora datos de cámara derivados del campo de visión horizontal para calcular la matriz de transformación de proyección. Produce una condición positiva que incluye los mapas de características derivados de la imagen y los datos de proyección, así como una condición negativa con tensores de características cerosos para la guía sin clasificador.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | El modelo ClipVision DINOv3 ViT-L/16 utilizado para la extracción de características. | CLIP_VISION | Sí | — |
| `imagen` | La imagen preprocesada del nodo ImageCropToMask, destinada para Pixal3D con un factor de relleno de 1.1. | IMAGE | Sí | — |
| `camera_angle_x` | El campo de visión horizontal en grados. Este parámetro puede conectarse a un nodo MoGeGeometryToFOV para un campo de visión por imagen. Valor predeterminado: 49.13. | FLOAT | Sí | 1.0 – 170.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `positivo` | La salida de condición positiva que contiene los mapas de características derivados de la imagen y los datos de proyección para la generación de Trellis2. | CONDITIONING |
| `negativo` | La salida de condición negativa con tensores de características cerosos, utilizada para la guía sin clasificador. | CONDITIONING |

Nota: El valor de `camera_angle_x` se convierte internamente a radianes y se utiliza para calcular la distancia de la cámara para la matriz de transformación de proyección. Cuando el modelo de visión proporcionado incluye un componente NAF, el nodo también produce mapas de características de alta resolución para las etapas de forma y textura.
```

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/es.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
