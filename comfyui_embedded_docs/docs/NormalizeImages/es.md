# Normalizar Imágenes

Este nodo ajusta los valores de píxeles de una imagen de entrada utilizando un proceso de normalización matemática. Restablece un valor medio especificado de cada píxel y luego divide el resultado por una desviación estándar especificada. Este es un paso de preprocesamiento común para preparar datos de imagen para otros modelos de aprendizaje automático. Si la imagen de entrada tiene un canal alfa, el canal alfa se pasa sin cambios, preservando la transparencia.

## Resumen

El nodo Normalizar Imágenes normaliza los colores de una imagen de entrada ajustando sus valores de píxeles basándose en un valor medio y una desviación estándar. Este proceso es útil para estandarizar datos de imagen antes de aplicar algoritmos de aprendizaje automático.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `image`   | La imagen de entrada que se debe normalizar. | IMAGEN | Sí | - |
| `media` | Valor medio para la normalización. | FLOAT | No | 0.0 - 1.0 (por defecto: 0.5) |
| `desviación estándar` | Desviación estándar para la normalización. | FLOAT | No | 0.001 - 1.0 (por defecto: 0.5) |

Los parámetros `mean` y `std` se utilizan para normalizar los valores de píxeles de la imagen de entrada. Los valores por defecto para ambos parámetros están establecidos en 0.5, lo que es una elección común para la normalización.

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `imágenes`     | La imagen resultante después de que se haya aplicado el proceso de normalización. | IMAGEN |

La salida del nodo Normalizar Imágenes es la imagen normalizada. Los valores de píxeles se ajustan según el valor medio y la desviación estándar especificados, y el canal alfa (si existe) se preserva.

## Nota

El nodo Normalizar Imágenes está diseñado para manejar cualquier tamaño de lote de imágenes, lo que lo hace adecuado para tareas de procesamiento por lotes.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/es.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
