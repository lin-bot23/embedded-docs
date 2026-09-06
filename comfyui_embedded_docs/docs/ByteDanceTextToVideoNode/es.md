# ByteDance Texto a Video

# Nodo de Texto a Vídeo de ByteDance

El nodo de Texto a Vídeo de ByteDance genera videos utilizando modelos de ByteDance a través de una API basada en sugerencias de texto. Acepta una descripción de texto y varios ajustes de vídeo como entrada, luego crea un vídeo que coincida con las especificaciones proporcionadas. El nodo maneja la comunicación con la API y devuelve el vídeo generado como salida.

## Resumen

El nodo de Texto a Vídeo de ByteDance está diseñado para convertir sugerencias de texto en vídeos utilizando las capacidades de IA de ByteDance. Los usuarios pueden especificar el modelo, la resolución, el aspecto, la duración y otros parámetros para controlar el proceso de generación de vídeo.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | El modelo de ByteDance a utilizar para la generación. | STRING | Sí | 
  - "seedance-1-5-pro-251215"
  - "seedance-1-0-pro-250528"
  - "seedance-1-0-pro-fast-251015" |
| `prompt` | La sugerencia de texto utilizada para generar el vídeo. | STRING | Sí | Entrada de texto multilinea |
| `resolución` | La resolución del vídeo de salida. | STRING | Sí | 
  - "480p"
  - "720p"
  - "1080p" |
| `relación_de_aspecto` | El aspecto del vídeo de salida. | STRING | Sí | 
  - "16:9"
  - "4:3"
  - "1:1"
  - "3:4"
  - "9:16"
  - "21:9" |
| `duración` | La duración del vídeo de salida en segundos. | INT | Sí | 3 a 12 segundos |
| `semilla` | Semilla a utilizar para la generación. | INT | No | 0 a 2,147,483,647 |
| `cámara_fija` | Especifica si se debe fijar la cámara. | BOOLEAN | No | - |
| `marca_de_agua` | Si se debe agregar una marca de agua "Generado por IA" al vídeo. | BOOLEAN | No | - |
| `generate_audio` | Este parámetro se ignora para cualquier modelo excepto `seedance-1-5-pro-251215`. | BOOLEAN | No | - |

**Restricciones del Parámetro:**

- El `prompt` debe contener al menos 1 carácter después de la eliminación de espacios en blanco.
- El `prompt` no puede contener los siguientes parámetros de texto: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- La `duration` está limitada a valores entre 3 y 12 segundos.
- Para el modelo `seedance-1-5-pro-251215`, la duración mínima admitida es de 4 segundos.
- La `seed` acepta valores de 0 a 2,147,483,647.
- El parámetro `generate_audio` solo tiene efecto cuando el `model` está configurado en `seedance-1-5-pro-251215`; se ignora para todos los otros modelos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `output` | El archivo de vídeo generado. | VIDEO |

**Nota:** El nodo de Texto a Vídeo de ByteDance es un nodo de API y requiere tokens de autenticación y claves de API para funcionar adecuadamente. Estos se proporcionan a través de las entradas ocultas `auth_token_comfy_org` y `api_key_comfy_org`.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
