# Tripo: Redireccionar modelo con rig

El nodo TripoRetargetNode aplica una animación preestablecida a un modelo 3D existente que tiene un rig. Toma el ID de tarea de un modelo al que se le aplicó rig anteriormente, envía una solicitud de retargeting a la API de Tripo y descarga el archivo animado resultante. El modelo animado se puede devolver como GLB o FBX, con geometría de malla opcional y reproducción en el lugar opcional.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `original_model_task_id` | El ID de tarea del modelo 3D que ya tiene rig y al que se aplicará el retargeting. La tarea referenciada debe ser una tarea de rig; un rig creado con la especificación Mixamo en la versión de modelo v1.0 no puede utilizarse para retargeting. | RIG_TASK_ID | Sí | - |
| `animation` | El preset de animación que se aplicará al modelo con rig. Las animaciones `preset:*` funcionan con ambos modelos con rig; las animaciones `preset:biped:*` requieren un rig creado con la versión de modelo v1.0-20240301. | COMBO | Sí | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>más opciones `"preset:biped:*"` que se muestran en la interfaz |
| `out_format` | Formato de archivo de salida; el resultado llega por la salida correspondiente. (por defecto: glb) | COMBO | No | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | Incluir la malla en la exportación; si está desactivado, exporta solo el esqueleto animado. (por defecto: True) | BOOLEAN | No | True<br>False |
| `animate_in_place` | Reproducir la animación en el lugar, sin desplazamiento de la raíz. (por defecto: False) | BOOLEAN | No | True<br>False |
| `auth_token_comfy_org` | Token de autenticación para el acceso a la API de Comfy.org (parámetro oculto). | AUTH_TOKEN_COMFY_ORG | No | - |
| `api_key_comfy_org` | Clave de API para el acceso al servicio de Comfy.org (parámetro oculto). | API_KEY_COMFY_ORG | No | - |
| `unique_id` | Identificador único para el seguimiento de la operación (parámetro oculto). | UNIQUE_ID | No | - |

Nota: Las animaciones del grupo `preset:*` funcionan con ambos modelos con rig, mientras que las animaciones del grupo `preset:biped:*` requieren un rig creado con la versión de modelo v1.0-20240301. Si el rig referenciado se creó con la especificación Mixamo y con una versión de modelo que empiece por `v1.0`, la llamada de retargeting falla con un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_file` | El archivo de modelo 3D animado generado (solo por compatibilidad con versiones anteriores). | STRING |
| `retarget task_id` | El ID de tarea para el seguimiento de la operación de retargeting. | RETARGET_TASK_ID |
| `GLB` | El modelo 3D animado en formato GLB. Se completa cuando `out_format` es glb. | FILE3DGLB |
| `FBX` | El modelo 3D animado en formato FBX. Se completa cuando `out_format` es fbx. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/es.md)

---
**Source fingerprint (SHA-256):** `e5417a8fa584285ba9e57526e65b091c2383374c70364df9053777a3ce09541a`
