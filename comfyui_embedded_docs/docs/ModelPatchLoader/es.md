# Cargador de Parches de Modelo

El nodo ModelPatchLoader carga un archivo de parche de modelo desde la carpeta `model_patches` y lo prepara para usarlo en un flujo de trabajo. Detecta automáticamente el tipo de parche contenido en el archivo, construye la arquitectura correspondiente, carga los pesos guardados y envuelve todo en un model patcher para que pueda aplicarse a otros modelos. Admite muchos formatos de parche especializados, incluidas ramas adicionales de ControlNet, modelos de incrustación de características (*feature embedder*), adaptadores y módulos similares.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `nombre` | El nombre del archivo del parche de modelo que se cargará desde el directorio `model_patches`. Seleccione uno de los archivos de parche disponibles en la lista. | COMBO | Sí | Lista generada dinámicamente de todos los archivos de parche de modelo encontrados en la carpeta `model_patches` |

Nota: Este nodo está marcado como experimental. El tipo de parche se detecta automáticamente a partir del contenido del archivo, por lo que no se requiere ninguna selección manual de tipo.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `MODEL_PATCH` | El parche de modelo cargado envuelto en un `ModelPatcher`, listo para aplicarse a un modelo en el flujo de trabajo | MODEL_PATCH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/es.md)

---
**Source fingerprint (SHA-256):** `069f40b1f108ecd74fc58c12aa2f74edff07f743aa1ed6352ff7bcf0c39341d4`
