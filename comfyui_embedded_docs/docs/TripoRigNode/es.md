# Tripo: Modelo con rig

Este nodo toma un modelo 3D de Tripo existente y crea una versión con rig del mismo; es decir, el modelo obtiene un esqueleto para poder ser animado. Se proporciona el ID de tarea del modelo al que se aplicará el rig, se elige la versión de rig, el tipo de esqueleto, el estilo de nombres de huesos y el formato de archivo de salida; el nodo envía el trabajo a Tripo, espera a que finalice y devuelve el resultado descargado.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `ID_de_tarea_del_modelo_original` | El ID de tarea del modelo 3D original al que se aplicará el rig. Normalmente es el ID generado por un nodo anterior de generación de modelos de Tripo. | MODEL_TASK_ID | Sí | - |
| `model_version` | Versión del modelo de rig que se usará. v1.0: solo personajes humanoides (bípedos), más de 90 ajustes preestablecidos de animación. v2.5: criaturas no humanoides (cuadrúpedos, hexápodos, octópodos, aves, serpenteantes, acuáticas). Predeterminado: `v1.0-20240301`. | COMBO | No | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | Tipo de esqueleto. "auto" ejecuta primero la verificación de rig gratuita de Tripo y utiliza el tipo recomendado. Otros valores fuerzan un tipo de esqueleto específico, como "biped" para personajes humanoides. Predeterminado: "auto". | COMBO | No | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | Esquema de nombres de huesos: nativo de Tripo o compatible con Mixamo. Tripo no puede transferir sus ajustes preestablecidos de animación a un rig v1.0 creado con la especificación mixamo; utilice "tripo" para el nodo Tripo: Retarget rigged model. Predeterminado: "tripo". | COMBO | No | "tripo"<br>"mixamo" |
| `out_format` | Formato de archivo de salida; el resultado llega a la salida correspondiente. Predeterminado: "glb". | COMBO | No | "glb"<br>"fbx" |

**Nota:** La versión de modelo v1.0 (`v1.0-20240301`) solo admite esqueletos bípedos. Si se utiliza un `rig_type` no bípedo con esta versión, el nodo genera un error e indica que se use `v2.5-20260210` en su lugar.

**Nota:** Cuando `rig_type` es "auto", Tripo primero comprueba si el modelo puede recibir un rig y selecciona el tipo de esqueleto recomendado. Si Tripo informa que el modelo no puede recibir un rig, el nodo falla con un error.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|-------------|-------------|-----------|
| `archivo_de_modelo` | El archivo de modelo 3D con rig generado. Se conserva solo por compatibilidad con versiones anteriores. | STRING |
| `id_de_tarea_de_rig` | El ID de tarea para el seguimiento del proceso de generación de rig. | RIG_TASK_ID |
| `GLB` | El modelo con rig como archivo 3D GLB. Se completa cuando `out_format` es "glb". | FILE3DGLB |
| `FBX` | El modelo con rig como archivo 3D FBX. Se completa cuando `out_format` es "fbx". | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/es.md)

---
**Source fingerprint (SHA-256):** `54c3b0984835160b74884d2c30191ad6dac6ea447862e9276253ace7367bc419`
