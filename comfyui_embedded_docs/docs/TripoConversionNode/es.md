# Tripo: Convertir modelo

Este nodo convierte un modelo 3D de Tripo existente a otro formato de archivo 3D. Toma el ID de tarea de un modelo previamente creado o procesado por una operación de Tripo (como generación de modelos, rigging, retargeting o segmentación), envía una tarea de conversión a la API de Tripo, espera a que dicha tarea finalice y luego devuelve el archivo del modelo convertido.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `id_tarea_modelo_original` | ID de tarea del modelo de Tripo que se va a convertir. Debe provenir de una tarea anterior de Tripo, ya sea de generación de modelos, rigging, retargeting o segmentación. Si el ID falta o está vacío, el nodo genera un error. | STRING (ID de tarea de Tripo) | Sí | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `formato` | Formato de archivo de destino para el modelo 3D convertido. | COMBO | Sí | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `cuadrangular` | Convierte triángulos en cuadriláteros cuando está habilitado (predeterminado: False). | BOOLEAN | No | True o False |
| `límite_caras` | Número máximo de caras en el modelo convertido. Establece -1 para indicar que no hay límite (predeterminado: -1). | INT | No | -1 a 2000000 |
| `tamaño_textura` | Resolución de las texturas de salida en píxeles (predeterminado: 4096). | INT | No | 128 a 8192 |
| `formato_textura` | Formato de archivo utilizado para las texturas exportadas (predeterminado: JPEG). | COMBO | No | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | Fuerza la simetría del modelo cuando está habilitado (predeterminado: False). | BOOLEAN | No | True o False |
| `flatten_bottom` | Aplana la parte inferior del modelo cuando está habilitado (predeterminado: False). | BOOLEAN | No | True o False |
| `flatten_bottom_threshold` | Profundidad de aplanado utilizada con `flatten_bottom` (predeterminado: 0.01). Este valor solo se aplica cuando `flatten_bottom` está habilitado. | FLOAT | No | 0.01 a 1.0 |
| `pivot_to_center_bottom` | Mueve el punto de pivote al centro inferior del modelo cuando está habilitado (predeterminado: False). | BOOLEAN | No | True o False |
| `scale_factor` | Factor de escala aplicado al modelo convertido (predeterminado: 1.0). | FLOAT | No | 0.01 o más |
| `with_animation` | Mantiene el esqueleto y la animación de los modelos con rigging o retargeting (predeterminado: True). | BOOLEAN | No | True o False |
| `pack_uv` | Vuelve a empaquetar las coordenadas UV cuando está habilitado (predeterminado: False). | BOOLEAN | No | True o False |
| `bake` | Hornea los materiales avanzados en las texturas base para una mayor compatibilidad (predeterminado: True). | BOOLEAN | No | True o False |
| `part_names` | Lista separada por comas de nombres de partes del modelo para enviar a la conversión. Las entradas vacías se ignoran y los nombres duplicados se eliminan. Déjela vacía para omitir esta opción (predeterminado: vacío). | STRING | No | Lista de nombres de partes separada por comas |
| `fbx_preset` | Preajuste de compatibilidad FBX. `bake_scale` hornea la transformación de escala en la geometría (predeterminado: blender). | COMBO | No | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `export_vertex_colors` | Exporta los colores de vértice cuando está habilitado (predeterminado: False). | BOOLEAN | No | True o False |
| `export_orientation` | Eje frontal del modelo exportado. El ajuste predeterminado conserva el +x de Tripo (predeterminado: default). | COMBO | No | default<br>+x<br>-x<br>+y<br>-y |
| `animate_in_place` | Anima el modelo en su lugar cuando está habilitado (predeterminado: False). | BOOLEAN | No | True o False |

**Nota:** Excepto por `original_model_task_id` y `format`, todas las entradas son ajustes avanzados opcionales. Los ajustes que se dejan en sus valores predeterminados se omiten en la solicitud de conversión para que la API de Tripo utilice su comportamiento estándar. La entrada `flatten_bottom_threshold` solo tiene efecto cuando `flatten_bottom` está habilitado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_3d` | Modelo convertido en el formato solicitado. Tripo entrega el OBJ como un archivo ZIP (malla, material y texturas). | FILE_3D |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/es.md)

---
**Source fingerprint (SHA-256):** `5fd181d15025576083769e1ce31fb20cabb33096a01c67be50c3d9bb332739bf`
