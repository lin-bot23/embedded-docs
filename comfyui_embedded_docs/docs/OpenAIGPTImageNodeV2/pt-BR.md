# OpenAI GPT Image 2

Este nó gera imagens usando a API GPT Image da OpenAI. Ele suporta cinco modelos: `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5` e `gpt-image-1`. Também é possível anexar imagens de referência para edição de imagem e usar uma máscara para especificar quais partes de uma imagem devem ser substituídas.

## Entradas

### Entradas comuns

Estas entradas estão sempre visíveis.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo GPT Image da OpenAI a ser usado. Selecionar um modelo revela parâmetros adicionais específicos desse modelo. | DYNAMIC_COMBO | Sim | `"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Prompt textual para o GPT Image (padrão: `""`). | STRING | Sim | N/A |
| `n` | Número de imagens a gerar (padrão: `1`). | INT | Sim | 1 a 8 |
| `semente` | Semente para reprodutibilidade (padrão: `0`). Este parâmetro ainda não está implementado no backend. | INT | Sim | 0 a 2147483647 |

### Entradas do gpt-image-2.5-flare e gpt-image-2.5-sunburst

Estas entradas aparecem quando `model` é definido como `gpt-image-2.5-flare` ou `gpt-image-2.5-sunburst`. Ambos os modelos compartilham o mesmo conjunto de parâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem. Selecione "Custom" para usar largura e altura personalizadas (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `largura_personalizada` | Usado apenas quando `model.size` for "Custom". Deve ser múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `altura_personalizada` | Usado apenas quando `model.size` for "Custom". Deve ser múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Imagens de referência opcionais para edição de imagem. Até 16 imagens. Consulte Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

### Entradas do gpt-image-2

Estas entradas aparecem quando `model` é definido como `gpt-image-2`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem. Selecione "Custom" para usar largura e altura personalizadas (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `largura_personalizada` | Usado apenas quando `model.size` for "Custom". Deve ser múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `altura_personalizada` | Usado apenas quando `model.size` for "Custom". Deve ser múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imagens de referência opcionais para edição de imagem. Até 16 imagens. Consulte Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

### Entradas do gpt-image-1.5 e gpt-image-1

Estas entradas aparecem quando `model` é definido como `gpt-image-1.5` ou `gpt-image-1`. Ambos os modelos compartilham o mesmo conjunto de parâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imagens de referência opcionais para edição de imagem. Até 16 imagens. Consulte Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.images` | Slot expansível: conecte de 1 a N itens (por exemplo, `image_1`...`image_16`); até 16 imagens de referência para todos os modelos. | IMAGE | Não | 1 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

**Restrições e limitações dos parâmetros:**

- Quando `model.size` for "Custom" (apenas `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` e `gpt-image-2`), tanto `model.custom_width` quanto `model.custom_height` devem ser múltiplos de 16, o maior lado não pode exceder 3840, a proporção entre as dimensões não pode exceder 3:1 e o número total de pixels deve estar entre 655.360 e 8.294.400.
- `model.mask` exige exatamente uma imagem de referência em `model.images`: ela não pode ser usada sem uma imagem nem com mais de uma imagem.
- Quando `model.mask` for usada, a altura e a largura da máscara devem corresponder às da imagem de referência.
- Quando `model.images` for fornecido, o nó opera no modo de edição de imagem; sem `model.images`, ele gera imagens apenas com base no prompt.
- As imagens de referência e a máscara são reduzidas em escala antes de serem enviadas para a API.
- Os níveis de qualidade `"xhigh"` e `"max"` estão disponíveis apenas para `gpt-image-2.5-flare` e `gpt-image-2.5-sunburst`.
- A opção de fundo `"transparent"` está disponível para `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-1.5` e `gpt-image-1`, mas não para `gpt-image-2`.
- Atualmente, `seed` não está implementado no backend.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem ou as imagens geradas. Todas as imagens retornadas são empilhadas em um único lote; se as dimensões forem diferentes, elas são redimensionadas para corresponder à primeira imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4f77b79f9f432a1f2e0fd814012aebe7cc42a8aa983ee9a61f3b32984bf65148`
