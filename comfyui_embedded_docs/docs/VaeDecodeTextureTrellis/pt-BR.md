# VaeDecodeTextureTrellis

Este nó decodifica um latente de textura Trellis2 em cores de voxels usando um VAE. O latente de entrada contém amostras de características esparsas com coordenadas; o nó reconstrói a cor para cada voxel e retorna o resultado como uma grade de voxels que nós downstream, como PaintMesh, podem usar para colorir uma malha 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `samples` | O latente de textura a ser decodificado. Contém amostras de características e coordenadas esparsas, e pode incluir metadados opcionais, como contagens de coordenadas, frame de modelo e resolução de coordenadas. | LATENT | Sim | — |
| `vae` | O VAE Trellis2 usado para decodificar o latente de textura em cores de voxels. | VAE | Sim | — |
| `shape_subdivides` | Informações de forma usadas para guiar a reconstrução de maior detalhe durante a decodificação. Ajuda a preservar a consistência da estrutura em resoluções mais altas. | SHAPE_SUBDIVIDES | Sim | — |

Nota: Quando o latente `samples` inclui contagens de coordenadas, as contagens devem ser não-negativas, seu total deve coincidir com o número de linhas de coordenadas e cada lote deve ter exatamente o número esperado de linhas; caso contrário, o nó gera um erro. Se o frame do modelo do latente for "z_up", as coordenadas de voxel decodificadas são remapeadas para Y-up para alinharem-se com os vértices da malha. Quando uma resolução de coordenada é fornecida, a resolução da textura de saída é esse valor multiplicado por 16; caso contrário, é inferida da maior coordenada de voxel e arredondada para um dos valores 256, 512, 1024, 1536 ou 2048 (1024 quando não há coordenadas disponíveis).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `voxel_colors` | Dados de voxel decodificados contendo coordenadas, características de cor e resolução de textura. Cada voxel possui 6 canais de cor: cor base (RGB), metálico, rugosidade e alfa, todos no intervalo [0, 1]. Consumidores de cor de vértice, como PaintMesh, usam os primeiros 3 canais. | VOXEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/pt-BR.md)

---
**Source fingerprint (SHA-256):** `952ea7d7a0147519392bebe352a0da731462db278c8640fa527aa5b6f64e4aa7`
