# OpenAI ChatGPT

Este nodo genera respuestas de texto a partir de un modelo de OpenAI. Acepta un texto de entrada y, opcionalmente, imágenes o archivos como contexto, y luego envía esta información a un modelo de OpenAI para generar una respuesta de texto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Entradas de texto al modelo, utilizadas para generar una respuesta. Este es el texto al que el modelo debe responder. | STRING | Sí | - |
| `persistir_contexto` | Este parámetro está obsoleto y no tiene efecto. Se incluye por compatibilidad con versiones anteriores, pero no influye en el comportamiento del nodo. | BOOLEAN | No | - |
| `modelo` | El modelo utilizado para generar la respuesta. Seleccione entre los modelos de OpenAI disponibles. | COMBO | Sí | gpt-6-astra<br>gpt-5.6-sol<br>gpt-5.6-terra<br>gpt-5.6-luna<br>gpt-5.5-pro<br>gpt-5.5<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br>gpt-4.1<br>gpt-4.1-mini<br>gpt-4.1-nano<br>o4-mini<br>o3<br>o1-pro<br>o1 |
| `imágenes` | Imágenes opcionales para utilizar como contexto para el modelo. Para incluir múltiples imágenes, utilice el nodo de Imágenes en lote. | IMAGE | No | - |
| `archivos` | Archivos opcionales para utilizar como contexto para el modelo. Acepta entradas del nodo de Entradas de archivos de Chat de OpenAI. | OPENAI_INPUT_FILES | No | - |
| `opciones_avanzadas` | Configuración opcional para el modelo. Acepta entradas del nodo de Opciones avanzadas de Chat de OpenAI. | OPENAI_CHAT_CONFIG | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output_text` | La respuesta de texto generada por el modelo de OpenAI. Este es el texto generado basado en el prompt de entrada y el contexto. | STRING |

## Notas

- El parámetro `persist_context` está obsoleto y no tiene efecto. Se incluye por compatibilidad con versiones anteriores, pero no debe utilizarse.
- La entrada `images` puede utilizarse para proporcionar contexto adicional al modelo. Si se proporcionan múltiples imágenes, deben conectarse utilizando el nodo de Imágenes en lote.
- La entrada `files` permite proporcionar contexto adicional en forma de archivos. Estos archivos deben conectarse desde el nodo de Entradas de archivos de Chat de OpenAI.
- La entrada `advanced_options` permite una configuración más detallada del comportamiento del modelo. Esto debe conectarse desde el nodo de Opciones avanzadas de Chat de OpenAI.
- El costo de usar este nodo depende del modelo seleccionado. El costo se calcula basado en el número de tokens utilizados por el modelo. El costo exacto se mostrará en la IU del nodo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/es.md)

---
**Source fingerprint (SHA-256):** `687a6b1110518a2eaf23e240f43991b4ff91d6f01cae6c3ef55bcdac810e7a89`
