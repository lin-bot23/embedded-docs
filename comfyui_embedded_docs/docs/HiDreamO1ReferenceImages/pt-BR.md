# Imagens de Referência HiDream-O1

Este nó anexa imagens de referência tanto ao condicionamento positivo quanto ao negativo, permitindo que nós downstream as utilizem para guiar a geração. As imagens de referência são aplicadas na ordem numérica de suas entradas de soquetes. Se nenhuma imagem de referência estiver conectada, o condicionamento positivo e negativo passam inalterados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | O condicionamento positivo ao qual anexar imagens de referência. | CONDITIONING | Sim | - |
| `negative` | O condicionamento negativo ao qual anexar imagens de referência. | CONDITIONING | Sim | - |
| `images` | As imagens de referência são usadas na ordem numérica dos soquetes. Quando imagens são fornecidas, elas são anexadas tanto ao condicionamento positivo quanto ao negativo. | IMAGE | Não | 0 a 100 imagens (`image_1` a `image_100`) |

**Nota sobre o parâmetro `images`:** Este é um entrada aut crescente que fornece soquetes numerados `image_1` até `image_100`. As imagens são usadas na ordem numérica dos soquetes. A entrada é opcional: se nenhuma imagem de referência estiver conectada, o nó retorna o condicionamento positivo e negativo inalterados. Quando imagens são conectadas, o mesmo conjunto de imagens de referência é anexado aos dois outputs, e o condicionamento negativo é também marcado como negativo antes das imagens serem anexadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo com as imagens de referência anexadas. | CONDITIONING |
| `negative` | O condicionamento negativo com as imagens de referência anexadas. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/pt-BR.md)

---
**Source fingerprint (SHA-256):** `07f9f0ea19957523e95d04b9086dc994807bb0cd5262fe798dc784c1ecb4920d`
