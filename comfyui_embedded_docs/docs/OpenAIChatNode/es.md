# OpenAI ChatGPT

Este nodo genera respuestas de texto a partir de un modelo OpenAI. Envía el prompt de texto y, opcionalmente, imágenes o archivos a un modelo OpenAI, y devuelve la respuesta de texto generada.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `prompt` | Entradas de texto para el modelo, utilizadas para generar una respuesta (por defecto: cadena vacía). | STRING | Sí | - |
| `persistir_contexto` | Este parámetro está obsoleto y no tiene efecto (por defecto: False). | BOOLEAN | Sí | - |
| `modelo` | El modelo utilizado para generar la respuesta (por defecto: `gpt-5`). | COMBO | Sí | `gpt-6-astra`<br>`gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `imágenes` | Opcional: imagen(es) para usar como contexto para el modelo. Para incluir varias imágenes, puedes usar el nodo Batch Images. | IMAGE | No | - |
| `archivos` | Opcional: archivo(s) para usar como contexto para el modelo. Acepta entradas del nodo OpenAI Chat Input Files. | OPENAI_INPUT_FILES | No | - |
| `opciones_avanzadas` | Opcional: configuración para el modelo. Acepta entradas del nodo OpenAI Chat Advanced Options. | OPENAI_CHAT_CONFIG | No | - |

Nota: Cuando se conecta una configuración `advanced_options` que establece un esfuerzo de razonamiento, el `model` seleccionado debe admitir ese valor de esfuerzo. Por ejemplo, la familia de modelos gpt-4.1 no admite ningún esfuerzo de razonamiento; `gpt-5.5` admite none, low, medium, high y xhigh; y `gpt-5.5-pro` admite medium, high y xhigh. Si el esfuerzo de razonamiento no es compatible con el modelo seleccionado, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `output_text` | La respuesta de texto generada por el modelo OpenAI. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/es.md)

---
**Source fingerprint (SHA-256):** `687a6b1110518a2eaf23e240f43991b4ff91d6f01cae6c3ef55bcdac810e7a89`
