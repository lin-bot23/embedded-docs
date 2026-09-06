# Gerar Textura a Partir de Voxel

### Visão Geral

Este nó aplica texturas PBR em uma malha 3D usando o layout de UV existente da malha. Ele amostra atributos de cor e material de um volume voxel ralo em cada texel e gera uma imagem de cor base mais mapas de metálico e rugosidade. Ele não desdobra a malha, então um nó de desdobramento de UV deve ser conectado no fluxo ascendente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha 3D em que as texturas serão aplicadas. Deve já ter um layout de UV; um nó de desdobramento de UV deve ser conectado no fluxo ascendente. | MESH | Sim | |
| `voxel_colors` | Volume voxel ralo contendo cores por voxel e atributos PBR opcionais (canais de metálico e rugosidade). | VOXEL | Sim | |
| `texture_size` | Resolução quadrada do atlas UV (nome exibido: "resolução", padrão: 2048). | INT | Sim | 64 a 8192 |
| `reference_mesh` | Malha pré-decimada densa opcional; projeta cada texel para sua superfície real antes da amostragem, removendo o desdobramento facetado em malhas grossas. | MESH | Não | |

Notas:

- A malha de entrada deve ter UVs. Se não houver UVs, o nó gera um erro. Os UVs devem ser 1:1 com os vértices (um UV por vértice).
- Quando a malha e os coordenadas voxel contêm uma dimensão de lote, cada item do lote é desdobrado separadamente. Se um item do lote não tiver voxels ou faces, ele é pulado e uma textura preta é emitida para ele.
- Quando `reference_mesh` é fornecido para um lote, ele é mapeado pelo índice do lote, a menos que ele contenha apenas uma malha, no qual caso essa malha é usada para todos os itens.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `base_color` | Mapa de textura de cor base RGB. Valores são float na faixa 0–1. | IMAGEM |
| `metallic` | Mapa metálico em escala de cinza (float, 0–1). Preto quando as cores voxel não contêm canal metálico. | IMAGEM |
| `roughness` | Mapa de rugosidade em escala de cinza (float, 0–1). Preto quando as cores voxel não contêm canal de rugosidade. | IMAGEM |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`
