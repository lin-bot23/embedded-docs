# Remallar malla (DC de banda estrecha)

Remesh Mesh reconstruye una malla con una teselación limpia y uniforme, muestreando un campo de distancia de banda estrecha alrededor de la superficie original y extrayendo la malla con Dual Contouring. Esto normaliza topologías desordenadas, no múltiples o autointersecantes, y está pensado para ejecutarse antes de Decimate Mesh a fin de alcanzar un número exacto de caras. El procesamiento se ejecuta en el dispositivo de cómputo activo y la malla de salida se mantiene soldada.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|------------|-------|
| `malla` | La malla de entrada que se va a remallar. | MESH | Sí | — |
| `resolución` | Resolución de la rejilla de vóxeles (densidad de salida). 256 ~ 100k caras, 512 ~ 1M. Para un número exacto de caras, aplique Decimate Mesh a continuación. (predeterminado: 512) | INT | Sí | 32 - 2048 |
| `sign_mode` | Modo de extracción de superficie. `"udf"` es robusto frente a entradas desordenadas o no múltiples; `"sdf"` produce una única superficie limpia con recuperación de detalles nítidos mediante QEF (Quadratic Error Function), pero requiere una orientación de las caras consistente. Al seleccionar un modo se muestran sus subopciones específicas. (predeterminado: `"udf"`) | DYNAMIC_COMBO | Sí | `"udf"`<br>`"sdf"` |
| `band` | Ancho de la banda estrecha en unidades de vóxel. En el modo UDF también desplaza la superficie. (avanzado, predeterminado: 1.0) | FLOAT | Sí | 0.5 - 4.0 |
| `project_back` | Interpola linealmente los vértices hacia la superficie original (0 = DC puro, 1 = proyectado sobre la superficie). (avanzado, predeterminado: 0.0) | FLOAT | Sí | 0.0 - 1.0 |
| `fix_poles` | Colapsa pares de vértices de valencia 3 (artefacto de unión en T de DC). (avanzado, predeterminado: false) | BOOLEAN | Sí | true / false |
| `smooth_iters` | Iteraciones de suavizado de Taubin (0 = desactivado). Con 2-3 se limpian los artefactos escalonados de DC; valores más altos suavizan en exceso las aristas QEF. (predeterminado: 0) | INT | Sí | 0 - 20 |
| `drop_small_components` | Elimina los componentes por debajo de esta fracción del número de caras del componente más grande. 0 desactiva esta opción. (avanzado, predeterminado: 0.01) | FLOAT | Sí | 0.0 - 0.5 |
| `precluster_max_verts` | Limita el número de vértices de entrada antes de las consultas al campo; las entradas que superen este valor se deciman primero por clústeres hasta ese límite. Evita quedarse sin memoria (OOM) en mallas enormes. (avanzado, predeterminado: 20,000,000) | INT | Sí | 0 - 100,000,000 |

### Entradas del modo "udf"

Estos parámetros aparecen cuando `sign_mode` está establecido en `"udf"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|------------|-------|
| `qef` | Colocación de vértices duales mediante QEF (Quadratic Error Function) para aristas más nítidas. (predeterminado: false) | BOOLEAN | No | true / false |
| `drop_inverted_components` | Elimina los componentes cerrados con normales hacia adentro (volumen negativo), es decir, la capa interna de UDF. (predeterminado: false) | BOOLEAN | No | true / false |
| `drop_enclosed_components` | Elimina los componentes dentro de la caja delimitadora (bbox) del más grande que no pasan una prueba de punto en la malla por raycast. Desactívelo para piezas anidadas legítimas. (predeterminado: false) | BOOLEAN | No | true / false |

### Entradas del modo "sdf"

Estos parámetros aparecen cuando `sign_mode` está establecido en `"sdf"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|------------|-------|
| `qef` | Colocación de vértices duales mediante QEF (Quadratic Error Function) para recuperar detalles nítidos, en lugar del centroide del cruce de arista. (predeterminado: true) | BOOLEAN | No | true / false |
| `manifold` | Manifold Dual Contouring: de 1 a 4 vértices duales por vóxel para casos de varias láminas. Más lento. (predeterminado: false) | BOOLEAN | No | true / false |

Nota: la opción `qef` tiene un valor predeterminado distinto según el modo seleccionado: `false` en el modo `"udf"` y `true` en el modo `"sdf"`. Cuando `precluster_max_verts` es mayor que 0 y la malla de entrada tiene más vértices que ese valor, la malla se decima primero por clústeres hasta ese objetivo antes de las consultas al campo. Tras el procesamiento, el nodo muestra el cambio en el número de caras entre la entrada y la salida (por ejemplo, "caras: 1.23M → 200K (-84%)").

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `mesh` | La malla remallada con teselación uniforme y topología soldada. Los colores de vértice se conservan si están presentes en la entrada; las UV, normales y tangentes no se transfieren. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/es.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`
