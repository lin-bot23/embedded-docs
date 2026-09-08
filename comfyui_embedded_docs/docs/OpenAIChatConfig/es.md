# Opciones Avanzadas de OpenAI ChatGPT

# Opciones Avanzadas de ChatGPT de OpenAI

El nodo Opciones Avanzadas de ChatGPT de OpenAI permite configurar opciones adicionales para los Nodos de Chat de OpenAI. Este nodo proporciona configuraciones avanzadas que controlan cómo el modelo genera respuestas, incluyendo el comportamiento de truncamiento, límites de longitud de salida y instrucciones personalizadas.

## Resumen

El nodo Opciones Avanzadas de ChatGPT de OpenAI está diseñado para mejorar la funcionalidad de los Nodos de Chat de OpenAI, permitiendo a los usuarios especificar opciones de configuración avanzadas. Estas configuraciones pueden ayudar a ajustar la generación de respuestas del modelo a requisitos específicos.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `truncamiento` | La estrategia de truncamiento a usar para la respuesta del modelo. auto: Si el contexto de esta respuesta y las anteriores excede el tamaño de la ventana de contexto del modelo, el modelo truncará la respuesta para ajustarse a la ventana de contexto eliminando elementos de entrada en el medio de la conversación. disabled: Si una respuesta del modelo excederá el tamaño de la ventana de contexto de un modelo, la solicitud fallará con un error 400 (por defecto: "auto") | STRING | Sí | "auto"<br>"disabled" |
| `tokens_salida_max` | Un límite superior para el número de tokens que pueden generarse para una respuesta, incluyendo tokens de salida visibles y tokens de razonamiento (por defecto: 4096) | INT | No | 16 a 16384 |
| `instrucciones` | Instrucciones para el modelo sobre cómo generar la respuesta (se admite entrada multilinea) | STRING | No | - |
| `reasoning_effort` | Cuánto razona el modelo antes de responder. 'default' deja la elección al modelo. Los niveles de soporte varían según el modelo: GPT-6 Astra low-max, GPT-5.6 none-max (sin mínimo), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high; GPT-4.1 no tiene razonamiento. Los niveles no soportados se rechazan antes de que se envíe la solicitud (por defecto: "default") | STRING | No | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | Objeto de configuración que contiene las configuraciones especificadas para su uso con los Nodos de Chat de OpenAI | OPENAI_CHAT_CONFIG |

## Notas

- El parámetro `max_output_tokens` establece un límite superior en el número total de tokens, incluyendo tanto tokens de salida visibles como tokens de razonamiento.
- El parámetro `reasoning_effort` permite especificar el nivel de razonamiento que debe aplicar el modelo antes de generar una respuesta. Los niveles de soporte varían dependiendo del modelo utilizado.
- El parámetro `instructions` se puede usar para proporcionar instrucciones detalladas al modelo para guiar el proceso de generación de respuestas.
- El parámetro `truncation` determina si el modelo debe truncar automáticamente la respuesta si excede el tamaño de la ventana de contexto o fallar con un error 400.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/es.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
