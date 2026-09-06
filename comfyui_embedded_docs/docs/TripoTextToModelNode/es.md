# Tripo: Texto a Modelo

Genera modelos 3D terminados a partir de una descripción de texto mediante la API de Tripo. El nodo espera a que finalice la generación y devuelve el archivo del modelo, opcionalmente con texturas y materiales PBR.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Descripción textual del modelo 3D a generar (multilínea). Este parámetro es obligatorio y no puede estar vacío. | STRING | Sí | - |
| `promoción_negativa` | Descripción textual de lo que se debe evitar en el modelo generado (multilínea). Hasta 255 caracteres. Solo se envía a la API cuando no está vacío. | STRING | No | Hasta 255 caracteres |
| `versión_del_modelo` | Versión del modelo de Tripo que se usará para la generación (por defecto: v3.1-20260211). | COMBO | No | Varias opciones disponibles |
| `estilo` | Estilo aplicado al modelo generado (por defecto: None). Tripo ya no lo admite y lo ignora; se conserva para flujos de trabajo antiguos. | COMBO | No | Varias opciones disponibles |
| `textura` | Indica si se generan mapas de textura. Desactivado devuelve geometría sin texturas e ignora `pbr` (por defecto: True). | BOOLEAN | No | true / false |
| `pbr` | Indica si se generan mapas de materiales PBR (color base, metalizado, rugosidad, normales). Requiere `texture`; cuando `texture` está desactivado, el nodo lo fuerza a desactivado e ignora su valor (por defecto: True). | BOOLEAN | No | true / false |
| `semilla_de_imagen` | Semilla utilizada en la etapa de generación de la imagen (por defecto: 42). | INT | No | 0 a 2147483647 |
| `semilla_del_modelo` | Semilla utilizada en la etapa de generación del modelo (por defecto: 42). | INT | No | 0 a 2147483647 |
| `semilla_de_textura` | Semilla utilizada en la etapa de generación de texturas (por defecto: 42). | INT | No | 0 a 2147483647 |
| `calidad_de_textura` | Calidad de las texturas generadas. detailed = texturas HD, extreme = texturas 8K Ultra (por defecto: standard). | COMBO | No | "standard"<br>"detailed"<br>"extreme" |
| `límite_de_caras` | Número máximo de caras. -1 permite que Tripo lo elija de forma adaptativa (alrededor de 1,4 millones de caras en el modo standard de v3.x y 2 millones en el modo detailed). Tripo lo limita silenciosamente: v2.5 hasta 500 000 y mallas quad hasta 150 000. (por defecto: -1) | INT | No | -1 a 2000000 |
| `cuadrante` | Salida de malla quad. Tripo entrega las mallas quad como FBX, por lo que el resultado llega a la salida FBX y la salida GLB permanece vacía. (por defecto: False) | BOOLEAN | No | true / false |
| `geometry_quality` | Calidad de la geometría generada (por defecto: standard). | COMBO | No | "standard"<br>"detailed" |
| `smart_low_poly` | Malla de baja poligonización con una topología limpia y de estilo artesanal (de 500 a 20 000 caras; quad de 500 a 10 000). Ideal para temas simples; los complejos pueden fallar. (por defecto: False) | BOOLEAN | No | true / false |
| `auto_size` | Escala los modelos con textura a su tamaño real en metros. Tripo almacena el tamaño como transformación de escena del modelo y lo aplica cuando el modelo se convierte, se le aplica rigging o retargeting; se ignora si no hay textura. (por defecto: True) | BOOLEAN | No | true / false |

**Notas:**

- El parámetro `prompt` es obligatorio: un prompt vacío provoca que el nodo lance un error.
- `pbr` requiere `texture`. Cuando `texture` está desactivado, el nodo fuerza `pbr` a desactivado e ignora su valor. `auto_size` tampoco tiene efecto sin `texture`.
- Cuando `smart_low_poly` está habilitado y `face_limit` se establece en un valor distinto de -1, el límite de caras debe estar entre 500 y 20 000 para la salida de triángulos, o entre 500 y 10 000 cuando `quad` está habilitado; de lo contrario, el nodo lanza un error.
- Cuando `quad` está habilitado, la malla quad generada se entrega como FBX, por lo que la salida FBX se completa y la salida GLB permanece vacía.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `archivo_de_modelo` | El archivo de modelo 3D generado, conservado únicamente por compatibilidad con versiones anteriores. | STRING |
| `id_de_tarea_de_modelo` | El identificador único de la tarea para el proceso de generación del modelo. | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. Vacío cuando `quad` está habilitado. | FILE3DGLB |
| `FBX` | El modelo 3D generado en formato FBX. Solo se completa cuando `quad` está habilitado. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `3f4bc09d125fedb6c30968f31804cfc7ec6d2f068a7c28d90b006137803020b0`
