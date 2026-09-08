# ImageYUVToRGB

# Imagem YUV para RGB

O nó ImageYUVToRGB é projetado para converter imagens do espaço de cor YUV para o espaço de cor RGB. Ele faz isso ao tomar três imagens de entrada separadas que representam os canais Y (luminância), U (projeção azul) e V (projeção vermelha) da imagem. Esses canais são então combinados em uma única imagem RGB usando uma técnica de conversão de espaço de cor.

## Visão Geral

O nó ImageYUVToRGB converte imagens YUV para imagens RGB, combinando os canais Y, U e V. Isso é útil para aplicações que requerem conversão de espaço de cor entre esses dois padrões.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `Y`       | A imagem de entrada do canal Y, representando a informação de luminância. | IMAGEM | Sim | - |
| `U`       | A imagem de entrada do canal U, representando a diferença de cor azul. | IMAGEM | Sim | - |
| `V`       | A imagem de entrada do canal V, representando a diferença de cor vermelha. | IMAGEM | Sim | - |

**Nota:** Os canais Y, U e V devem ser fornecidos juntos e devem ter as mesmas dimensões para garantir uma conversão correta.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output`    | A imagem RGB resultante após a conversão YUV para RGB. | IMAGEM |

A imagem de saída terá as mesmas dimensões das imagens de entrada Y, U e V, mas com a informação de cor representada no espaço de cor RGB.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/pt-BR.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
