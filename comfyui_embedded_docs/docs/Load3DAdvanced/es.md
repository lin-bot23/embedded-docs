# Cargar 3D (Avanzado)

El nodo Load 3D (Advanced) carga un archivo de modelo 3D desde el directorio `input/3d` de ComfyUI y proporciona los datos del modelo junto con la ubicación del modelo y la información de la cámara capturada en el estado del viewport del visor 3D. Es compatible con formatos de archivo 3D comunes y permite establecer el ancho y el alto de renderizado del viewport en píxeles. Este nodo es experimental.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model_file` | El archivo de modelo 3D a cargar. Seleccione "none" para omitir la carga de un archivo de modelo. | COMBO | Sí | `"none"`<br>Archivos de modelos 3D disponibles en el directorio `input/3d` |
| `viewport_state` | El estado actual del viewport que contiene información de cámara y modelo del visor 3D. | LOAD3D | Sí | - |
| `width` | Ancho de renderizado del viewport en píxeles (por defecto: 1024). | INT | Sí | Mínimo: 1<br>Máximo: 4096<br>Por defecto: 1024<br>Incremento: 1 |
| `height` | Alto de renderizado del viewport en píxeles (por defecto: 1024). | INT | Sí | Mínimo: 1<br>Máximo: 4096<br>Por defecto: 1024<br>Incremento: 1 |

**Notas sobre los parámetros:**
- El parámetro `model_file` solo lista archivos con las siguientes extensiones: .gltf, .glb, .obj, .fbx, .stl
- Los archivos deben colocarse en el directorio `input/3d` de su instalación de ComfyUI; también se buscan en subcarpetas, y las rutas de archivo se muestran relativas al directorio `input`.
- Si `model_file` es "none", no se carga ningún dato de modelo y la salida `model_3d` estará vacía.
- Si `model_file` se establece en un archivo que no existe, el nodo devuelve un error de validación: "Invalid 3D model file: {model_file}"

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_3d` | Archivo de modelo 3D cargado (glb/obj/stl/etc.). Vacío si no se seleccionó ningún archivo de modelo. | FILE3DANY |
| `model_3d_info` | Ubicación de cada modelo en la escena: posición, rotación y escala (espacio mundial con eje Y hacia arriba). | LOAD3DMODELINFO |
| `camera_info` | Información de la cámara del viewport: posición, punto de mira, zoom y tipo. | LOAD3DCAMERA |
| `width` | Ancho de renderizado del viewport en píxeles. | INT |
| `height` | Alto de renderizado del viewport en píxeles. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `c79c53dde0c8b3afb7df7b972df749f5040c92d48b47e355c4497d9b0cbf1c22`
