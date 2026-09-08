# Block Sparse Attention

## Resumen

El nodo de Atención Esparsa por Bloques aplica un mecanismo de atención esparsa por bloques a un modelo ComfyUI, reduciendo el cálculo de atención permitiendo que cada bloque de consulta atienda solo un subconjunto seleccionado de bloques clave exactamente.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo ComfyUI al que aplicar la atención esparsa por bloques. | MODEL | Sí | N/A |
| `selection` | El método de selección para elegir qué bloques clave atender. | DYNAMIC_COMBO | Sí | Opciones: Sol-Attn (tau adaptativo), top-k (SLA), VSA (FastVideo) |
| `tau` | El umbral en sigmas de distribución de puntuaciones para la selección Sol-Attn (tau adaptativo). | FLOAT | No | predeterminado: 1.3, min: 0.0, max: 4.0, paso: 0.05 |
| `keep_percent` | El porcentaje de bloques clave que cada bloque de consulta mantiene exactamente para la selección top-k (SLA). | FLOAT | No | predeterminado: 10.0, min: 0.5, max: 95.0, paso: 0.5 |
| `start_percent` | El porcentaje del horario antes del cual el modelo utiliza atención densa. | FLOAT | No | predeterminado: 0.2, min: 0.0, max: 1.0, paso: 0.01 |
| `end_percent` | El porcentaje del horario después del cual el modelo utiliza atención densa. | FLOAT | No | predeterminado: 1.0, min: 0.0, max: 1.0, paso: 0.01 |
| `dense_blocks` | Una cadena que representa los bloques de transformador que siempre ejecutan atención densa. | STRING | No | predeterminado: "" |
| `min_tokens` | El número mínimo de tokens en una secuencia para el que el modelo utiliza atención densa. | INT | No | predeterminado: 12288, min: 0, max: 1 << 20, paso: 512 |
| `extra_tokens` | El número de tokens de alta puntuación adicionales que cada bloque de consulta atiende más allá de sus bloques seleccionados. | INT | No | predeterminado: 256, min: 0, max: 256, paso: 64 |
| `sink_conditioning` | Las filas de condicionamiento MiniMax-H3 a usar para el condicionamiento de sumidero. | COMBO | No | Opciones: exact_kv, exact_kv_and_rows, off |
| `verbose` | Si se debe activar el registro detallado. | BOOLEAN | No | predeterminado: Falso |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `model` | El modelo ComfyUI con la atención esparsa por bloques aplicada. | MODEL |

### Notas

- El parámetro `selection` determina cómo se eligen los bloques clave. Las opciones son:
  - Sol-Attn (tau adaptativo): Cada bloque de consulta atiende un subconjunto seleccionado de bloques clave basado en un umbral adaptativo.
  - top-k (SLA): Cada bloque de consulta mantiene un porcentaje fijo de bloques clave exactamente.
  - VSA (FastVideo): Cada bloque de consulta mantiene un porcentaje fijo de cubos de video exactamente, utilizando el mosaico de cubos y la rama gruesa de FastH3-VSA.
- El parámetro `dense_blocks` permite especificar los bloques de transformador que siempre ejecutan atención densa.
- El parámetro `min_tokens` establece el número mínimo de tokens en una secuencia para el que el modelo utiliza atención densa.
- El parámetro `extra_tokens` permite especificar el número de tokens de alta puntuación adicionales que cada bloque de consulta atiende más allá de sus bloques seleccionados.
- El parámetro `sink_conditioning` determina las filas de condicionamiento MiniMax-H3 a usar para el condicionamiento de sumidero.
- El parámetro `verbose` activa el registro detallado.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/es.md)

---
**Source fingerprint (SHA-256):** `6a27aee45593883f5958ae1aac74a2077362742a0fdf74fc9dbfd68eddc6d259`
