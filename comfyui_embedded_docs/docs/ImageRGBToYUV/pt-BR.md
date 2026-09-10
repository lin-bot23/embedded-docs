# Converter RGB para YUV

O nó ImageRGBToYUV converte uma imagem RGB para o espaço de cores YUV. Ele divide a imagem em três componentes — Y (luminância, ou brilho), U (croma de diferença de azul) e V (croma de diferença de vermelho) — e retorna cada componente como uma imagem separada, do mesmo tamanho da entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem RGB de entrada para converter em YUV. Se a imagem contiver um canal alfa, apenas os três primeiros canais (RGB) são usados. | IMAGE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `Y` | O componente de luminância (brilho) do espaço de cores YUV | IMAGE |
| `U` | O componente croma de diferença de azul do espaço de cores YUV | IMAGE |
| `V` | O componente croma de diferença de vermelho do espaço de cores YUV | IMAGE |

Cada saída possui a mesma largura, altura e número de canais que a imagem de entrada. O componente Y, U ou V correspondente é repetido em todos os canais para que cada saída seja retornada como uma imagem padrão.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
