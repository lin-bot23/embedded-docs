# Opções Avançadas do OpenAI ChatGPT

O nó OpenAIChatConfig permite que você defina opções avançadas que controlam como o Nó de Chat OpenAI gera respostas. Você pode definir a estratégia de truncamento, limitar o número de tokens de saída, fornecer instruções personalizadas e escolher o quanto o modelo deve raciocinar antes de responder.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `truncation` | A estratégia de truncamento a ser usada para a resposta do modelo. auto: Se o contexto desta resposta e das anteriores exceder o tamanho da janela de contexto do modelo, o modelo truncará a resposta para caber na janela de contexto, descartando itens de entrada no meio da conversa. disabled: Se uma resposta do modelo exceder o tamanho da janela de contexto de um modelo, a solicitação falhará com um erro 400 (padrão: "auto") | COMBO | Sim | "auto"<br>"disabled" |
| `max_output_tokens` | Um limite superior para o número de tokens que podem ser gerados em uma resposta, incluindo tokens de saída visíveis e tokens de raciocínio (padrão: 4096) | INT | Não | 16 a 16384 |
| `instructions` | Instruções para o modelo sobre como gerar a resposta (entrada multilinha suportada) | STRING | Não | - |
| `reasoning_effort` | O quanto o modelo raciocina antes de responder. "default" deixa a escolha para o modelo. Os níveis suportados variam conforme o modelo: GPT-6 Astra de low a max, GPT-5.6 de none a max (sem minimal), GPT-5.5 de none a xhigh, GPT-5.5 Pro de medium a xhigh, GPT-5 de minimal a high, série o de low a high; GPT-4.1 não tem raciocínio. Níveis não suportados são rejeitados antes do envio da solicitação. (padrão: "default") | COMBO | Não | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

Nota: Embora `top_p` e `temperature` sejam listados como propriedades na especificação da API, eles não são suportados para todos os modelos e, portanto, não são expostos como entradas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | Objeto de configuração contendo as configurações especificadas para uso com os Nós de Chat OpenAI | OPENAI_CHAT_CONFIG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/pt-BR.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
