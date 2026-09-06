# MiniMax H3 Referência para Vídeo

Este nó gera um vídeo usando os modelos MiniMax H3, condicionado por imagens, vídeos e áudio de referência. As referências são mencionadas no prompt pela ordem de conexão: "Image 1", "Image 2", "Video 1", "Audio 1" e assim por diante. Dois modelos estão disponíveis: "MiniMax H3" e "MiniMax H3 Max".

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar para a geração de vídeo (padrão: "MiniMax H3"). Ao selecionar "MiniMax H3", são fornecidas as entradas de geração e referência do MiniMax H3. Ao selecionar "MiniMax H3 Max", são fornecidas as entradas de geração e referência do MiniMax H3 Max. | COMBO DINÂMICO | Sim | "MiniMax H3"<br>"MiniMax H3 Max" |
| `seed` | Semente aleatória. A mesma solicitação com a mesma semente gera resultados semelhantes, mas não garantidamente idênticos (padrão: 42). | INTEIRO | Sim | 0 a 4294967295 |
| `watermark` | Se adicionar uma marca d'água AIGC ao vídeo (padrão: falso). Suportado apenas pelo modelo MiniMax H3. | BOOLEANO | Não | verdadeiro<br>falso |

### Entradas do MiniMax H3

Essas entradas estão disponíveis quando "MiniMax H3" é selecionado como o modelo.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração de vídeo. Mídia de referência pode ser mencionada por sua ordem, por exemplo "Image 1", "Image 2", "Video 1" ou "Audio 1". | STRING | Sim | Mínimo 1 caractere |
| `resolution` | Resolução do vídeo de saída (padrão: "768P"). | COMBO | Sim | "768P"<br>"2K" |
| `ratio` | Relação de aspecto do vídeo de saída (padrão: "adaptive"). | COMBO | Sim | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5). | INTEIRO | Sim | 4 a 15 |

### Entradas do MiniMax H3 Max

Essas entradas estão disponíveis quando "MiniMax H3 Max" é selecionado como o modelo.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração de vídeo. Mídia de referência pode ser mencionada por sua ordem, por exemplo "Image 1", "Image 2", "Video 1" ou "Audio 1". | STRING | Sim | 1 a 50000 caracteres |
| `resolution` | Resolução do vídeo de saída (padrão: "768P"). | COMBO | Sim | "480P"<br>"768P" |
| `ratio` | Relação de aspecto do vídeo de saída (padrão: "adaptive"). | COMBO | Sim | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Duração do vídeo de saída em segundos (padrão: 5). | INTEIRO | Sim | 5 a 15 |
| `prompt_expansion_mode` | Quanto esforço é gasto na reescrever o prompt antes da geração (padrão: "balanced"). | COMBO | Sim | "balanced"<br>"quality" |
| `reference_detail` | Nível de detalhe no qual as imagens de referência são enviadas. "high" envia-as no maior tamanho que o modelo usa (até um lado curto de 2048 pixels); "standard" reduz-as a no máximo 2048x1024 para reduzir o custo de referência (padrão: "standard"). | COMBO | Sim | "high"<br>"standard" |

### Entradas de referência

Essas entradas de referência são compartilhadas por ambos os modelos. Cada uma é um slot crescível.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot crescível: conecte até 9 itens (`image_1`...`image_9`). Imagens de referência de sujeito ou estilo, mencionadas no prompt como "Image 1"..."Image 9" na ordem de conexão. Até 9 imagens. | IMAGEM | Não | 0 a 9 imagens |
| `reference_videos` | Slot crescível: conecte até 3 itens (`video_1`...`video_3`). Vídeos de referência de movimento ou cena, mencionados no prompt como "Video 1"..."Video 3" na ordem de conexão. Até 3 vídeos, de 2-15 segundos cada, com um total de 15 segundos. | VÍDEO | Não | 0 a 3 vídeos |
| `reference_audios` | Slot crescível: conecte até 3 itens (`audio_1`...`audio_3`). Referências de áudio, mencionadas no prompt como "Audio 1"..."Audio 3" na ordem de conexão. Até 3 clips, de 2-15 segundos cada, com um total de 15 segundos. Não pode ser usado sem uma imagem ou vídeo de referência. | ÁUDIO | Não | 0 a 3 clips |

### Restrições de parâmetros

- Pelo menos uma imagem de referência ou um vídeo de referência é obrigatório. O áudio de referência sozinho não é aceito.
- Cada imagem de referência deve ter uma relação de aspecto entre aproximadamente 0,4 e 2,5 (2:5 a 5:2) e uma largura e altura mínima de 256 pixels.
- Cada vídeo de referência deve ter uma duração entre 2 e 15 segundos com uma taxa de quadros entre 23,976 e 60 FPS. A duração total de todos os vídeos de referência não pode exceder 15 segundos.
- Cada clip de áudio de referência deve ter uma duração entre 2 e 15 segundos. A duração total de todos os clips de áudio de referência não pode exceder 15 segundos.
- Quando "MiniMax H3 Max" é selecionado, a configuração `watermark` deve ser desativada.
- Quando "MiniMax H3 Max" é selecionado, o número total de arquivos de referência (imagens, vídeos e áudio combinados) não pode exceder 12.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado. | VÍDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b77eedb1f7757e60518c04484f1cc24c27cf6886b3ae31c15207ea49fd436a73`
