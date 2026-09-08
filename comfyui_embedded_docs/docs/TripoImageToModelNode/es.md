# Tripo: Imagen a Modelo

Genera modelos 3D sincrónicamente basándose en una única imagen mediante la API de Tripo. Proporcione una imagen de entrada y el nodo creará un modelo 3D terminado a partir de ella, con controles opcionales para la versión del modelo, la generación de texturas, el nivel de detalle y el formato de salida.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imagen` | La imagen de entrada utilizada para generar el modelo 3D. Debe proporcionarse una imagen; de lo contrario, el nodo mostrará un error. | IMAGE | Sí | - |
| `versión_modelo` | La versión del modelo que se usará para la generación. | COMBO | No | `"v1.4"`<br>`"v3.0"`<br>`"v3.5"`<br>`"v3.6"` |
| `estilo` | Ya no es compatible con Tripo y se ignora. Se conserva para flujos de trabajo antiguos. (predeterminado: `"None"`) | COMBO | No | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `textura` | Genera mapas de textura. Si está desactivado, devuelve solo geometría sin texturizar y omite `pbr`. (predeterminado: True) | BOOLEAN | No | True<br>False |
| `pbr` | Mapas de materiales PBR (color base, metálico, rugosidad, normal). Requiere `texture`. (predeterminado: True) | BOOLEAN | No | True<br>False |
| `semilla_modelo` | Semilla aleatoria para la generación del modelo. (predeterminado: 42) | INT | No | 0 a 2147483647 |
| `orientación` | Configuración de orientación para el modelo generado. (predeterminado: `"default"`) | COMBO | No | `"default"`<br>`"front"`<br>`"back"`<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `semilla_textura` | Semilla aleatoria para la generación de texturas. (predeterminado: 42) | INT | No | 0 a 2147483647 |
| `calidad_textura` | Nivel de calidad para la generación de texturas: `detailed` = texturas HD, `extreme` = texturas Ultra 8K. (predeterminado: `"standard"`) | COMBO | No | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `alineación_de_textura` | Método de alineación para el mapeado de texturas. (predeterminado: `"original_image"`) | COMBO | No | `"original_image"`<br>`"geometry"` |
| `límite_de_caras` | Número máximo de caras. -1 permite que Tripo elija adaptativamente (alrededor de 1.4M de caras en v3.x estándar, 2M en detallado). Tripo ajusta silenciosamente: v2.5 en 500,000, mallas quad en 150,000. (predeterminado: -1) | INT | No | -1 a 2000000 |
| `cuadrilátero` | Salida de malla quad. Tripo entrega las mallas quad como FBX, por lo que el resultado llega por la salida FBX y la salida GLB permanece vacía. (predeterminado: False) | BOOLEAN | No | True<br>False |
| `geometry_quality` | Nivel de calidad para la generación de geometría. (predeterminado: `"standard"`) | COMBO | No | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Malla low-poly con topología limpia y de estilo artesanal (500-20,000 caras, quad 500-10,000). Ideal para sujetos sencillos; los complejos pueden fallar. (predeterminado: False) | BOOLEAN | No | True<br>False |
| `auto_size` | Escala los modelos texturizados a su tamaño real en metros. Tripo guarda el tamaño como transformación de escena del modelo y lo incorpora cuando el modelo se convierte, se le aplica rigging o retargeting; se ignora si no hay textura. (predeterminado: True) | BOOLEAN | No | True<br>False |

Nota: Se requiere una `image`; si falta, el nodo lanza un RuntimeError. Cuando `texture` es False, el modelo contiene solo geometría sin texturizar y `pbr` se fuerza a False. Cuando `smart_low_poly` está habilitado, `face_limit` debe estar entre 500 y 20,000 para mallas triangulares, o entre 500 y 10,000 cuando `quad` también está habilitado; si el límite no es válido, el nodo lanza un ValueError. Establecer `face_limit` en -1 (el valor predeterminado) no envía ningún límite explícito de caras a la API, lo que permite que Tripo elija adaptativamente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `archivo_de_modelo` | El archivo de modelo 3D generado (solo por compatibilidad con versiones anteriores). | STRING |
| `id_de_tarea_de_modelo` | El ID de la tarea para el seguimiento del proceso de generación del modelo. | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. Vacío cuando `quad` está habilitado. | FILE3DGLB |
| `FBX` | El modelo 3D generado en formato FBX. Solo se completa cuando `quad` está habilitado. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `79ebe76234036e8284640d7eaeee3a1220975b8adc043994de7de0ee161ccd45`
