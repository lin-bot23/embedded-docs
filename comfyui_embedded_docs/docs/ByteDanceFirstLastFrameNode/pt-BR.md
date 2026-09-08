# ByteDance Primeiro-Último-Frame para Vídeo

Este nó gera um vídeo usando um prompt de texto juntamente com o primeiro e o último frames de uma imagem. Ele cria uma transição suave entre os dois frames, resultando em uma sequência de vídeo completa. O nó oferece uma variedade de opções para personalizar a resolução, proporção, duração e parâmetros adicionais de geração do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser usado para a geração de vídeo. Selecione entre as opções disponíveis (padrão: `"seedance-1-5-pro-251215"`). | COMBO | Sim | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"` |
| `prompt` | O prompt de texto usado para gerar o vídeo. Este prompt não deve conter parâmetros específicos como resolução, proporção, duração, seed, camerafixed ou watermark. | STRING | Sim | - |
| `first_frame` | O primeiro frame a ser usado para o vídeo. A imagem deve estar entre 300x300 e 6000x6000 pixels e ter uma proporção entre 0,4 e 2,5. | IMAGE | Sim | - |
| `last_frame` | O último frame a ser usado para o vídeo. A imagem deve estar entre 300x300 e 6000x6000 pixels e ter uma proporção entre 0,4 e 2,5. | IMAGE | Sim | - |
| `resolution` | A resolução do vídeo de saída. Escolha entre as opções disponíveis (padrão: `"480p"`). | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | A proporção do vídeo de saída. Selecione entre as opções disponíveis (padrão: `"adaptive"`). | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | A duração do vídeo de saída em segundos (padrão: 5). Para o modelo `seedance-1-5-pro-251215`, a duração mínima suportada é 4 segundos. | INT | Sim | 3 - 12 |
| `seed` | O seed a ser usado para a geração (padrão: 0). Este parâmetro é opcional. | INT | Não | 0 - 2147483647 |
| `camera_fixed` | Especifica se o câmera deve ser fixada no vídeo. A plataforma adiciona uma instrução para fixar a câmera ao seu prompt, mas o efeito real não é garantido (padrão: Falso). | BOOLEAN | Não | - |
| `watermark` | Determina se deve ser adicionado um selo "Gerado por IA" ao vídeo (padrão: Falso). | BOOLEAN | Não | - |
| `generate_audio` | Este parâmetro é ignorado para todos os modelos exceto `seedance-1-5-pro-251215` (padrão: Falso). | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

## Notas

- O parâmetro `model` determina as capacidades e limitações do processo de geração de vídeo.
- O `prompt` deve ser criativo e claro, pois ele guiará a geração do vídeo.
- As imagens `first_frame` e `last_frame` devem ser representativas do conteúdo desejado do vídeo.
- Os parâmetros `resolution` e `aspect_ratio` afetarão a qualidade e as dimensões finais do vídeo de saída.
- O parâmetro `duration` define a duração do vídeo, com um mínimo de 3 segundos e um máximo de 12 segundos.
- O parâmetro `seed` é opcional e pode ser usado para a reprodutibilidade do processo de geração de vídeo.
- O parâmetro `camera_fixed` é uma opção avançada que pode não sempre resultar no efeito esperado.
- O parâmetro `watermark` pode ser usado para adicionar um selo ao vídeo, indicando que ele foi gerado por uma IA.
- O parâmetro `generate_audio` é atualmente ignorado para todos os modelos exceto `seedance-1-5-pro-251215`.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae0f3a34a21baad7f04f6917e98d16dc64496479a050896869ec6693a9a9ebaf`
