# MiniMax H3 Referência para Vídeo

## Inputs

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modelo CLIP usado para tokenizar o prompt e codificar os meios de referência em tokens de condição. | CLIP | Sim | |
| `vae` | VAE de vídeo usado para codificar imagens de referência e quadros de vídeo de referência. Sem ele, imagens e vídeos de referência apenas condicionam o encoder de texto. | VAE | Não | |
| `audio_vae` | VAE de áudio usado para codificar áudio de referência. O áudio é resampled para a taxa de amostragem do VAE de áudio (32 kHz por padrão). Sem ele, o áudio de referência apenas condiciona o encoder de texto. | VAE | Não | |
| `prompt` | Prompt de texto para o vídeo. Meios de referência podem ser mencionados com tags `<Picture i>`, `<Video k>`, e `<Audio j>` (baseado em 1 para cada tipo). Suporta prompts multilinha e dinâmicos. | STRING | Sim | |
| `largura` | Largura do vídeo gerado em pixels (padrão: 1344). | INT | Sim | 32 a 16384 (passo 32) |
| `altura` | Altura do vídeo gerado em pixels (padrão: 768). | INT | Sim | 32 a 16384 (passo 32) |
| `duração` | Número de quadros em 24 fps; 124 = ~5s, o intervalo treinado é ~124-362 (padrão: 124). | INT | Sim | 5 a 3600 (passo 17) |
| `tamanho_imagem_ref` | Tamanho da imagem de referência. `match` escala cada imagem de referência apenas para a área de pixels da geração, mantendo a proporção, enquanto `max` usa a borda curta de 2048px da pipeline de referência para a melhor fidelidade de identidade. Os tokens de referência passam por cada passo de amostragem, então `max` pode ser várias vezes mais lento (padrão: `match`). | COMBO | Sim | `"match"`<br>`"max"` |
| `imagens_ref` | Espaço crescente: conecte até 9 imagens de referência (`ref_image_1` ... `ref_image_9`). As imagens de referência são escalonadas para uma borda curta de 2048px se maior e nunca são escalonadas para cima. | IMAGE | Não | 0 a 9 |
| `vídeos_ref` | Espaço crescente: conecte até 3 vídeos de referência (`ref_video_1` ... `ref_video_3`). Quadros de vídeo de referência a 24 fps (2-15s). | IMAGE | Não | 0 a 3 |
| `áudios_vídeo_ref` | Espaço crescente: conecte até 3 trilhas de som (`ref_video_audio_1` ... `ref_video_audio_3`). Trilha de som do vídeo de referência com o mesmo número. | AUDIO | Não | 0 a 3 |
| `áudios_ref` | Espaço crescente: conecte até 3 cliques de áudio de referência independentes (`ref_audio_1` ... `ref_audio_3`). | AUDIO | Não | 0 a 3 |

Notas:

- O prompt menciona meios de referência com tags baseadas em 1 para cada tipo: `<Picture i>` para imagens, `<Video k>` para vídeos e `<Audio j>` para áudio. As referências são apresentadas ao modelo em uma ordem fixa: imagens, seguidas por vídeos (com a etiqueta `<Audio j>` do trilha de som logo antes do `<Video k>`), e, em seguida, áudio independente.
- Uma trilha de som conectada a `ref_video_audio_N` é usada com o vídeo de referência conectado a `ref_video_N`.
- Os vídeos de referência devem conter pelo menos 5 quadros (~0.2 segundos a 24 fps), caso contrário, o nó gera um erro. Quadros além do `length` solicitado são cortados, e o número restante de quadros é ajustado a um valor suportado pelo modelo.
- O `length` solicitado é alinhado a um número de quadros suportado antes da criação do latente.

## Outputs

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positivo` | Condição contendo o prompt codificado. Quando meios de referência e os relevantes VAEs são fornecidos, também contém o conteúdo de imagem, vídeo e áudio de referência codificado usado pelo modelo MiniMax H3. | CONDIÇÃO |
| `latent` | Latente de áudio-vídeo vazio com a largura, altura e comprimento solicitados (número de quadros). | LATENTE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `47df0d6d13cb02aa4f69b50a7f8d0f6c1639c1fb5e0f69bf8fc57dd4cb752db8`
