# Tripo: Multivista a Modelo

Este nodo genera modelos 3D de forma síncrona mediante la API de Tripo procesando hasta cuatro imágenes que muestran diferentes vistas de un objeto (frontal, izquierda, trasera, derecha). Requiere una imagen frontal y al menos una vista adicional (izquierda, trasera o derecha) para construir el modelo 3D. La textura, el material PBR, la calidad de la geometría y el formato de salida se pueden controlar desde el nodo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imagen` | Imagen de la vista frontal del objeto. | IMAGE | Sí | - |
| `imagen_izquierda` | Imagen de la vista izquierda del objeto. | IMAGE | No | - |
| `imagen_posterior` | Imagen de la vista trasera del objeto. | IMAGE | No | - |
| `imagen_derecha` | Imagen de la vista derecha del objeto. | IMAGE | No | - |
| `versión_del_modelo` | La versión del modelo a utilizar para la generación. | COMBO | No | Múltiples opciones disponibles |
| `orientación` | Configuración de orientación para el modelo 3D (predeterminado: `"default"`). | COMBO | No | Múltiples opciones disponibles |
| `textura` | Generar mapas de textura. Desactivado devuelve geometría sin texturizar e ignora PBR. (predeterminado: True) | BOOLEAN | No | - |
| `pbr` | Mapas de material PBR (color base, metálico, rugosidad, normal). Requiere textura. (predeterminado: True) | BOOLEAN | No | - |
| `semilla_del_modelo` | Semilla aleatoria para la generación del modelo (predeterminado: 42). | INT | No | 0 a 2,147,483,647 |
| `semilla_de_textura` | Semilla aleatoria para la generación de textura (predeterminado: 42). | INT | No | 0 a 2,147,483,647 |
| `calidad_de_textura` | Nivel de calidad para la generación de textura (predeterminado: `"standard"`). `"detailed"` = texturas HD, `"extreme"` = texturas Ultra 8K. | COMBO | No | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `alineación_de_textura` | Método utilizado para alinear las texturas al modelo (predeterminado: `"original_image"`). | COMBO | No | `"original_image"`<br>`"geometry"` |
| `límite_de_caras` | Número máximo de caras. -1 permite que Tripo elija de forma adaptativa (aproximadamente 1,4 M de caras en v3.x estándar, 2 M en detallado). Tripo limita silenciosamente: v2.5 a 500,000, mallas quad a 150,000. (predeterminado: -1) | INT | No | -1 a 2,000,000 |
| `cuadrilátero` | Salida de malla quad. Tripo entrega las mallas quad como FBX, por lo que el resultado llega en la salida FBX y la salida GLB permanece vacía. (predeterminado: False) | BOOLEAN | No | - |
| `geometry_quality` | Nivel de calidad para la generación de geometría (predeterminado: `"standard"`). | COMBO | No | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Malla low-poly con topología limpia de estilo artesanal (500-20,000 caras, quad 500-10,000). Ideal para objetos simples; los complejos pueden fallar. (predeterminado: False) | BOOLEAN | No | - |
| `auto_size` | Escala los modelos texturizados a su tamaño real en metros. Tripo almacena el tamaño como la transformación de escena del modelo y lo integra cuando el modelo se convierte, se le aplica rig o se le hace retargeting; se ignora sin textura. (predeterminado: False) | BOOLEAN | No | - |

**Nota:** La imagen frontal (`image`) siempre es obligatoria, y también debe proporcionarse al menos una de `image_left`, `image_back` o `image_right`. Desactivar `texture` desactiva automáticamente `pbr` también, ya que `pbr` requiere textura. Cuando `smart_low_poly` está habilitado y `face_limit` no se deja en -1, `face_limit` debe estar entre 500 y 20,000 para mallas de triángulos o entre 500 y 10,000 para mallas quad.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `archivo_de_modelo` | Ruta de archivo o identificador del modelo 3D generado (solo por compatibilidad con versiones anteriores). | STRING |
| `id_de_tarea_de_modelo` | Identificador de tarea para el seguimiento del proceso de generación del modelo. | MODEL_TASK_ID |
| `GLB` | El archivo de modelo 3D generado en formato GLB. Vacío cuando `quad` está habilitado. | FILE3DGLB |
| `FBX` | El archivo de modelo 3D generado en formato FBX. Solo se completa cuando `quad` está habilitado. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `73f1259dcba75ce1d56aabb6f0435f11d21eee3268f93502c4c3293d562a6db0`
