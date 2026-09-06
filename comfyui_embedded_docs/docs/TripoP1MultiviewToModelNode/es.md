# Tripo P1: Multivista a Modelo

Este nodo genera un modelo 3D a partir de dos a cuatro imágenes de referencia de un objeto o personaje. Proporcione la vista frontal junto con cualquier combinación de vistas izquierda, posterior y derecha, y el nodo devuelve el sujeto reconstruido como una malla GLB.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `image` | Vista frontal (0°). Obligatoria. | IMAGE | Sí | - |
| `image_left` | Vista izquierda (90°), es decir, el lado izquierdo del sujeto. | IMAGE | No | - |
| `image_back` | Vista posterior (180°). | IMAGE | No | - |
| `image_right` | Vista derecha (270°), es decir, el lado derecho del sujeto. | IMAGE | No | - |
| `output_mode` | Elija el tipo de modelo a generar. "Geometry only" devuelve una malla sin textura. "Textured" añade mapas de color/PBR. | DYNAMIC_COMBO | Sí | "Geometry only"<br>"Textured" |
| `face_limit` | Número de caras objetivo, de 48 a 20000. -1 permite que Tripo lo elija adaptativamente. (predeterminado: -1) | INT | No | -1 a 20000 |
| `model_seed` | Semilla para la generación reproducible de modelos. (predeterminado: 42) | INT | No | 0 a 2147483647 |
| `auto_size` | Escala la salida para aproximarse a metros del mundo real. (predeterminado: False) | BOOLEAN | No | True<br>False |
| `export_uv` | Desenvolvimiento UV durante la generación. Desactívelo para ejecuciones más rápidas solo de geometría. (predeterminado: True) | BOOLEAN | No | True<br>False |
| `compress_geometry` | Aplica compresión de geometría meshopt (EXT_meshopt_compression). Archivos más pequeños, pero la vista previa 3D de ComfyUI no puede mostrarlos; descomprímalos antes de editarlos. (predeterminado: False) | BOOLEAN | No | True<br>False |

### Entradas de Geometry only

No se muestran entradas adicionales para este modo. El modelo generado se devuelve sin textura.

### Entradas de Textured

Estas entradas aparecen cuando `output_mode` se establece en `"Textured"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `pbr` | Incluye mapas PBR. Al activarlo, la textura base también se fuerza a activarse. (predeterminado: True) | BOOLEAN | Sí | True<br>False |
| `texture_quality` | Nivel de calidad de textura. `detailed` = texturas HD, `extreme` = texturas Ultra 8K. (predeterminado: "standard") | COMBO | Sí | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Prioriza la fidelidad visual a la imagen de origen, o la alineación con la geometría de la malla. (predeterminado: "original_image") | COMBO | Sí | "original_image"<br>"geometry" |
| `orientation` | Rota la salida para que coincida con la imagen de origen. Solo se aplica cuando hay textura. (predeterminado: "default") | COMBO | Sí | "default"<br>"align_image" |
| `texture_seed` | Semilla utilizada para la generación de texturas. (predeterminado: 42) | INT | Sí | 0 a 2147483647 |

**Nota:** Debe proporcionar al menos 2 imágenes: la vista frontal (`image`) más al menos una de las otras vistas (`image_left`, `image_back` o `image_right`). Si se proporcionan menos de 2 imágenes, el nodo generará un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `model_file` | El nombre del archivo del modelo GLB generado (solo para compatibilidad hacia atrás). | STRING |
| `model_task_id` | El ID de tarea único para esta solicitud de generación de modelo. | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `c26bf9d46f6b95ec57e4eb663cb6c602035c3ad00682e7f9622ce575ff54d228`
