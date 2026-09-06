# Carregar Vídeo

### Visão Geral

O nó Load Video carrega arquivos de vídeo do diretório de entrada e os torna disponíveis para processamento no fluxo de trabalho. Ele lê arquivos de vídeo do diretório de entrada designado e os exporta como dados de vídeo que podem ser conectados a outros nós de processamento de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `file` | O arquivo de vídeo a ser carregado do diretório de entrada. A lista suspensa é populada dinamicamente com todos os arquivos de vídeo encontrados na pasta de entrada do ComfyUI, e novos arquivos de vídeo podem ser carregados diretamente através do seletor de arquivos. | COMBO | Sim | Múltiplas opções disponíveis (todos os arquivos de vídeo no diretório de entrada) |

**Nota:** As opções disponíveis para o parâmetro `file` são populadas dinamicamente a partir dos arquivos de vídeo presentes no diretório de entrada. Apenas arquivos de vídeo com tipos de conteúdo suportados são exibidos. Você também pode carregar um novo arquivo de vídeo diretamente através da interface de seletor de arquivos do nó. Se um arquivo de vídeo previamente selecionado não puder ser encontrado, o nó reporta um erro de arquivo inválido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | Os dados de vídeo carregados que podem ser passados para outros nós de processamento de vídeo para manipulação ou análise adicional. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dcdd252792ade2a106c11826bbe7344011f0bc08506b80d634043a4dc156e076`
