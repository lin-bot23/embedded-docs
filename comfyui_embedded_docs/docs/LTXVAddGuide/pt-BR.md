# LTXVAddGuide

O nó LTXVAddGuide adiciona orientação de condicionamento de vídeo às sequências latentes codificando imagens ou vídeos de entrada e incorporando-os como quadros-chave nos dados de condicionamento. Ele processa a entrada por meio de um codificador VAE e posiciona estrategicamente os latentes resultantes em posições de quadro especificadas, atualizando o condicionamento positivo e o negativo com as informações dos quadros-chave. O nó lida com restrições de alinhamento de quadros e permite controlar a força da influência do condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamento positivo a ser modificada com orientação por quadros-chave | CONDITIONING | Sim | - |
| `negative` | Entrada de condicionamento negativo a ser modificada com orientação por quadros-chave | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar os quadros de imagem/vídeo de entrada | VAE | Sim | - |
| `latent` | Sequência latente de entrada que receberá os quadros de condicionamento | LATENT | Sim | - |
| `image` | Imagem ou vídeo para condicionar o vídeo latente. Deve ter 8*n + 1 quadros. Se o vídeo não tiver 8*n + 1 quadros, ele será cortado para a quantidade válida mais próxima de 8*n + 1 quadros. | IMAGE | Sim | - |
| `frame_idx` | Índice do quadro no qual o condicionamento começa. Para imagens de quadro único ou vídeos com 1 a 8 quadros, qualquer valor de `frame_idx` é aceitável. Para vídeos com 9 ou mais quadros, `frame_idx` deve ser divisível por 8; caso contrário, será arredondado para baixo até o múltiplo de 8 mais próximo. Valores negativos são contados a partir do final do vídeo. (padrão: 0) | INT | Sim | -9999 a 9999 |
| `strength` | Força da influência do condicionamento, em que 1.0 aplica condicionamento total e 0.0 não aplica condicionamento algum (padrão: 1.0) | FLOAT | Sim | 0.0 a 10.0 |
| `attention_mask` | Máscara espacial opcional no espaço de pixels. Controla a influência do condicionamento por região por meio da autoatenção, sendo multiplicada pela força. | MASK | Não | - |
| `iclora_parameters` | Parâmetros IC-LoRA opcionais provenientes de um nó Get IC-LoRA Parameters. Usados para ajustar o processamento da orientação conforme exigido por determinados IC-LoRAs (por exemplo, aqueles com `reference_downscale_factor` maior que 1). Quando encadeados, cada LTXVAddGuide usa somente os parâmetros conectados a ele. | IC_LORA_PARAMETERS | Não | - |

**Observação:** A imagem/vídeo de entrada deve ter uma contagem de quadros que siga o padrão 8*n + 1 (por exemplo, 1, 9, 17, 25 quadros). Se a entrada estiver fora desse padrão, ela será automaticamente cortada para a contagem de quadros válida mais próxima.

**Observação sobre `iclora_parameters`:** Ao usar parâmetros IC-LoRA com `reference_downscale_factor` maior que 1, as dimensões espaciais do latente (largura e altura) devem ser divisíveis por esse fator. O nó gerará um erro se essa condição não for atendida.

**Observação:** Os quadros de orientação codificados devem caber dentro da sequência latente na posição de quadro selecionada. Se esses quadros excederem o comprimento da sequência latente, o nó gerará um erro.

**Observação:** Não há suporte para adicionar uma orientação a um latente que combine canais de áudio e vídeo; isso gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo atualizado com informações de orientação por quadros-chave | CONDITIONING |
| `negative` | Condicionamento negativo atualizado com informações de orientação por quadros-chave | CONDITIONING |
| `latent` | Sequência latente com quadros de condicionamento incorporados e máscara de ruído atualizada | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/pt-BR.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
