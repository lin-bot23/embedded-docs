# Tripo: Editar Multiview

Edita as vistas de um resultado do Tripo: Image to Multiview usando uma instrução de texto separada para cada vista. As vistas sem instrução permanecem inalteradas. As imagens editadas devem ser conectadas ao Tripo: Multiview to Model para criar um modelo 3D; um conjunto multiview editado não pode ser editado novamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `multiview_task_id` | ID da tarefa do resultado do Tripo: Image to Multiview cujas vistas serão editadas. Deve vir do nó Tripo: Image to Multiview. | MULTIVIEW_TASK_ID | Sim | Task ID |
| `front_prompt` | Instrução de texto descrevendo a edição a ser aplicada à vista frontal. Quando vazia, a vista frontal permanece inalterada. Padrão: string vazia. | STRING | Não | Texto multilinha |
| `left_prompt` | Instrução de texto descrevendo a edição a ser aplicada à vista esquerda. Quando vazia, a vista esquerda permanece inalterada. Padrão: string vazia. | STRING | Não | Texto multilinha |
| `back_prompt` | Instrução de texto descrevendo a edição a ser aplicada à vista traseira. Quando vazia, a vista traseira permanece inalterada. Padrão: string vazia. | STRING | Não | Texto multilinha |
| `right_prompt` | Instrução de texto descrevendo a edição a ser aplicada à vista direita. Quando vazia, a vista direita permanece inalterada. Padrão: string vazia. | STRING | Não | Texto multilinha |

Observação: pelo menos um dos quatro prompts (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) deve conter texto não vazio; textos compostos apenas por espaços em branco são tratados como vazios, e se todos os prompts estiverem vazios o nó gera um erro.

Observação: o custo é de aproximadamente 0,05 USD por vista que possui uma instrução de edição.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `frente` | Imagem da vista frontal editada. | IMAGE |
| `esquerda` | Imagem da vista esquerda editada. | IMAGE |
| `traseira` | Imagem da vista traseira editada. | IMAGE |
| `direita` | Imagem da vista direita editada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db8b0a3ffe4332fcbcaac4da0d7b07217d01d2f05526750540f6036293e013ab`
