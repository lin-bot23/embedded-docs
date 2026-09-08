# ByteDance Texto para Vídeo

O nó ByteDance Text to Video gera vídeos usando modelos da ByteDance por meio de uma API com base em prompts de texto. Ele recebe uma descrição de texto e vários ajustes de vídeo como entrada, então cria um vídeo que corresponda às especificações fornecidas. O nó lida com a comunicação da API e retorna o vídeo gerado como saída.

## Visão Geral

O nó ByteDance Text to Video foi projetado para converter prompts de texto em vídeos usando as capacidades de IA da ByteDance. Os usuários podem especificar o modelo, a resolução, a proporção de aspecto, a duração e outros parâmetros para controlar o processo de geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo da ByteDance a ser usado para a geração. | STRING | Sim | 
  - "seedance-1-5-pro-251215"
  - "seedance-1-0-pro-250528"
  - "seedance-1-0-pro-fast-251015" |
| `prompt` | O prompt de texto usado para gerar o vídeo. | STRING | Sim | Entrada de texto multilinha |
| `resolution` | A resolução do vídeo de saída. | STRING | Sim | 
  - "480p"
  - "720p"
  - "1080p" |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída. | STRING | Sim | 
  - "16:9"
  - "4:3"
  - "1:1"
  - "3:4"
  - "9:16"
  - "21:9" |
| `duration` | A duração do vídeo de saída em segundos. | INT | Sim | 3 a 12 segundos |
| `seed` | Semente a ser usada para a geração. | INT | Não | 0 a 2,147,483,647 |
| `camera_fixed` | Especifica se a câmera deve ser fixada. | BOOLEAN | Não | - |
| `watermark` | Se deve ser adicionado um selo "Gerado por IA" ao vídeo. | BOOLEAN | Não | - |
| `generate_audio` | Este parâmetro é ignorado para qualquer modelo exceto `seedance-1-5-pro-251215`. | BOOLEAN | Não | - |

**Restrições do Parâmetro:**

- O `prompt` deve conter pelo menos 1 caractere após a remoção de espaços em branco.
- O `prompt` não pode conter os seguintes parâmetros de texto: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- A `duration` é limitada a valores entre 3 e 12 segundos.
- Para o modelo `seedance-1-5-pro-251215`, a duração mínima suportada é de 4 segundos.
- O `seed` aceita valores de 0 a 2,147,483,647.
- O parâmetro `generate_audio` tem efeito apenas quando o `model` é configurado para `seedance-1-5-pro-251215`; ele é ignorado para todos os outros modelos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
