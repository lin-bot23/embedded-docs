# Expressão Matemática

### ComfyMathExpression

O nó ComfyMathExpression avalia uma fórmula matemática que você escreve como texto. A fórmula pode referenciar os valores de entrada do nó usando nomes de letras, como `a`, `b`, `c`, e você pode adicionar quantos valores de entrada forem necessários através do grupo expandível `values`. O resultado da cálculação é retornado simultaneamente como um número flutuante, um inteiro e um valor booleano.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `expressão` | A fórmula matemática a ser avaliada, escrita como texto (por exemplo, `a + b`), usando os nomes das variáveis de entrada como variáveis. Entrada em múltiplas linhas. (padrão: "a + b") | STRING | Sim | N/A |
| `valores` | Grupo expandível de valores de entrada que fornece as variáveis para a expressão. Cada valor adicionado ao grupo recebe automaticamente o próximo nome de letra minúscula começando com `a` (`a`, `b`, `c`, ...), e esse nome pode então ser usado dentro da `expression`. Cada item aceita um número (INT ou FLOAT) ou um valor booleano (TRUE/FALSE). | FLOAT, INT, BOOLEAN | Sim | 1 a 26 valores, nomeados `a` a `z` |

### Notas e restrições

- `expression` não pode estar vazio ou conter apenas espaços em branco.
- A expressão deve avaliar a um resultado numérico (INT ou FLOAT). Se o resultado for de um tipo diferente, como texto, o nó gera um erro.
- O resultado numérico deve ser finito e convertible a float. Resultados que são muito grandes ou não finitos causam um erro.
- O conjunto completo de valores de entrada também está disponível dentro da expressão sob o nome da variável `values` (como uma lista), então expressões como `sum(values)` são possíveis.
- As seguintes funções matemáticas estão disponíveis dentro da expressão: `sum`, `min`, `max`, `abs`, `round`, `pow`, `sqrt`, `ceil`, `floor`, `log`, `log2`, `log10`, `sin`, `cos`, `tan`, `int`, `float`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `FLOAT` | O resultado da expressão como um número flutuante. | FLOAT |
| `INT` | O resultado da expressão convertido para um inteiro, com a parte decimal truncada. | INT |
| `BOOL` | O resultado convertido para um valor booleano: TRUE quando o resultado numérico não é zero, FALSE quando é zero. | BOOLEAN |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4c77e9834fe7341143352f95ed8808dc81def3361b197c67e33a531bb3696d71`
