# Atención dispersa por bloques del modelo

## Resumen

El nodo de Atención Esparsa de Bloque modifica un modelo de ComfyUI para aplicar un mecanismo de atención esparsa de bloque. Este mecanismo reduce la carga computacional permitiendo que cada bloque de consulta se centre en un subconjunto de bloques clave, en lugar de atender a todos los posibles bloques, lo cual es particularmente beneficioso para secuencias largas.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo de ComfyUI al que aplicar la atención esparsa de bloque. | MODEL | Sí | N/A |
| `selection` | El método utilizado para determinar qué bloques clave atender. | DYNAMIC_COMBO | Sí | Opciones: sol-attn (tau adaptativo), sla (top-k), vsa (Atención Esparsa de Video) |
| `tau` | El umbral en sigmas de distribución de puntuaciones para el método sol-attn. | FLOAT | No | predeterminado: 1.3, mínimo: 0.0, máximo: 4.0, paso: 0.05 |
| `keep_percent` | El porcentaje de bloques clave que cada bloque de consulta mantiene exactamente para el método sla. | FLOAT | No | predeterminado: 10.0, mínimo: 0.5, máximo: 95.0, paso: 0.5 |
| `start_percent` | El punto porcentual cuando comienza la atención esparsa. | FLOAT | No | predeterminado: 0.2, mínimo: 0.0, máximo: 1.0, paso: 0.01 |
| `end_percent` | El punto porcentual cuando termina la atención esparsa. | FLOAT | No | predeterminado: 1.0, mínimo: 0.0, máximo: 1.0, paso: 0.01 |
| `dense_blocks` | Una cadena que representa los bloques del transformador que siempre ejecutan atención densa. | STRING | No | predeterminado: "" |
| `min_tokens` | El número mínimo de tokens en una secuencia para el que el modelo utiliza atención densa. | INT | No | predeterminado: 12288, mínimo: 0, máximo: 1 << 20, paso: 512 |
| `extra_tokens` | El número de tokens de alta puntuación adicionales a los que cada bloque de consulta debe prestar atención más allá de sus bloques seleccionados. | INT | No | predeterminado: 256, mínimo: 0, máximo: 256, paso: 64 |
| `sink_conditioning` | Las filas de condicionamiento MiniMax-H3 a usar para el condicionamiento de sumidero. | COMBO | No | Opciones: exact_kv, exact_kv_and_rows, off |
| `verbose` | Habilita el registro detallado. | BOOLEAN | No | predeterminado: Falso |

### Notas

- El parámetro `selection` le permite elegir entre diferentes métodos para seleccionar bloques clave:
  - `sol-attn`: Utiliza un umbral adaptativo para seleccionar bloques clave basado en la distribución de puntuaciones.
  - `sla`: Mantiene un porcentaje fijo de los bloques clave de mayor puntuación.
  - `vsa`: Aplica Atención Esparsa de Video, que utiliza mosaico de cubo 3D de video y una rama de atención gruesa aprendida.
- El parámetro `dense_blocks` puede utilizarse para especificar los bloques del transformador que deben utilizar siempre atención densa.
- El parámetro `min_tokens` establece el número mínimo de tokens en una secuencia para el que se utiliza atención densa.
- El parámetro `extra_tokens` permite especificar el número adicional de tokens de alta puntuación a los que cada bloque de consulta debe prestar atención.
- El parámetro `sink_conditioning` es relevante solo para modelos MiniMax-H3 y determina cómo se manejan las filas de condicionamiento.
- El parámetro `verbose` habilita el registro detallado, lo cual puede ser útil para la depuración.

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `model` | El modelo de ComfyUI con la atención esparsa de bloque aplicada. | MODEL |

### Restricciones y Limitaciones

- El método `sol-attn` requiere un valor de `tau` entre 0.0 y 4.0.
- El método `sla` requiere un valor de `keep_percent` entre 0.5 y 95.0.
- El método `vsa` es compatible solo con modelos MiniMax-H3 y requiere que el modelo tenga una capa `to_gate_compress`.
- El parámetro `min_tokens` debe ser un entero no negativo (con 0, toda la atención permanece densa).
- El parámetro `extra_tokens` debe ser un entero no negativo.
- Las opciones de `sink_conditioning` solo son aplicables a modelos MiniMax-H3.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/es.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
