# OpenAI Sora - Vídeo

### Visão Geral

O nó OpenAIVideoSora2 gera vídeos usando os modelos Sora da OpenAI. Ele cria conteúdo de vídeo com base em um prompt de texto e uma imagem de referência opcional, então entrega o vídeo gerado como sua saída. O nó suporta diferentes durações e resoluções de vídeo dependendo do modelo selecionado.

**AVISO DE DEPRECAÇÃO:** A OpenAI vai parar de oferecer a API Sora v2 em setembro de 2026. Esse nó será removido do ComfyUI nessa data.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo OpenAI Sora a ser usado para a geração de vídeos (padrão: "sora-2") | COMBO | Sim | "sora-2"<br>"sora-2-pro" |
| `prompt` | Texto orientador; pode estar vazio se uma imagem de entrada estiver presente (padrão: vazio) | STRING | Sim | - |
| `size` | A resolução do vídeo gerado (padrão: "1280x720") | COMBO | Sim | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duration` | A duração do vídeo gerado em segundos (padrão: 8) | COMBO | Sim | 4<br>8<br>12 |
| `image` | Imagem de referência opcional usada para a geração de vídeos (ajuste, personagem, cena de referência, etc.); apenas uma única imagem é suportada | IMAGE | Não | - |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados são não determinísticos independentemente do valor da semente (padrão: 0) | INT | Não | 0 a 2147483647 |

**Restrições e Limitações:**

- O modelo "sora-2" suporta apenas as resoluções "720x1280" e "1280x720"; as opções "1024x1792" e "1792x1024" são válidas apenas com o modelo "sora-2-pro"
- Quando uma imagem é conectada, ela deve conter exatamente uma imagem; conectar mais de uma imagem gera um erro
- Os resultados são não determinísticos independentemente do valor da semente

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado pelo OpenAI Sora | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
