# Tripo P1: Texto a Modelo

Tripo P1 de texto a 3D. Este nodo genera un modelo 3D a partir de una descripción de texto usando la API Tripo P1. Está optimizado para crear mallas low-poly listas para juegos con topología estable, lo que lo hace adecuado para aplicaciones en tiempo real.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `modo_de_salida` | Controla si el modelo generado contiene solo geometría o también color/texturas PBR. "Geometry only" devuelve una malla sin textura. "Textured" agrega mapas de color/PBR y muestra las opciones de textura a continuación. | DYNAMIC_COMBO | Sí | `"Geometry only"`<br>`"Textured"` |
| `prompt` | La descripción textual del modelo 3D que deseas generar. Hasta 1024 caracteres. Obligatorio y no puede estar vacío. | STRING | Sí | Hasta 1024 caracteres |
| `prompt_negativo` | Una descripción textual de lo que no deseas en el modelo generado. Hasta 255 caracteres. Predeterminado: sin establecer. | STRING | No | Hasta 255 caracteres |
| `semilla_imagen` | Un valor semilla usado para controlar la aleatoriedad. Predeterminado: 42. | INT | No | 0 a 2147483647 |
| `límite_de_caras` | Cantidad objetivo de caras, 48-20000. -1 permite que Tripo elija de forma adaptativa. Predeterminado: -1. | INT | No | -1 a 20000 |
| `semilla_modelo` | Un valor semilla usado para controlar la aleatoriedad. Predeterminado: 42. | INT | No | 0 a 2147483647 |
| `auto_escala` | Escala la salida para aproximar metros del mundo real. Predeterminado: False. | BOOLEAN | No | True / False |
| `exportar_uv` | Desenvoltura UV durante la generación. Desactívalo para ejecuciones solo de geometría más rápidas. Predeterminado: True. | BOOLEAN | No | True / False |
| `comprimir_geometría` | Aplica compresión de geometría meshopt (EXT_meshopt_compression). Archivos más pequeños, pero la vista previa 3D de ComfyUI no puede mostrarlos; descomprime antes de editar. Predeterminado: False. | BOOLEAN | No | True / False |

### Entradas de solo geometría

No hay entradas adicionales disponibles cuando `output_mode` está establecido en `"Geometry only"`. Los parámetros relacionados con texturas no se envían a Tripo en este modo.

### Entradas con textura

Estas entradas solo aparecen cuando `output_mode` está establecido en `"Textured"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `pbr` | Incluye mapas PBR. Cuando está activado, la textura base también se activa forzosamente. Predeterminado: True. | BOOLEAN | Sí | True / False |
| `texture_quality` | Preajuste de calidad de textura. detailed = texturas HD, extreme = texturas 8K Ultra. Predeterminado: "standard". | COMBO | Sí | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Un valor semilla para la generación de texturas, usado para controlar la aleatoriedad. Predeterminado: 42. | INT | Sí | 0 a 2147483647 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `archivo_modelo` | El nombre de archivo del modelo generado; se conserva solo por compatibilidad hacia atrás. | STRING |
| `id_tarea_modelo` | El ID de tarea único para la solicitud de generación del modelo. | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `53a5573384294612b912558436e82f3481717d2ba3d50b73f1e40c3065aff2a0`
