# Vista previa de cualquier

PreviewAny convierte cualquier valor de entrada en texto legible para que puedas inspeccionarlo. Las cadenas pasan sin cambios, los números y los booleanos se convierten en texto plano, y otros tipos de datos se serializan a JSON cuando es posible (recurriendo a su forma de cadena simple si la serialización falla). El texto resultante se muestra en la interfaz de usuario y también se devuelve como salida de cadena para su posterior procesamiento.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `fuente` | Acepta cualquier tipo de dato de entrada para mostrarlo en la vista previa. Si no se proporciona ningún valor, la vista previa muestra 'None'. | ANY | Sí | Cualquier tipo de dato |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `result` | El valor de entrada convertido a formato de texto. El mismo texto también se muestra en la interfaz de usuario. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/es.md)

---
**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`
