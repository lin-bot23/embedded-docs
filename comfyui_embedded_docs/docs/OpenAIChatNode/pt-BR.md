# OpenAI ChatGPT

Este nó gera respostas de texto a partir de um modelo da OpenAI. Ele recebe um prompt de texto e, opcionalmente, imagens ou arquivos como contexto, e então envia essa informação para um modelo da OpenAI para gerar uma resposta de texto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Entradas de texto para o modelo, usadas para gerar uma resposta. Este é o texto que você deseja que o modelo responda. | STRING | Sim | - |
| `persist_context` | Este parâmetro está obsoleto e não tem efeito. Ele é incluído para compatibilidade reversa, mas não influencia o comportamento do nó. | BOOLEAN | Não | - |
| `model` | O modelo usado para gerar a resposta. Selecione entre os modelos da OpenAI disponíveis. | COMBO | Sim | gpt-6-astra<br>gpt-5.6-sol<br>gpt-5.6-terra<br>gpt-5.6-luna<br>gpt-5.5-pro<br>gpt-5.5<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br>gpt-4.1<br>gpt-4.1-mini<br>gpt-4.1-nano<br>o4-mini<br>o3<br>o1-pro<br>o1 |
| `images` | Imagem(s) opcional(ais) para usar como contexto para o modelo. Para incluir múltiplas imagens, você pode usar o nó Batch Images. | IMAGE | Não | - |
| `files` | Arquivo(s) opcional(ais) para usar como contexto para o modelo. Aceita entradas do nó OpenAI Chat Input Files. | OPENAI_INPUT_FILES | Não | - |
| `advanced_options` | Configuração opcional para o modelo. Aceita entradas do nó OpenAI Chat Advanced Options. | OPENAI_CHAT_CONFIG | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output_text` | A resposta de texto gerada pelo modelo da OpenAI. Este é o texto gerado com base no prompt de entrada e contexto. | STRING |

## Notas

- O parâmetro `persist_context` está obsoleto e não tem efeito. Ele é incluído para compatibilidade reversa, mas não deve ser usado.
- A entrada `images` pode ser usada para fornecer contexto adicional ao modelo. Se múltiplas imagens forem fornecidas, elas devem ser conectadas usando o nó Batch Images.
- A entrada `files` permite fornecer contexto adicional na forma de arquivos. Esses arquivos devem ser conectados do nó OpenAI Chat Input Files.
- A entrada `advanced_options` permite uma configuração mais detalhada do comportamento do modelo. Isso deve ser conectado do nó OpenAI Chat Advanced Options.
- O preço para usar este nó depende do modelo selecionado. O custo é calculado com base no número de tokens usados pelo modelo. O custo exato será exibido na interface do usuário do nó.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `687a6b1110518a2eaf23e240f43991b4ff91d6f01cae6c3ef55bcdac810e7a89`
