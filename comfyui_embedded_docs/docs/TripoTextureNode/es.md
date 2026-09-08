# Tripo: Modelo de textura

El nodo TripoTextureNode agrega texturas a un modelo 3D de Tripo existente mediante la API de Tripo. Toma el ID de tarea de un modelo creado por otro nodo de Tripo y devuelve un modelo texturizado en GLB o FBX cuando finaliza la tarea de texturizado. Puede controlar los mapas de materiales, la calidad de la textura, la alineación, la semilla y guiar las texturas con una indicación de texto, una imagen de estilo o imágenes de referencia.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `id_de_tarea_del_modelo` | El ID de tarea de Tripo del modelo a texturizar. Acepta IDs de tarea de modelo y de segmentación. | MODEL_TASK_ID | Sí | - |
| `textura` | Se ignora: este nodo siempre genera texturas. Se conserva para flujos de trabajo antiguos. (por defecto: True) | BOOLEAN | No | true<br>false |
| `pbr` | Mapas de materiales PBR (color base, metalizado, rugosidad, normal). Desactivado, produce una textura de color plano. (por defecto: True) | BOOLEAN | No | true<br>false |
| `semilla_de_textura` | Semilla aleatoria para la generación de texturas. Usar la misma semilla con las mismas entradas produce el mismo resultado. (por defecto: 42) | INT | No | 0 – 2147483647 |
| `calidad_de_textura` | Calidad de resolución de textura: detailed = texturas HD, extreme = texturas 8K Ultra. (por defecto: "standard"). Costo aproximado: standard $0.10, detailed $0.20, extreme $0.30. | COMBO | No | "standard"<br>"detailed"<br>"extreme" |
| `alineación_de_textura` | Método utilizado para alinear las texturas generadas con el modelo. (por defecto: "original_image"). | COMBO | No | "original_image"<br>"geometry" |
| `texture_prompt` | Indicación de texto opcional para el texturizado. En la práctica, es necesaria para modelos importados (Tripo: Import Model), que no tienen una imagen de origen de la que inferir colores. No puede combinarse con imágenes de referencia. (por defecto: "") | STRING | No | - |
| `model_version` | Modelo de texturizado: v3.0 para mallas generadas con v3.x, v2.5 para mallas generadas con v2.5. (por defecto: la versión más reciente de v3.0) | COMBO | No | Múltiples opciones disponibles |
| `style_image` | Imagen de referencia para el estilo artístico de las texturas. Solo se usa junto con `texture_prompt`. | IMAGE | No | - |
| `referencia` | Imágenes de referencia que guían las texturas. No puede combinarse con `texture_prompt` ni con `style_image`. (por defecto: "none") | DYNAMIC_COMBO | No | "none"<br>"image"<br>"multiview" |
| `part_names` | Nombres de piezas separados por comas de Tripo: Segment Model para texturizar. Si se deja vacío, se texturizan todas las piezas. (por defecto: "") | STRING | No | - |

### Entradas de referencia "image"

Estas entradas están disponibles cuando `reference` se define como `"image"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | Imagen de referencia única que deben seguir las texturas. | IMAGE | No | - |

### Entradas de referencia "multiview"

Estas entradas están disponibles cuando `reference` se define como `"multiview"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `image_front` | Vista frontal (0°). | IMAGE | No | - |
| `image_left` | Vista izquierda (90°). | IMAGE | No | - |
| `image_back` | Vista trasera (180°). | IMAGE | No | - |
| `image_right` | Vista derecha (270°). | IMAGE | No | - |

**Nota:** Los modos de referencia `"image"` y `"multiview"` no se pueden combinar con un `texture_prompt` no vacío ni con `style_image`. La entrada `style_image` requiere un `texture_prompt` no vacío. Cuando `texture_prompt` se deja vacío, el modelo de origen ya debe tener su propia imagen de origen (por ejemplo, modelos generados mediante texto a modelo, imagen a modelo, multivista a modelo o una tarea de texturizado anterior). Los modelos que no tienen imagen de origen — como los modelos importados, segmentados, completados o retopologizados — deben texturizarse con un `texture_prompt`; las imágenes de referencia solo se aceptan para modelos generados por la propia API de Tripo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `archivo_de_modelo` | El archivo de modelo generado (solo por compatibilidad hacia atrás). | STRING |
| `id_de_tarea_de_modelo` | El ID de la tarea de generación de texturas completada, utilizable como entrada para otros nodos de Tripo. | MODEL_TASK_ID |
| `GLB` | El modelo texturizado generado en formato GLB. Vacío cuando el modelo de origen es una malla de cuadriláteros o una importación FBX. | FILE3DGLB |
| `FBX` | El modelo texturizado generado en formato FBX. Tripo devuelve FBX para mallas de cuadriláteros e importaciones FBX; vacío en caso contrario. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/es.md)

---
**Source fingerprint (SHA-256):** `815c22a9d8f4785ef5219789e0f2eee804776ec7e4752099ec0db0a2b5ad4bb2`
