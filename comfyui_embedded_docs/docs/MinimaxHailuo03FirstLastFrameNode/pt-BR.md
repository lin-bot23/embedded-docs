# MiniMax H3 Primeiro-Último-Frame para Vídeo

Este nó gera um vídeo a partir de uma imagem de primeiro frame e, opcionalmente, uma imagem de último frame, usando modelos MiniMax H3. O seletor de `model` altera quais configurações e restrições de geração se aplicam, e a proporção da imagem gerada segue a das imagens fornecidas.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar para a geração de vídeo. A seleção de um modelo revela suas configurações específicas do modelo abaixo. | COMBO DINÂMICO | Sim | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `first_frame` | Imagem de primeiro frame para o vídeo. O vídeo gerado segue a proporção dessa imagem. | IMAGEM | Sim | - |
| `last_frame` | Imagem de último frame opcional para o vídeo. Quando fornecida, o vídeo é gerado do primeiro frame até esse último frame. | IMAGEM | Não | - |
| `seed` | Semente aleatória. A mesma solicitação com a mesma semente gera resultados semelhantes, mas não garantidamente idênticos. Inclui uma opção "controle após geração". Padrão: 42. | INTEIRO | Sim | 0 a 4294967295 |
| `watermark` | Se adicionar um selo AIGC ao vídeo. Este é um parâmetro avançado. Somente suportado pelo modelo `MiniMax H3`. Padrão: Falso. | BOOLEANO | Sim | Sim<br>Falso |

### Entradas do MiniMax H3

Essas configurações são exibidas quando `MiniMax H3` é selecionado no seletor de `model`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texto de sinal para a geração de vídeo. Deve conter pelo menos um caractere não branco. | STRING | Sim | Texto de múltiplas linhas |
| `resolution` | Resolução do vídeo de saída. | COMBO | Sim | "768P"<br>"2K" |
| `duration` | Duração do vídeo de saída em segundos. Padrão: 5. | INTEIRO | Sim | 4 a 15 |

### Entradas do MiniMax H3 Max e MiniMax H3 Max Turbo

Essas configurações são exibidas quando `MiniMax H3 Max` ou `MiniMax H3 Max Turbo` é selecionado no seletor de `model`. Ambos os modelos expõem as mesmas configurações.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texto de sinal para a geração de vídeo. Não deve estar vazio ou composto apenas de espaços em branco e é limitado a 50.000 caracteres. | STRING | Sim | Texto de múltiplas linhas |
| `resolution` | Resolução do vídeo de saída. Padrão: 768P. | COMBO | Sim | "480P"<br>"768P" |
| `duration` | Duração do vídeo de saída em segundos. Padrão: 5. | INTEIRO | Sim | 5 a 15 |
| `prompt_expansion_mode` | Quanto esforço é gasto na reescrever o sinal antes da geração. Padrão: equilibrado. | COMBO | Sim | "equilibrado"<br>"qualidade" |

**Notas sobre restrições:**

- O sinal deve conter texto: sinal vazio ou composto apenas de espaços em branco é rejeitado.
- Qualquer imagem de frame fornecida deve ter pelo menos 256 pixels de largura e 256 pixels de altura, com uma proporção largura-altura entre 0,4 e 2,5 (aproximadamente 2:5 a 5:2). Esta exigência se aplica a `first_frame` e, quando fornecida, `last_frame`.
- Quando `last_frame` é omitido, o vídeo é gerado a partir do primeiro frame apenas.
- O vídeo de saída segue a proporção das imagens fornecidas.
- `watermark` é suportado apenas pelo `MiniMax H3`. Ativar com `MiniMax H3 Max` ou `MiniMax H3 Max Turbo` gera um erro.
- O intervalo de duração vai de 4 a 15 segundos para `MiniMax H3` e de 5 a 15 segundos para `MiniMax H3 Max` e `MiniMax H3 Max Turbo`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | Vídeo gerado a partir do primeiro frame e, opcionalmente, do último frame usando o modelo MiniMax H3 selecionado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6eaf895e6e9e46b9a1efb1dd13e951040e12e865cc73d7741ab7546f5f8f9ec0`
