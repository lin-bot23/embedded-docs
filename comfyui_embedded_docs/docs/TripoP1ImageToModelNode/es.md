# Tripo P1: Imagen a Modelo

Tripo P1: Image to Model convierte una única imagen 2D en un modelo 3D mediante la API de Tripo P1. Está optimizado para generar mallas de baja poligonización listas para juegos y permite elegir entre una malla solo de geometría o un modelo texturizado con mapas PBR. El modelo final se devuelve como un archivo GLB.

## Entradas

### Entradas comunes

Estos parámetros están siempre disponibles.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `output_mode` | Selecciona el tipo de resultado. "Geometry only" devuelve una malla sin texturizar; "Textured" añade color y mapas PBR y muestra ajustes adicionales de textura. | DYNAMIC_COMBO | Sí | `"Geometry only"`<br>`"Textured"` |
| `image` | La imagen 2D de origen utilizada para generar el modelo 3D. El nodo requiere una sola imagen y devuelve un error si no se proporciona ninguna. | IMAGE | Sí | - |
| `enable_image_autofix` | Preprocesa la imagen de entrada para mejorar la calidad de generación. (por defecto: False) | BOOLEAN | No | True<br>False |
| `face_limit` | Número de caras objetivo, entre 48 y 20000. -1 permite que Tripo lo seleccione de forma adaptativa. (por defecto: -1) | INT | No | -1 a 20000 |
| `model_seed` | Semilla utilizada para la generación de geometría, de modo que los resultados puedan reproducirse. (por defecto: 42) | INT | No | 0 a 2147483647 |
| `auto_size` | Escala la salida para que se aproxime a los metros del mundo real. (por defecto: False) | BOOLEAN | No | True<br>False |
| `export_uv` | Despliegue UV durante la generación. Se puede desactivar para acelerar las ejecuciones solo de geometría. (por defecto: True) | BOOLEAN | No | True<br>False |
| `compress_geometry` | Aplica compresión de geometría meshopt (EXT_meshopt_compression). Genera archivos más pequeños, pero la vista previa 3D de ComfyUI no puede mostrarlos; deben descomprimirse antes de editarlos. (por defecto: False) | BOOLEAN | No | True<br>False |

### Entradas de textura

Estos parámetros aparecen cuando `output_mode` está configurado como "Textured". El modo "Geometry only" no tiene parámetros adicionales.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `pbr` | Incluye mapas PBR. Cuando está activado, la textura base también se incluye forzosamente. (por defecto: True) | BOOLEAN | No | True<br>False |
| `texture_quality` | Nivel de resolución de textura. "detailed" = texturas HD, "extreme" = texturas 8K Ultra. (por defecto: "standard") | COMBO | No | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Prioriza la fidelidad visual respecto a la imagen de origen o la alineación con la geometría de la malla. (por defecto: "original_image") | COMBO | No | `"original_image"`<br>`"geometry"` |
| `orientation` | Rota la salida para que coincida con la imagen de origen. Solo se aplica cuando el resultado lleva textura. (por defecto: "default") | COMBO | No | `"default"`<br>`"align_image"` |
| `texture_seed` | Semilla utilizada para la generación de texturas, de modo que los resultados texturizados puedan reproducirse. (por defecto: 42) | INT | No | 0 a 2147483647 |

Nota: cuando `output_mode` es "Geometry only", la texturización está deshabilitada para la solicitud. En el modo "Textured", siempre se solicita una textura de color; desactivar `pbr` elimina los mapas PBR pero conserva la textura de color base, mientras que activar `pbr` fuerza también la textura base.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_file` | El resultado del modelo 3D generado. Se mantiene únicamente por compatibilidad con versiones anteriores. | STRING |
| `model task_id` | El ID de tarea único devuelto por la API de Tripo para el trabajo de generación completado. | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `db5dc76518a4efcd28d388dc00ad0810f619481482f20fa456c4ff2478192aa3`
