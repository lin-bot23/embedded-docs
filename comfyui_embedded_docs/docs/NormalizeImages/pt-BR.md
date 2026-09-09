# Normalizar Imagens

Este nó ajusta os valores dos pixels de uma imagem de entrada usando um processo de normalização matemática. Subtrai um valor médio especificado de cada pixel e, em seguida, divide o resultado pela desvio padrão especificada. Este é um passo comum de pré-processamento para preparar dados de imagem para outros modelos de aprendizado de máquina. Se a imagem de entrada tiver um canal alfa, o canal alfa é passado inalterado, preservando a transparência.

## Visão Geral

O nó Normalizar Imagens normaliza as cores de uma imagem de entrada ajustando seus valores de pixel com base em um valor médio e desvio padrão. Este processo é útil para padronizar dados de imagem antes de aplicar algoritmos de aprendizado de máquina.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image`   | A imagem de entrada a ser normalizada. | IMAGEM | Sim | - |
| `mean`    | Valor médio para a normalização. | FLOAT | Não | 0.0 - 1.0 (padrão: 0.5) |
| `std`     | Desvio padrão para a normalização. | FLOAT | Não | 0.001 - 1.0 (padrão: 0.5) |

Os parâmetros `mean` e `std` são usados para normalizar os valores de pixel da imagem de entrada. Os valores padrão para ambos os parâmetros são definidos como 0.5, o que é uma escolha comum para a normalização.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `images`     | A imagem resultante após a aplicação do processo de normalização. | IMAGEM |

A saída do nó Normalizar Imagens é a imagem normalizada. Os valores de pixel são ajustados de acordo com o valor médio e o desvio padrão especificados, e o canal alfa (se presente) é preservado.

## Nota

O nó Normalizar Imagens foi projetado para lidar com qualquer tamanho de lote de imagens, tornando-o adequado para tarefas de processamento em lote.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/pt-BR.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
