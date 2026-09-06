# Vista previa 3D (Avanzado)

Este nodo muestra una vista previa 3D del modelo en la interfaz sin guardar el archivo en el directorio de salida de ComfyUI. Guarda el modelo en un archivo temporal y transmite los datos del modelo, la información del modelo, la información de la cámara y las dimensiones de la vista previa para su posterior procesamiento en el flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model_3d` | Archivo de modelo 3D proveniente de un nodo 3D anterior. | FILE3D | Sí | GLB, GLTF, FBX, OBJ, STL, USDZ o cualquier formato 3D compatible |
| `model_3d_info` | Metadatos opcionales de información del modelo. Opción avanzada. | LOAD3DMODELINFO | No | - |
| `viewport_state` | El estado actual de la vista que contiene información de la cámara y del modelo. | LOAD3D | Sí | - |
| `camera_info` | Configuración opcional de cámara para la vista 3D. Opción avanzada. | LOAD3DCAMERA | No | - |
| `width` | El ancho de la vista previa en píxeles. Valor predeterminado: 1024. | INT | Sí | 1 a 4096 |
| `height` | La altura de la vista previa en píxeles. Valor predeterminado: 1024. | INT | Sí | 1 a 4096 |

Nota: cuando `camera_info` o `model_3d_info` no están conectados, sus valores se toman de `viewport_state` cuando estén disponibles. Si `viewport_state` no contiene información de cámara, `camera_info` es None. Si `viewport_state` no tiene información del modelo, `model_3d_info` se establece por defecto en una lista vacía. Si `viewport_state` no es un diccionario, se trata como vacío.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_3d` | El archivo de modelo 3D transmitido desde la entrada. | FILE3D |
| `model_3d_info` | Metadatos de información del modelo, ya sea desde la entrada o desde el estado de la vista. | LOAD3DMODELINFO |
| `camera_info` | Configuración de cámara, ya sea desde la entrada o desde el estado de la vista. | LOAD3DCAMERA |
| `width` | El ancho de la vista previa en píxeles. | INT |
| `height` | La altura de la vista previa en píxeles. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `46c14d6242cbcabd457e13ae193427bb4c1fed55e81e568d50719fff0f1a95a0`
