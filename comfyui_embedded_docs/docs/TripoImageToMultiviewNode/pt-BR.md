# Tripo: Imagem para Multiview

Gera vistas frontal, esquerda, traseira e direita do sujeito a partir de uma única imagem de entrada usando a API Tripo. A imagem é enviada, uma tarefa de geração multiview é iniciada e consultada periodicamente até ser concluída, e as quatro vistas resultantes são retornadas junto com o ID da tarefa. Esta é uma tarefa paga, cobrada a aproximadamente 0,10 USD.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de origem do sujeito a partir da qual o Tripo gera as vistas frontal, esquerda, traseira e direita. Apenas uma imagem é usada para a solicitação, mesmo que um lote seja fornecido. | IMAGE | Sim | Imagem única |

Nota: o nó chama a API de nuvem do Tripo e aguarda a conclusão da tarefa de geração. Uma tarefa típica leva cerca de 25 segundos. A autenticação é tratada automaticamente por meio das entradas ocultas do nó, portanto nenhuma chave de API do Tripo precisa ser fornecida no fluxo de trabalho. O nó exige todas as quatro URLs de vista na resposta do Tripo (`front_view_url`, `left_view_url`, `back_view_url`, `right_view_url`); se alguma vista estiver ausente, a execução falha com um erro.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `task_id multiview` | O identificador da tarefa retornado pelo Tripo para a solicitação de geração de imagem multiview. Pode ser usado para referenciar a tarefa concluída, por exemplo, ao refinar as vistas com Tripo: Edit Multiview. | MULTIVIEW_TASK_ID |
| `frente` | A vista frontal gerada do sujeito. | IMAGE |
| `esquerda` | A vista lateral esquerda gerada do sujeito. | IMAGE |
| `traseira` | A vista traseira gerada do sujeito. | IMAGE |
| `direita` | A vista lateral direita gerada do sujeito. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`
