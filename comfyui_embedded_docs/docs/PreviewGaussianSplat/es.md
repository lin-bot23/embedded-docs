# Vista previa de Splat

El nodo PreviewGaussianSplat muestra un archivo de gaussian splat 3D en una ventana de vista previa sin guardarlo en el directorio de salida de ComfyUI. Acepta un archivo de modelo 3D en varios formatos gaussian splat, guarda una copia temporal para la vista previa y transmite los datos del modelo sin modificar para su posterior procesamiento en el flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo_3d` | Un archivo de gaussian splat 3D. | FILE3D | Sí | splat<br>ply<br>spz<br>ksplat |
| `info_modelo_3d` | Información de metadatos opcional sobre el modelo 3D. Cuando no está conectado, el nodo utiliza la información del modelo de `viewport_state`. | LOAD3DMODELINFO | No | - |
| `estado_de_vista` | El estado actual del visor 3D, incluida la información de cámara y modelo. | LOAD3D | Sí | - |
| `info_cámara` | Información de cámara opcional para la vista previa. Cuando no está conectado, el nodo utiliza la información de cámara de `viewport_state`. | LOAD3DCAMERA | No | - |
| `ancho` | El ancho del renderizado de la vista previa en píxeles (por defecto: 1024). | INT | Sí | 1 a 4096 |
| `alto` | La altura del renderizado de la vista previa en píxeles (por defecto: 1024). | INT | Sí | 1 a 4096 |

Nota: cuando no se proporcionan `camera_info` o `model_3d_info`, el nodo recurre a la información de cámara y modelo almacenada en `viewport_state`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `modelo_3d` | El archivo de gaussian splat 3D de entrada, transmitido sin cambios. | FILE3D |
| `info_modelo_3d` | Información de metadatos sobre el modelo 3D, ya sea de la entrada o derivada del estado del visor. | LOAD3DMODELINFO |
| `info_cámara` | Información de cámara para la vista previa, ya sea de la entrada o derivada del estado del visor. | LOAD3DCAMERA |
| `ancho` | El ancho del renderizado de la vista previa. | INT |
| `alto` | La altura del renderizado de la vista previa. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/es.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`
