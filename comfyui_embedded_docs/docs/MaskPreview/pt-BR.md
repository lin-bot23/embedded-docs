# Pré-visualizar Mask

### Visão Geral

O nó MaskPreview exibe uma prévia visual dos dados da máscara diretamente na interface do ComfyUI, sem salvá-la no diretório de saída. Isso permite que você insira a máscara em qualquer ponto do seu fluxo de trabalho, enquanto a máscara também passa inalterada pelo nó, permitindo que continue a ser usada em outras partes do processo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mask` | Dados da máscara para prévia | MÁSCARA | Sim | - |
| `filename_prefix` | Prefixo do nome do arquivo usado para a prévia (padrão: "ComfyUI") | STRING | Não | - |
| `prompt` | Informações de prompt para metadados (fornecidas automaticamente) | PROMPT | Não | - |
| `extra_pnginfo` | Informações adicionais PNG para metadados (fornecidas automaticamente) | EXTRA_PNGINFO | Não | - |

Apenas `mask` é uma entrada visível que precisa ser conectada. Os parâmetros `filename_prefix`, `prompt` e `extra_pnginfo` são fornecidos pelo sistema: `filename_prefix` recolhe seu valor padrão, enquanto `prompt` e `extra_pnginfo` são ocultos e fornecidos automaticamente pelo runtime do ComfyUI.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mask` | Mesmos dados da máscara que foram previstos, retornados inalterados para que possam ser usados em outras partes do fluxo de trabalho | MÁSCARA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fb7abe8cb6b5ac8a6a38e88ef90a146d16caf41d24c5de95309a94bc3c371d75`
