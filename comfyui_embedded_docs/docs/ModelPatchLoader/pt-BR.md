# ModelPatchLoader

O nó ModelPatchLoader carrega um arquivo de patch de modelo da pasta `model_patches` e prepara-o para uso em um fluxo de trabalho. Ele detecta automaticamente o tipo de patch contido no arquivo, constrói a arquitetura correspondente, carrega os pesos salvos e envolve tudo em um patcher de modelo, permitindo que seja aplicado a outros modelos. Ele suporta muitos formatos de patch especializados, incluindo ramos adicionais do ControlNet, modelos de embedder de características, adaptadores e módulos semelhantes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `nome` | O nome do arquivo do patch de modelo a ser carregado da pasta model_patches. Selecione um dos arquivos de patch disponíveis na lista. | COMBO | Sim | Lista gerada dinamicamente de todos os arquivos de patch de modelo encontrados na pasta model_patches |

Nota: Este nó está marcado como experimental. O tipo de patch é detectado automaticamente a partir do conteúdo do arquivo, portanto, não há necessidade de seleção manual do tipo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL_PATCH` | O patch de modelo carregado envolto em um ModelPatcher, pronto para ser aplicado a um modelo no fluxo de trabalho | MODEL_PATCH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `069f40b1f108ecd74fc58c12aa2f74edff07f743aa1ed6352ff7bcf0c39341d4`
