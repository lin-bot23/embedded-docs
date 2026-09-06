# Vista previa de audio

El nodo Preview Audio te permite escuchar el audio directamente en la interfaz de ComfyUI sin necesidad de guardarlo en el directorio de salida. Toma datos de audio como entrada, verifica que estén presentes y los deja pasar mientras muestra un reproductor de audio temporal para que puedas escuchar el resultado.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `audio` | Los datos de audio para previsualizar. El nodo lanza un ValueError si la entrada es None, lo que puede ocurrir cuando el video de origen no tiene pista de audio. | AUDIO | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `audio` | Los datos de audio pasan sin cambios desde la entrada. | AUDIO |
| `ui` | Muestra un widget de reproductor de audio en la interfaz para previsualizar el audio. | UI |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/es.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`
