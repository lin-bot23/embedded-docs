# Interruptor

El nodo Switch selecciona entre dos entradas posibles según una condición booleana. Cuando `switch` está habilitado (verdadero), pasa la entrada `on_true` a la salida; cuando está deshabilitado (falso), pasa `on_false`. Solo se evalúa la rama seleccionada, por lo que no es necesario que la otra entrada esté conectada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `switch` | Una condición booleana que determina qué entrada se pasa. Cuando está habilitado (verdadero), se selecciona la entrada `on_true`. Cuando está deshabilitado (falso), se selecciona la entrada `on_false`. | BOOLEAN | Sí |  |
| `on_false` | Los datos que se pasan a la salida cuando `switch` está deshabilitado (falso). Esta entrada solo es necesaria cuando `switch` es falso. | MATCH_TYPE | No |  |
| `on_true` | Los datos que se pasan a la salida cuando `switch` está habilitado (verdadero). Esta entrada solo es necesaria cuando `switch` es verdadero. | MATCH_TYPE | No |  |

**Nota sobre los requisitos de entrada:** Las entradas `on_false` y `on_true` son obligatorias de forma condicional. El nodo solicita la entrada `on_true` solo cuando `switch` es verdadero, y la entrada `on_false` solo cuando `switch` es falso. Ambas entradas deben ser del mismo tipo de datos y deben coincidir con el tipo de datos de la salida. Si la entrada seleccionada no está conectada, el nodo no emite ningún valor.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | Los datos seleccionados. Este es el valor de la entrada `on_true` cuando `switch` es verdadero, o el valor de la entrada `on_false` cuando `switch` es falso. | MATCH_TYPE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/es.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
