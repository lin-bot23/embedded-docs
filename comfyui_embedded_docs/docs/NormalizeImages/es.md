# Normalizar Imágenes

Este nodo ajusta los valores de píxel de una imagen de entrada mediante un proceso de normalización matemática. Resta un valor medio específico a cada píxel y luego divide el resultado por una desviación estándar especificada. Este es un paso de preprocesamiento común para preparar datos de imagen para otros modelos de aprendizaje automático.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada que se va a normalizar. | IMAGE | Sí | - |
| `media` | Valor medio para la normalización (predeterminado: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `desviación estándar` | Desviación estándar para la normalización (predeterminado: 0.5). | FLOAT | No | 0.001 - 1.0 |

Nota: Cuando la imagen de entrada incluye un canal alfa (transparencia), el canal alfa no se normaliza. Se mantiene sin cambios en la salida porque el alfa almacena transparencia en lugar de color.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `imágenes` | La imagen resultante después de aplicar el proceso de normalización. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/es.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
