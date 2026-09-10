# Tripo: De imagen a vistas múltiples

Genera vistas frontal, izquierda, trasera y derecha del sujeto a partir de una única imagen de entrada usando la API de Tripo. La imagen se sube, se inicia una tarea de generación multivista y se consulta repetidamente hasta que finaliza, y las cuatro vistas resultantes se devuelven junto con el ID de tarea. Esta es una tarea de pago facturada por aproximadamente 0,10 USD.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `image` | La imagen de origen del sujeto a partir de la cual Tripo genera las vistas frontal, izquierda, trasera y derecha. Solo se utiliza una imagen para la solicitud, incluso si se proporciona un lote. | IMAGE | Sí | Imagen única |

Nota: El nodo llama a la API en la nube de Tripo y espera a que finalice la tarea de generación. Una tarea típica tarda alrededor de 25 segundos. La autenticación se gestiona automáticamente a través de las entradas ocultas del nodo, por lo que no es necesario proporcionar ninguna clave de API de Tripo en el flujo de trabajo. El nodo requiere las cuatro URL de vista en la respuesta de Tripo (`front_view_url`, `left_view_url`, `back_view_url`, `right_view_url`); si falta alguna vista, la ejecución falla con un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `task_id de vistas múltiples` | El identificador de tarea devuelto por Tripo para la solicitud de generación de imágenes multivista. Se puede usar para hacer referencia a la tarea completada, por ejemplo, al refinar las vistas con Tripo: Edit Multiview. | MULTIVIEW_TASK_ID |
| `frontal` | La vista frontal generada del sujeto. | IMAGE |
| `izquierda` | La vista izquierda generada del sujeto. | IMAGE |
| `atrás` | La vista trasera generada del sujeto. | IMAGE |
| `derecha` | La vista derecha generada del sujeto. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/es.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`
