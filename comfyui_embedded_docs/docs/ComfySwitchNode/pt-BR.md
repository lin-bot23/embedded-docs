# Alternar

O nó Switch seleciona entre duas entradas possíveis com base em uma condição booleana. Quando `switch` está ativado (true), ele passa a entrada `on_true` para a saída; quando desativado (false), ele passa `on_false`. Apenas a ramificação selecionada é avaliada, então a outra entrada não precisa estar conectada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `alternar` | Uma condição booleana que determina qual entrada passar. Quando ativado (true), a entrada `on_true` é selecionada. Quando desativado (false), a entrada `on_false` é selecionada. | BOOLEAN | Sim | |
| `falso` | Os dados a serem passados para a saída quando o `switch` estiver desativado (false). Esta entrada é necessária apenas quando o `switch` é false. | MATCH_TYPE | Não | |
| `verdadeiro` | Os dados a serem passados para a saída quando o `switch` estiver ativado (true). Esta entrada é necessária apenas quando o `switch` é true. | MATCH_TYPE | Não | |

**Nota sobre Requisitos de Entrada:** As entradas `on_false` e `on_true` são necessárias condicionalmente. O nó solicita a entrada `on_true` apenas quando o `switch` é true e a entrada `on_false` apenas quando o `switch` é false. Ambas as entradas devem ser do mesmo tipo de dados e devem coincidir com o tipo de dados da saída. Se a entrada selecionada não estiver conectada, o nó não gera valor de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `saída` | Os dados selecionados. Este é o valor da entrada `on_true` quando o `switch` é true ou o valor da entrada `on_false` quando o `switch` é false. | MATCH_TYPE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
