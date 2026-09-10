# Pixal3DConditioning

Este nó prepara o condicionamento de imagem para o pipeline de geração 3D do Trellis2. Ele extrai características visuais da imagem de entrada com um modelo de visão DINOv3 em duas resoluções, organiza-as em mapas de características por estágio (opcionalmente aprimorados com um modelo NAF) e os combina com dados de câmera derivados do campo de visão horizontal. Ele produz um par de condicionamentos positivo e negativo, em que o negativo usa características zeradas para orientação livre de classificador.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Sim | — |
| `imagem` | Imagem pré-processada do ImageCropToMask (pad_factor=1.1 para Pixal3D). | IMAGE | Sim | — |
| `camera_angle_x` | FOV horizontal em graus (nome de exibição: fov). Conecte um MoGeGeometryToFOV (axis='horizontal', unit='degrees') para um FoV por imagem (corresponde ao padrão upstream). Padrão: 49.13. | FLOAT | Sim | 1.0 – 170.0 |

Observação: O valor de `camera_angle_x` é convertido internamente para radianos e usado para calcular a distância da câmera para a matriz de transformação de projeção. Quando o modelo de visão fornecido inclui um componente NAF, o nó também produz mapas de características de alta resolução para os estágios de forma e textura.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `positivo` | Condicionamento positivo contendo os mapas de características derivados da imagem e os dados de projeção para a geração do Trellis2. | CONDITIONING |
| `negativo` | Condicionamento negativo com tensores de características zerados, usado para orientação livre de classificador. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
