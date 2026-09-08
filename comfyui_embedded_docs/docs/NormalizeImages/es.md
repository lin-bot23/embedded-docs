# Normalizar Imágenes

Este nodo ajusta los valores de píxeles de una imagen de entrada mediante un proceso matemático de normalización. Resta un valor medio especificado a cada píxel y luego divide el resultado por una desviación estándar especificada. Este es un paso común de preprocesamiento para preparar datos de imagen para otros modelos de aprendizaje automático. Si la imagen de entrada tiene un canal alfa, este se mantiene sin cambios para preservar la transparencia.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada que se va a normalizar. | IMAGE | Sí | - |
| `media` | Valor medio para la normalización (por defecto: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `desviación estándar` | Desviación estándar para la normalización (por defecto: 0.5). | FLOAT | No | 0.001 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `imágenes` | La imagen resultante después de aplicar el proceso de normalización. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/es.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842d1e56d478b89e87c1d014fcaad01894a7a2f4a21fa17b83f`
