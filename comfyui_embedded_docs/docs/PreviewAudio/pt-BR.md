# Pré-visualizar Áudio

### Visão Geral

O nó Preview Audio permite que você ouça áudio diretamente na interface do ComfyUI sem salvá-lo no diretório de saída. Ele recebe dados de áudio como entrada, verifica se eles estão presentes e os passa em seguida, mostrando um player de áudio temporário para que você possa ouvir o resultado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `audio` | Os dados de áudio a serem visualizados. O nó levanta um ValueError se a entrada for None, o que pode acontecer quando o vídeo de origem não possui faixa de áudio. | AUDIO | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `áudio` | Os dados de áudio passados em seguida sem alteração da entrada. | AUDIO |
| `ui` | Exibe um widget de player de áudio na interface para visualização do áudio. | UI |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`
