# Backend de atención del modelo

## Resumen

El nodo ModelAttentionBackend permite seleccionar una implementación de atención densa para un modelo. Este nodo parchea el modelo con el backend de atención seleccionado, que puede ser la atención de PyTorch o la atención de Comfy Kitchen cuando esté disponible. Este nodo es especialmente útil cuando la atención esparsa está inactiva o no es compatible, asegurando que el modelo opere con el mecanismo de atención densa especificado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | El modelo que será parcheado con el backend de atención seleccionado. | MODELO | Sí |  |
| `atención` | El backend de atención densa a aplicar al modelo. Las opciones disponibles son "atención de PyTorch" y "atención de Comfy Kitchen" si la última está disponible en el entorno. | STRING | Sí | "atención de PyTorch"<br> "atención de Comfy Kitchen" (cuando esté disponible) |

- La opción "atención de Comfy Kitchen" utiliza atención cuantizada en INT8 y es compatible solo con GPUs Nvidia y AMD.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `model` | El modelo de entrada con el backend de atención seleccionado aplicado. | MODELO |

## Nota

- Si el backend de atención seleccionado no está disponible, el nodo se fallback a utilizar la atención de PyTorch y registrará una advertencia.
- El nodo ModelAttentionBackend es experimental y puede estar sujeto a cambios en futuras versiones.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/es.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
