# Tripo: Modelo de textura

El nodo Tripo: Texture model (Legacy) agrega texturas a un modelo 3D de Tripo existente a través de la API de Tripo. Toma el ID de tarea de un modelo creado por otro nodo de Tripo y devuelve un modelo GLB o FBX texturizado una vez finalizado el trabajo de texturizado. Puedes controlar los mapas de material, la calidad de textura, la alineación y la semilla, y guiar las texturas con un prompt de texto, una imagen de estilo o imágenes de referencia. Este nodo es una versión legacy de la herramienta de texturizado.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `id_de_tarea_del_modelo` | El ID de tarea de Tripo del modelo a texturizar. Acepta IDs de tarea de modelo y IDs de tarea de segmentación. | MODEL_TASK_ID, SEGMENT_TASK_ID | Sí | - |
| `textura` | Ignorado: este nodo siempre genera texturas. Se mantiene para flujos de trabajo anteriores. (predeterminado: True) | BOOLEAN | No | true<br>false |
| `pbr` | Mapas de material PBR (color base, metálico, rugosidad, normal); desactivado produce una textura de color plano. (predeterminado: True) | BOOLEAN | No | true<br>false |
| `semilla_de_textura` | Semilla aleatoria para la generación de texturas. (predeterminado: 42) | INT | No | 0 – 2147483647 |
| `calidad_de_textura` | Calidad de resolución de textura: detailed = texturas HD, extreme = texturas 8K Ultra. (predeterminado: "standard"). Costo aproximado: standard $0.10, detailed $0.20, extreme $0.30. | COMBO | No | "standard"<br>"detailed"<br>"extreme" |
| `alineación_de_textura` | Método usado para alinear las texturas generadas con el modelo. (predeterminado: "original_image") | COMBO | No | "original_image"<br>"geometry" |
| `texture_prompt` | Guía de texto opcional para el texturizado. Requerida en la práctica para modelos importados (Tripo: Import Model), que no tienen una imagen de origen de la cual inferir colores. No se puede combinar con imágenes de referencia. (predeterminado: "") | STRING | No | - |
| `model_version` | Modelo de texturizado: v3.0 para mallas generadas con v3.x, v2.5 para mallas generadas con v2.5. (predeterminado: v3.0_20250812) | COMBO | No | Múltiples opciones disponibles |
| `style_image` | Imagen de referencia para el estilo artístico de las texturas. Solo se usa junto con `texture_prompt`. | IMAGE | No | - |
| `referencia` | Imágenes de referencia que guían las texturas. No se puede combinar con `texture_prompt` ni con `style_image`. (predeterminado: "none") | DYNAMIC_COMBO | No | "none"<br>"image"<br>"multiview" |
| `part_names` | Nombres de partes separados por comas de Tripo: Segment Model a texturizar. Si está vacío, texturiza todas las partes. (predeterminado: "") | STRING | No | - |

### Entradas de referencia de `image`

Estas entradas están disponibles cuando `reference` se establece en `"image"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | Imagen de referencia única que deben seguir las texturas. | IMAGE | Sí | - |

### Entradas de referencia de `multiview`

Estas entradas están disponibles cuando `reference` se establece en `"multiview"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `image_front` | Vista frontal (0°). | IMAGE | Sí | - |
| `image_left` | Vista izquierda (90°). | IMAGE | Sí | - |
| `image_back` | Vista trasera (180°). | IMAGE | Sí | - |
| `image_right` | Vista derecha (270°). | IMAGE | Sí | - |

**Nota:** Los modos de referencia `"image"` y `"multiview"` no se pueden combinar con un `texture_prompt` no vacío ni con `style_image`. La entrada `style_image` requiere un `texture_prompt` no vacío. Cuando `texture_prompt` se deja vacío, el modelo de origen ya debe tener su propia imagen de origen (por ejemplo, modelos producidos por text-to-model, image-to-model, multiview-to-model o una tarea de texturizado anterior). Los modelos que no tienen imagen de origen — como los modelos importados, segmentados, completados o retopologizados — deben texturizarse con un `texture_prompt`; las imágenes de referencia solo se aceptan para modelos que la propia API de Tripo generó. La entrada `part_names` se puede dejar vacía para texturizar todas las partes.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `archivo_de_modelo` | El archivo de modelo generado (solo para compatibilidad con versiones anteriores). | STRING |
| `id_de_tarea_de_modelo` | El ID de la tarea de generación de texturas completada, utilizable como entrada para otros nodos de Tripo. | MODEL_TASK_ID |
| `GLB` | El modelo texturizado generado en formato GLB. Vacío cuando el origen es una malla de cuadriláteros o una importación FBX. | FILE3DGLB |
| `FBX` | El modelo texturizado generado en formato FBX. Tripo devuelve FBX para mallas de cuadriláteros e importaciones FBX; vacío en caso contrario. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/es.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`
