# Expresión matemática

El nodo ComfyMathExpression evalúa una fórmula matemática que se escribe como texto. La fórmula puede hacer referencia a los valores de entrada del nodo mediante nombres de letra como `a`, `b`, `c`, y se pueden agregar tantos valores de entrada como sea necesario a través del grupo ampliable `values`. El resultado del cálculo se devuelve simultáneamente como un número de coma flotante, un número entero y un valor booleano.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `expresión` | La fórmula matemática a evaluar, escrita como texto (por ejemplo, `a + b`), que utiliza los nombres de letra de los valores de entrada como variables. Entrada multilínea. (valor por defecto: "a + b") | STRING | Sí | N/A |
| `valores` | Grupo ampliable de valores de entrada que proporciona las variables para la expresión. Cada valor agregado al grupo recibe automáticamente el siguiente nombre de letra minúscula a partir de `a` (`a`, `b`, `c`, ...), y ese nombre puede usarse luego dentro de `expression`. Cada elemento acepta un número (INT o FLOAT) o un valor booleano (TRUE/FALSE). | FLOAT, INT, BOOLEAN | Sí | 1 a 26 valores, nombrados de `a` a `z` |

### Notas y restricciones

- `expression` no puede estar vacía ni contener solo espacios en blanco.
- La expresión debe dar como resultado un valor numérico (INT o FLOAT). Si el resultado es de otro tipo, como texto, el nodo genera un error.
- El resultado numérico debe ser finito y convertible a un número de coma flotante (FLOAT). Los resultados demasiado grandes o no finitos provocan un error.
- El conjunto completo de valores de entrada también está disponible dentro de la expresión bajo el nombre de variable `values` (como una lista), por lo que expresiones como `sum(values)` son posibles.
- Las siguientes funciones matemáticas están disponibles dentro de la expresión: `sum`, `min`, `max`, `abs`, `round`, `pow`, `sqrt`, `ceil`, `floor`, `log`, `log2`, `log10`, `sin`, `cos`, `tan`, `int`, `float`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `FLOAT` | El resultado de la expresión como número de coma flotante. | FLOAT |
| `INT` | El resultado de la expresión convertido a un número entero, con la parte decimal truncada. | INT |
| `BOOL` | El resultado convertido a un valor booleano: TRUE cuando el resultado numérico no es cero, FALSE cuando es cero. | BOOLEAN |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/es.md)

---
**Source fingerprint (SHA-256):** `4c77e9834fe7341143352f95ed8808dc81def3361b197c67e33a531bb3696d71`
