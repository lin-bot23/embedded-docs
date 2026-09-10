# Pixal3DConditioning

Este nodo prepara el acondicionamiento de imagen para el proceso de generación 3D de Trellis2. Extrae características visuales de la imagen de entrada con un modelo de visión DINOv3 en dos resoluciones, las organiza en mapas de características por etapa (opcionalmente mejorados con un modelo NAF) y las combina con los datos de cámara derivados del campo de visión horizontal. Genera un par de acondicionamientos positivo y negativo, donde el negativo utiliza características puestas a cero para la guía sin clasificador.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Sí | — |
| `imagen` | Imagen preprocesada de ImageCropToMask (pad_factor=1.1 para Pixal3D). | IMAGE | Sí | — |
| `camera_angle_x` | Campo de visión horizontal en grados (nombre visible: fov). Conecta un MoGeGeometryToFOV (axis='horizontal', unit='degrees') para obtener un FoV por imagen (coincide con el valor predeterminado del nodo anterior). Valor predeterminado: 49.13. | FLOAT | Sí | 1.0 – 170.0 |

Nota: El valor de `camera_angle_x` se convierte internamente a radianes y se utiliza para calcular la distancia de la cámara para la matriz de transformación de proyección. Cuando el modelo de visión suministrado incluye un componente NAF, el nodo produce además mapas de características de alta resolución para las etapas de forma y textura.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positivo` | Acondicionamiento positivo que contiene los mapas de características derivados de la imagen y los datos de proyección para la generación de Trellis2. | CONDITIONING |
| `negativo` | Acondicionamiento negativo con tensores de características puestos a cero, utilizado para la guía sin clasificador. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/es.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
