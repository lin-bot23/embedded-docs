# Tripo: Retopología

Tripo: Retopology toma un modelo 3D de alta poligonización que fue generado por un nodo Tripo anterior y lo reconstruye como una versión de baja poligonización con topología limpia. Envía el modelo al servicio de retopología de Tripo, espera a que finalice la tarea, luego descarga el modelo terminado y expone su ID de tarea para que lo usen otros nodos Tripo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | ID de tarea del modelo de alta poligonización de origen. Acepta un ID de tarea de modelo de un nodo de generación de Tripo o un ID de tarea de segmentación de Tripo: Segment Model. | STRING | Sí | ID de tarea de Tripo |
| `face_limit` | Recuento objetivo de caras: 500-20,000 triángulos o 500-10,000 cuadriláteros. -1 permite que Tripo elija. (predeterminado: -1) | INT | Sí | -1 (automático)<br>500 a 20,000 (triángulos)<br>500 a 10,000 (cuadriláteros) |
| `quad` | Salida de malla de cuadriláteros. Tripo entrega las mallas de cuadriláteros como FBX, por lo que el resultado llega en la salida FBX y la salida GLB permanece vacía. (predeterminado: False) | BOOLEAN | Sí | True<br>False (predeterminado) |
| `bake` | Aplicar bake a las texturas de origen sobre la malla de baja poligonización. (predeterminado: True) | BOOLEAN | No | True (predeterminado)<br>False |
| `part_names` | Nombres de partes separados por comas de Tripo: Segment Model. Si está vacío, se procesa el modelo completo. (predeterminado: "") | STRING | No | Nombres de partes del modelo o vacío |

Nota: Cuando `face_limit` se establece en -1, Tripo decide el recuento de caras automáticamente. Cuando `quad` está habilitado, el límite máximo de caras es de 10,000 cuadriláteros en lugar de 20,000 triángulos, y el resultado se proporciona como FBX (la salida GLB permanece vacía). Cuando `part_names` está vacío, se procesa el modelo completo. Si `face_limit` es cualquier valor distinto de -1 y queda fuera del rango permitido, el nodo lanza un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `model_file` | Salida compatible con versiones anteriores que identifica el archivo de modelo completado. Los flujos de trabajo más recientes deberían usar las salidas GLB o FBX en su lugar. | STRING |
| `model task_id` | ID de tarea del resultado de retopología terminado. Se puede pasar a otros nodos Tripo para hacer referencia a este modelo. | STRING |
| `GLB` | El modelo de baja poligonización retopologizado en formato GLB. Vacío cuando `quad` está habilitado. | GLB FILE |
| `FBX` | El modelo de baja poligonización retopologizado en formato FBX. Solo se completa cuando `quad` está habilitado. | FBX FILE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/es.md)

---
**Source fingerprint (SHA-256):** `b0e967eb4987a70242b6cfce93f09e0caffb7f4bdd3e4f1439e68f33f9138bb5`
