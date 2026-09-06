# Janelas de Contexto LTXV

### Visão Geral

Este nó define janelas de contexto para modelos semelhantes ao LTXV durante a amostragem. Ele divide o processo de geração de vídeo em janelas sobrepostas para gerenciar o uso da memória e melhorar a coesão temporal.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a aplicar janelas de contexto durante a amostragem. | MODELO | Sim | - |
| `context_length` | O comprimento da janela de contexto em quadros reais. Deve ser 8*n + 1. (padrão: 145) | INTEIRO | Sim | Mínimo: 1<br>Máximo: nodes.MAX_RESOLUTION<br>Passo: 8 |
| `context_overlap` | A sobreposição da janela de contexto em quadros reais. (padrão: 40) | INTEIRO | Sim | Mínimo: 0<br>Passo: 8 |
| `context_schedule` | Algoritmo de agendamento dependente de passo para janelas de contexto. (padrão: UNIFORM_STANDARD) | COMBO | Sim | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | O comprimento do passo da janela de contexto; aplicável apenas a agendamentos uniformes. (padrão: 1) | INTEIRO | Não | Mínimo: 1 |
| `closed_loop` | Se deve fechar o loop da janela de contexto; aplicável apenas a agendamentos em loop. (padrão: Falso) | BOOLEANO | Não | True<br>False |
| `fuse_method` | O método a usar para fundir as janelas de contexto. (padrão: PYRAMID) | COMBO | Sim | Opções de comfy.context_windows.ContextFuseMethods.LIST_STATIC |
| `freenoise` | Se deve aplicar o FreeNoise noise shuffling, melhora a mesclagem de janelas. (padrão: True) | BOOLEANO | Não | True<br>False |
| `retain_first_frame` | Manter o primeiro frame latente em cada janela de contexto (pode ajudar a manter referência inicial). (padrão: Falso) | BOOLEANO | Não | True<br>False |
| `split_conds_to_windows` | Se deve dividir múltiplas condições (criadas por ConditionCombine) para cada janela com base no índice da região. (padrão: Falso) | BOOLEANO | Não | True<br>False |

**Nota:** O parâmetro `context_length` deve seguir a fórmula 8*n + 1, onde n é um inteiro positivo. O nó ajusta automaticamente o valor para atender a essa exigência, convertendo quadros reais para quadros latentes. O `context_overlap` também é convertido de quadros reais para quadros latentes (dividido por 8).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MODEL` | O modelo com janelas de contexto aplicadas para a amostragem. | MODELO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/pt-BR.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`
