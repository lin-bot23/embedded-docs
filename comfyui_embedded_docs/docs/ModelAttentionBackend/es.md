# Backend de atención del modelo

Este nodo selecciona el backend de atención densa que un modelo utiliza para sus cálculos de atención. Clona el modelo dado, aplica el backend elegido y devuelve el clon parcheado. Cuando se usa con Block Sparse Attention, este backend se utiliza siempre que la atención dispersa esté inactiva o no sea compatible. Si el backend seleccionado no está disponible, el nodo recurre automáticamente a la atención de PyTorch.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo a parchear. | MODEL | Sí |  |
| `atención` | El backend de atención densa a aplicar (predeterminado: "pytorch attention"). La atención de Comfy Kitchen utiliza atención INT8 cuantizada y está disponible solo en GPU de Nvidia y AMD. Si el backend seleccionado no está disponible, se utiliza la atención de PyTorch como respaldo. | COMBO | Sí | "pytorch attention"<br>"comfy kitchen attention" |

Nota: La opción "comfy kitchen attention" solo aparece cuando el módulo de atención INT8 de Comfy Kitchen está disponible en el entorno actual.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model` | Un clon del modelo de entrada con el backend de atención seleccionado aplicado. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/es.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
