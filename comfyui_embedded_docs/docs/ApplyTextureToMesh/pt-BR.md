# Aplicar Textura à Malha

Este nó anexa imagens de texturas pré-cozidas a uma malha de layout de UV, permitindo que sejam exportadas juntamente com a malha pelo nó SaveGLB. Conecte a mesma malha UV-desempacotada usada para pré-cozimento, juntamente com os mapas de imagens pré-cozidos. Mapas opcionais de metálico, rugosidade e oclusão são empacotados em uma única textura ORM, e fornecer um mapa normal também armazena os normais suaves e tangentes necessários para o iluminamento correto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha UV-desempacotada à qual as texturas pré-cozidas serão anexadas. Deve ser a mesma malha usada durante o pré-cozimento; um erro é gerado se a malha não tiver UVs. | MESH | Sim | — |
| `base_color` | A imagem de cor base pré-cozida. Armazenada como a textura da malha e limitada ao intervalo 0-1. | IMAGEM | Sim | — |
| `metallic` | O mapa metálico pré-cozido. Usado como o canal azul da textura combinada ORM; padrão é 0 quando não fornecido. | IMAGEM | Não | — |
| `roughness` | O mapa de rugosidade pré-cozido. Usado como o canal verde da textura combinada ORM; padrão é 1 quando não fornecido. | IMAGEM | Não | — |
| `occlusion` | O mapa de oclusão ambiental pré-cozido. Usado como o canal vermelho da textura combinada ORM; padrão é 1 quando não fornecido. Quando fornecido, a textura ORM é também marcada como a textura de oclusão para SaveGLB. | IMAGEM | Não | — |
| `normal_map` | O mapa normal pré-cozido no espaço tangente. Quando fornecido, o nó recalcula a base de tangente por vértice e exporta normais de vértice suaves para que o mapa normal iluminado corretamente. | IMAGEM | Não | — |

Nota: Quando qualquer um dos `metallic`, `roughness` ou `occlusion` estiver conectado, todos os três são empacotados em uma única textura glTF ORM com canais R = oclusão, G = rugosidade, B = metálico. Mapas ausentes são preenchidos com valores padrão (oclusão 1, rugosidade 1, metálico 0), e mapas com diferentes resoluções são redimensionados para a maior largura e altura. Quando `normal_map` estiver conectado, as normais da malha são substituídas por normais de vértice suaves calculadas e uma base de tangente é adicionada. Coordenadas UV que caem fora do intervalo [0,1] são escaladas uniformemente para [0,1] enquanto preservam o aspecto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha de entrada com as imagens de texturas anexadas ao seu layout de UV, pronta para ser salva pelo SaveGLB. | MESH | Sim |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7492922c9c7c0117366cb8b9017fc192eb8dd6b6594fd429044d60408693210e`
