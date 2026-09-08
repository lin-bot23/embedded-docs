# Tripo P1: Texto a Modelo

Este nodo genera un modelo 3D a partir de una descripción de texto mediante la API Tripo P1. Está optimizado para crear mallas de baja poligonación (low-poly) y listas para juegos, con una topología estable, lo que lo hace adecuado para aplicaciones en tiempo real.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `modo_de_salida` | Controla si el modelo generado contiene solo geometría o también texturas/color y mapas PBR. Si se selecciona "Textured", aparecen entradas de textura debajo. "Geometry only" devuelve una malla sin texturas; "Textured" añade mapas de color/PBR. | DYNAMIC_COMBO | Sí | `"Geometry only"`<br>`"Textured"` |
| `prompt` | La descripción de texto del modelo 3D que deseas generar. Hasta 1024 caracteres. | STRING | Sí | Hasta 1024 caracteres |
| `prompt_negativo` | Descripción de texto que indica qué no se desea en el modelo generado. Hasta 255 caracteres. | STRING | No | Hasta 255 caracteres |
| `semilla_imagen` | Valor de semilla para la generación de imágenes, utilizado para controlar la aleatoriedad. Predeterminado: 42. | INT | No | 0 a 2147483647 |
| `límite_de_caras` | Número de caras objetivo, entre 48 y 20000. Un valor de -1 permite que Tripo elija de forma adaptativa. Predeterminado: -1. | INT | No | -1 a 20000 |
| `semilla_modelo` | Valor de semilla para la generación del modelo, utilizado para controlar la aleatoriedad. Predeterminado: 42. | INT | No | 0 a 2147483647 |
| `auto_escala` | Escala la salida para aproximarse a metros del mundo real. Predeterminado: False. | BOOLEAN | No | True / False |
| `exportar_uv` | Realiza el desplegado UV durante la generación. Desactívalo para ejecuciones de solo geometría más rápidas. Predeterminado: True. | BOOLEAN | No | True / False |
| `comprimir_geometría` | Aplica compresión de geometría meshopt (EXT_meshopt_compression). Archivos más pequeños, pero la vista previa 3D de ComfyUI no puede mostrarlos; descomprímelos antes de editar. Predeterminado: False. | BOOLEAN | No | True / False |

### Entradas de solo geometría

No hay entradas adicionales disponibles cuando `output_mode` se establece en `"Geometry only"`. En este modo, los parámetros relacionados con texturas no se envían a Tripo.

### Entradas del modo Textured

Estas entradas solo aparecen cuando `output_mode` se establece en `"Textured"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `pbr` | Incluye mapas PBR. Cuando está activado, la textura base también se activa de forma forzada. Predeterminado: True. | BOOLEAN | Sí | True / False |
| `texture_quality` | Ajuste de calidad de textura. detailed = texturas HD, extreme = texturas 8K Ultra. Predeterminado: "standard". | COMBO | Sí | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Valor de semilla para la generación de texturas, utilizado para controlar la aleatoriedad. Predeterminado: 42. | INT | Sí | 0 a 2147483647 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `archivo_modelo` | La ruta de archivo del modelo 3D generado, conservada únicamente por compatibilidad inversa. | STRING |
| `id_tarea_modelo` | El ID único de tarea para la solicitud de generación del modelo. | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `63781a990f892e6b1f241179039d1fb24778ba7aa7dccda7d14557cbf190b712`
