# Imagem para Vídeo ByteDance

# Nó ByteDance Image to Video

O nó ByteDance Image to Video gera um vídeo a partir de uma imagem de entrada e um prompt de texto usando a API da ByteDance. Ele cria uma sequência de vídeo que visualmente representa a descrição fornecida, com opções para personalizar a resolução, proporção de aspecto, duração e outros parâmetros de saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo ByteDance a ser usado para a geração de vídeo. As opções disponíveis são: <br>`"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` | STRING | Sim | Como listado acima |
| `prompt` | O prompt de texto usado para gerar o vídeo. Deve ter pelo menos 1 caractere após a remoção de espaços em branco. | STRING | Sim | - |
| `imagem` | A primeira imagem a ser usada para o vídeo. A imagem deve ter entre 300x300 e 6000x6000 pixels, com uma proporção de aspecto entre 0,4 e 2,5. | IMAGE | Sim | - |
| `resolução` | A resolução do vídeo de saída. As opções disponíveis são: <br>`"480p"`<br>`"720p"`<br>`"1080p"` | STRING | Sim | Como listado acima |
| `proporção` | A proporção de aspecto do vídeo de saída. As opções disponíveis são: <br>`"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | STRING | Sim | Como listado acima |
| `duração` | A duração do vídeo de saída em segundos. Para o modelo `seedance-1-5-pro-251215`, a duração mínima suportada é 4 segundos. | INT | Sim | 3 - 12 |
| `semente` | Semente a ser usada para a geração. Opcional, com valor padrão 0. | INT | Não | 0 - 2147483647 |
| `câmera fixa` | Especifica se deve fixar a câmera. A plataforma anexa uma instrução para fixar a câmera ao seu prompt, mas não garante o efeito real. Opcional, com valor padrão False. | BOOLEAN | Não | - |
| `marca d'água` | Se deve adicionar uma marca d'água "AI generated" ao vídeo. Opcional, com valor padrão False. | BOOLEAN | Não | - |
| `generate_audio` | Este parâmetro é ignorado para qualquer modelo exceto `seedance-1-5-pro-251215`. Opcional, com valor padrão False. | BOOLEAN | Não | - |

**Nota:** O prompt não deve conter as seguintes palavras (sem distinção de maiúsculas e minúsculas): `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Esses parâmetros são configurados via suas entradas dedicadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado com base na imagem de entrada e nos parâmetros do prompt. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9f4ad18642533689f9c664f2ca6a4ce8e92c8698754cdf9b6bb2d2735bc80415`
