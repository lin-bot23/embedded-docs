# Normalizar Imagens

Este nó ajusta os valores de pixels de uma imagem de entrada usando um processo matemático de normalização. Ele subtrai um valor médio especificado de cada pixel e depois divide o resultado por um desvio padrão especificado. Esta é uma etapa comum de pré-processamento para preparar dados de imagem para outros modelos de aprendizado de máquina.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada a ser normalizada. | IMAGE | Sim | - |
| `mean` | Valor médio para normalização (padrão: 0.5). | FLOAT | Não | 0.0 - 1.0 |
| `std` | Desvio padrão para normalização (padrão: 0.5). | FLOAT | Não | 0.001 - 1.0 |

Nota: Quando a imagem de entrada inclui um canal alfa (transparência), o canal alfa não é normalizado. Ele é mantido inalterado na saída porque o alfa armazena transparência em vez de cor.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | A imagem resultante após o processo de normalização ter sido aplicado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/pt-BR.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
