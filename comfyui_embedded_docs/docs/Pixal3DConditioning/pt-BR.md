# Pixal3DConditioning

## Visão Geral

O nó Pixal3DConditioning foi projetado para preparar a condição de imagem para o pipeline de geração 3D Trellis2. Ele utiliza o modelo de visão DINOv3 para extrair características visuais da imagem de entrada em duas resoluções. Essas características são então organizadas em mapas de características por estágio, que podem ser opcionalmente melhorados com um modelo NAF. O nó também incorpora dados de câmera derivados do campo de visão horizontal para calcular a matriz de transformação de projeção. Ele gera um par de condição positiva que inclui os mapas de características derivados da imagem e dados de projeção, bem como um par de condição negativa com tensores de características zerados para guia sem classificador.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | O modelo de ClipVision DINOv3 ViT-L/16 usado para extração de características. | CLIP_VISION | Sim | — |
| `imagem` | A imagem pré-processada do nó ImageCropToMask, destinada ao Pixal3D com um fator de preenchimento de 1.1. | IMAGEM | Sim | — |
| `camera_angle_x` | O campo de visão horizontal em graus. Este parâmetro pode ser conectado a um nó MoGeGeometryToFOV para um campo de visão por imagem. Valor padrão: 49.13. | FLOAT | Sim | 1.0 – 170.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positivo` | A saída de condição positiva contendo os mapas de características derivados da imagem e dados de projeção para a geração Trellis2. | CONDIÇÃO |
| `negativo` | A saída de condição negativa com tensores de características zerados, usada para guia sem classificador. | CONDIÇÃO |

Nota: O valor de `camera_angle_x` é convertido para radianos internamente e usado para calcular a distância da câmera para a matriz de transformação de projeção. Quando o modelo de visão fornecido inclui um componente NAF, o nó também gera mapas de características de alta resolução para os estágios de forma e textura.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
