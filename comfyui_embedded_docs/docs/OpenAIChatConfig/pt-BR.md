# Opções Avançadas do OpenAI ChatGPT

# Opções Avançadas do ChatGPT da OpenAI

O nó Opções Avançadas do ChatGPT da OpenAI permite que você configure adicionalmente os nós do ChatGPT da OpenAI. Este nó oferece configurações avançadas que controlam como o modelo gera respostas, incluindo comportamento de truncagem, limites de comprimento de saída e instruções personalizadas.

## Visão Geral

O nó Opções Avançadas do ChatGPT da OpenAI foi projetado para aprimorar a funcionalidade dos nós do ChatGPT da OpenAI, permitindo que os usuários especifiquem opções de configuração avançadas. Essas configurações podem ajudar a ajustar a geração de respostas do modelo para requisitos específicos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `truncation` | Estratégia de truncagem a ser usada para a resposta do modelo. auto: Se o contexto dessa resposta e das anteriores exceder o tamanho da janela de contexto do modelo, o modelo truncará a resposta para se encaixar na janela de contexto, descartando itens de entrada no meio da conversa. disabled: Se uma resposta do modelo exceder o tamanho da janela de contexto de um modelo, a solicitação falhará com um erro 400 (padrão: "auto") | STRING | Sim | "auto"<br>"disabled" |
| `max_output_tokens` | Limite superior para o número de tokens que podem ser gerados para uma resposta, incluindo tokens visíveis e tokens de raciocínio (padrão: 4096) | INT | Não | 16 a 16384 |
| `instructions` | Instruções para o modelo sobre como gerar a resposta (suporta entrada em múltiplas linhas) | STRING | Não | - |
| `reasoning_effort` | Quanto o modelo raciocina antes de responder. 'default' deixa a escolha para o modelo. Os níveis suportados diferem por modelo: GPT-6 Astra low-max, GPT-5.6 none-max (sem mínimo), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high; GPT-4.1 não tem raciocínio. Níveis não suportados são rejeitados antes de a solicitação ser enviada (padrão: "default") | STRING | Não | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | Objeto de configuração contendo as configurações especificadas para uso com os nós do ChatGPT da OpenAI | OPENAI_CHAT_CONFIG |

## Notas

- O parâmetro `max_output_tokens` define um limite superior para o número total de tokens, incluindo tokens visíveis e tokens de raciocínio.
- O parâmetro `reasoning_effort` permite que você especifique o nível de raciocínio que o modelo deve aplicar antes de gerar uma resposta. Os níveis suportados variam dependendo do modelo usado.
- O parâmetro `instructions` pode ser usado para fornecer instruções detalhadas ao modelo para guiar o processo de geração de respostas.
- O parâmetro `truncation` determina se o modelo deve truncar automaticamente a resposta se ela exceder o tamanho da janela de contexto ou falhar com um erro 400.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/pt-BR.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
