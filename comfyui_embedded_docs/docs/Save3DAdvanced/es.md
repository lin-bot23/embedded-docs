# Guardar 3D (Avanzado)

Save3DAdvanced guarda un modelo 3D en un archivo en el directorio de salida de ComfyUI y crea una vista previa de la escena guardada. También transmite el modelo 3D, su ubicación en la escena, la información de la cámara y las dimensiones del viewport a los nodos posteriores. Cuando la ubicación del modelo o la información de la cámara no están conectadas, el nodo utiliza los valores almacenados en el estado del viewport.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model_3d` | Archivo de modelo 3D de un nodo 3D anterior. | FILE3D | Sí | GLB<br>GLTF<br>FBX<br>OBJ<br>STL<br>USDZ<br>Any |
| `filename_prefix` | Prefijo utilizado para el nombre del archivo guardado (por defecto: "3d/ComfyUI"). | STRING | Sí | Texto libre |
| `viewport_state` | Estado del viewport que contiene información de la cámara y la ubicación del modelo, normalmente de un nodo Load 3D. | LOAD3D | Sí | - |
| `model_3d_info` | Ubicación de cada modelo en la escena: posición, rotación y escala (espacio mundial con eje Y hacia arriba). Anula la ubicación del modelo almacenada en `viewport_state` cuando está conectado. | LOAD3DMODELINFO | No | - |
| `camera_info` | Información de la cámara del viewport: posición, punto de mira, zoom y tipo. Anula la información de la cámara almacenada en `viewport_state` cuando está conectado. | LOAD3DCAMERA | No | - |
| `width` | Ancho de renderizado del viewport en píxeles (por defecto: 1024). | INT | Sí | 1 a 4096 |
| `height` | Alto de renderizado del viewport en píxeles (por defecto: 1024). | INT | Sí | 1 a 4096 |

Nota: `model_3d_info` y `camera_info` son opcionales. Cuando cualquiera de estas entradas no está conectada, el nodo recurre a los valores correspondientes almacenados en `viewport_state`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_3d` | El archivo de modelo 3D transmitido desde la entrada. | FILE3D |
| `model_3d_info` | Ubicación de cada modelo en la escena: posición, rotación y escala (espacio mundial con eje Y hacia arriba). | LOAD3DMODELINFO |
| `camera_info` | Información de la cámara del viewport: posición, punto de mira, zoom y tipo. | LOAD3DCAMERA |
| `width` | El valor de ancho de renderizado transmitido desde la entrada. | INT |
| `height` | El valor de alto de renderizado transmitido desde la entrada. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`
