# Converter RGB para YUV

# Imagem RGB para YUV

O nó ImageRGBToYUV realiza uma conversão de espaço de cor de RGB para YUV. Ele recebe uma imagem RGB como entrada e gera três imagens separadas representando os canais YUV: Y (luminância), U (diferença de azul) e V (diferença de vermelho).

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem RGB de entrada a ser convertida para o espaço de cor YUV. Esta deve ser uma imagem de 3 canais. | IMAGEM | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `Y`         | O canal Y representa a luminância (brilho) da imagem. | IMAGEM |
| `U`         | O canal U representa o componente de croma de diferença de azul. | IMAGEM |
| `V`         | O canal V representa o componente de croma de diferença de vermelho. | IMAGEM |

As imagens de saída terão as mesmas dimensões que a imagem de entrada.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
