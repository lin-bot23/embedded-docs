# Opciones Avanzadas de OpenAI ChatGPT

El nodo OpenAIChatConfig permite definir opciones avanzadas que controlan cómo el nodo OpenAI Chat genera las respuestas. Puedes establecer la estrategia de truncamiento, limitar el número de tokens de salida, proporcionar instrucciones personalizadas y elegir cuánto debe razonar el modelo antes de responder.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `truncamiento` | La estrategia de truncamiento que se usará para la respuesta del modelo. auto: si el contexto de esta respuesta y las anteriores supera el tamaño de la ventana de contexto del modelo, el modelo truncará la respuesta para ajustarse a la ventana de contexto descartando elementos de entrada en medio de la conversación. disabled: si una respuesta del modelo supera el tamaño de la ventana de contexto, la solicitud fallará con un error 400 (por defecto: "auto") | COMBO | Sí | "auto"<br>"disabled" |
| `tokens_salida_max` | Un límite superior para la cantidad de tokens que se pueden generar en una respuesta, incluidos los tokens de salida visibles y los tokens de razonamiento (por defecto: 4096) | INT | No | 16 a 16384 |
| `instrucciones` | Instrucciones para el modelo sobre cómo generar la respuesta (se admite entrada multilínea) | STRING | No | - |
| `reasoning_effort` | Cuánto debe razonar el modelo antes de responder. "default" deja la elección al modelo. Los niveles admitidos varían según el modelo: GPT-6 Astra low-max; GPT-5.6 none-max (sin mínimo); GPT-5.5 none-xhigh; GPT-5.5 Pro medium-xhigh; GPT-5 minimal-high; o-series low-high; GPT-4.1 no tiene razonamiento. Los niveles no admitidos se rechazan antes de enviar la solicitud. (por defecto: "default") | COMBO | No | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

Nota: aunque `top_p` y `temperature` aparecen como propiedades en la especificación de la API, no son compatibles con todos los modelos y, por lo tanto, no se exponen como entradas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `OPENAI_CHAT_CONFIG` | Objeto de configuración que contiene los ajustes especificados para usar con los nodos OpenAI Chat | OPENAI_CHAT_CONFIG |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/es.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
