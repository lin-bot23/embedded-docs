# Tripo: Convertir modelo

Este nodo convierte un modelo 3D de Tripo existente en otro formato de archivo 3D. Toma el ID de tarea de un modelo creado o procesado previamente por una operación de Tripo (como generación de modelos, rigging, retargeting o segmentación), envía una tarea de conversión a la API de Tripo, espera a que esa tarea finalice y luego devuelve el archivo del modelo convertido.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `id_tarea_modelo_original` | ID de tarea del modelo de Tripo que se va a convertir. Debe provenir de una tarea anterior de generación de modelos, rigging, retargeting o segmentación de Tripo. Si el ID falta o está vacío, el nodo lanza un error. | STRING | Sí | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `formato` | Formato de archivo de destino para el modelo 3D convertido. | COMBO | Sí | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `cuadrangular` | Convierte triángulos a quads cuando está habilitado (predeterminado: False). | BOOLEAN | No | True or False |
| `límite_caras` | Número máximo de caras en el modelo convertido. Establece -1 para sin límite (predeterminado: -1). | INT | No | -1 a 2000000 |
| `tamaño_textura` | Resolución de las texturas de salida en píxeles (predeterminado: 4096). | INT | No | 128 a 8192 |
| `formato_textura` | Formato de archivo utilizado para las texturas exportadas (predeterminado: JPEG). | COMBO | No | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | Fuerza que el modelo sea simétrico cuando está habilitado (predeterminado: False). | BOOLEAN | No | True or False |
| `flatten_bottom` | Aplana la parte inferior del modelo cuando está habilitado (predeterminado: False). | BOOLEAN | No | True or False |
| `flatten_bottom_threshold` | Profundidad de aplanado utilizada con `flatten_bottom` (predeterminado: 0.01). Este valor solo se aplica cuando `flatten_bottom` está habilitado. | FLOAT | No | 0.01 a 1.0 |
| `pivot_to_center_bottom` | Mueve el punto de pivote al centro inferior del modelo cuando está habilitado (predeterminado: False). | BOOLEAN | No | True or False |
| `scale_factor` | Factor de escala aplicado al modelo convertido (predeterminado: 1.0). | FLOAT | No | 0.01 y superior |
| `with_animation` | Conserva el esqueleto y la animación de los modelos con rigging o retargeting (predeterminado: True). | BOOLEAN | No | True or False |
| `pack_uv` | Reempaqueta las coordenadas UV cuando está habilitado (predeterminado: False). | BOOLEAN | No | True or False |
| `bake` | Hornea materiales avanzados en las texturas base para una mayor compatibilidad (predeterminado: True). | BOOLEAN | No | True or False |
| `part_names` | Lista de nombres de partes del modelo separados por comas para enviar a la conversión. Las entradas vacías se ignoran y los nombres duplicados se eliminan. Déjalo vacío para omitir esta opción (predeterminado: vacío). | STRING | No | Lista de nombres de partes separados por comas |
| `fbx_preset` | Preajuste de compatibilidad de FBX. bake_scale hornea la transformación de escala en la geometría (predeterminado: blender). | COMBO | No | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `export_vertex_colors` | Exporta los colores de vértices cuando está habilitado (predeterminado: False). | BOOLEAN | No | True or False |
| `export_orientation` | Eje frontal del modelo exportado. default mantiene el +x de Tripo (predeterminado: default). | COMBO | No | default<br>+x<br>-x<br>+y<br>-y |
| `animate_in_place` | Anima el modelo en su lugar cuando está habilitado (predeterminado: False). | BOOLEAN | No | True or False |

**Nota:** Excepto por `original_model_task_id` y `format`, todas las entradas son configuraciones avanzadas opcionales. La mayoría de las configuraciones que se dejan en sus valores predeterminados se omiten de la solicitud de conversión para que la API de Tripo pueda usar su comportamiento estándar. Las opciones `with_animation` y `bake` siempre se envían. `flatten_bottom_threshold` solo se aplica cuando `flatten_bottom` está habilitado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_3d` | Modelo convertido en el formato solicitado. Tripo entrega OBJ como un archivo ZIP (malla, material y texturas). | FILE_3D |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/es.md)

---
**Source fingerprint (SHA-256):** `b6be09bf6b1c5ccd6de5ae56ed28bfe1f0b81c1ca8ff61623e3094917c98d68a`
