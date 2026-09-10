# ModelPatchLoader

O nó ModelPatchLoader carrega um arquivo de patch de modelo da pasta `model_patches` e o prepara para uso em um fluxo de trabalho. Ele detecta automaticamente o tipo de patch contido no arquivo, constrói a arquitetura correspondente, carrega os pesos salvos e envolve tudo em um model patcher para que possa ser aplicado a outros modelos. Ele suporta muitos formatos de patch especializados, incluindo ramificações extras de ControlNet, modelos de incorporação de recursos, adaptadores e módulos semelhantes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `nome` | O nome do arquivo do patch de modelo a ser carregado do diretório model_patches. Selecione um dos arquivos de patch disponíveis na lista. | COMBO | Sim | Lista gerada dinamicamente de todos os arquivos de patch de modelo encontrados na pasta `model_patches` |

Nota: Este nó está marcado como experimental. O tipo de patch é detectado automaticamente a partir do conteúdo do arquivo, portanto, nenhuma seleção manual de tipo é necessária.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL_PATCH` | O patch de modelo carregado encapsulado em um ModelPatcher, pronto para ser aplicado a um modelo no fluxo de trabalho | MODEL_PATCH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `069f40b1f108ecd74fc58c12aa2f74edff07f743aa1ed6352ff7bcf0c39341d4`
