# LTXVAddGuide

O nó LTXVAddGuide foi projetado para adicionar guia de condição de vídeo a sequências latentes, codificando imagens ou vídeos de entrada e incorporando-as como quadros-chave na dados de condição. Ele processa a entrada por meio de um encoder VAE e coloca estratégicamente os latentes resultantes em posições de quadros específicas, atualizando tanto a condição positiva quanto negativa com informações de quadro-chave. O nó lida com restrições de alinhamento de quadros e permite controle sobre a força da influência da condição.

## Visão Geral

O nó LTXVAddGuide codifica imagens ou vídeos de entrada, os processa por meio de um encoder VAE e usa os latentes codificados para condicionar uma sequência de vídeo latente. Ele permite especificar um índice de quadro para começar a condição e ajusta a força da influência da condição. O nó também suporta máscaras espaciais optativas para influência de condição por região e pode lidar com parâmetros IC-LoRA para ajustes de processamento de guia específicos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Entrada de condição positiva a ser modificada com guia de quadro-chave | CONDIÇÃO | Sim | - |
| `negative` | Entrada de condição negativa a ser modificada com guia de quadro-chave | CONDIÇÃO | Sim | - |
| `vae` | Modelo VAE usado para codificar os quadros de entrada de imagem/vídeo | VAE | Sim | - |
| `latent` | Sequência latente de entrada que receberá os quadros de condição | LATENTE | Sim | - |
| `image` | Imagem ou vídeo para condicionar a sequência de vídeo latente. Deve ter 8*n + 1 quadros. Se o vídeo não tiver 8*n + 1 quadros, ele será cortado para o número mais próximo de 8*n + 1 quadros. | IMAGEM | Sim | - |
| `frame_idx` | Índice de quadro para começar a condição. Para imagens ou vídeos com 1-8 quadros, qualquer valor de frame_idx é aceitável. Para vídeos com 9+ quadros, frame_idx deve ser divisível por 8, caso contrário, ele será arredondado para o múltiplo mais próximo de 8. Valores negativos são contados a partir do final do vídeo. (padrão: 0) | INTEIRO | Sim | -9999 a 9999 |
| `strength` | Força da influência da condição, onde 1.0 aplica condição completa e 0.0 aplica nenhuma condição (padrão: 1.0) | FLUTUANTE | Sim | 0.0 a 10.0 |
| `attention_mask` | Máscara espacial optativa. Controla a influência de condição por região via auto-atenção, multiplicada por força. | MASK | Não | - |
| `iclora_parameters` | Parâmetros IC-LoRA optativos de um nó Get IC-LoRA Parameters. Usados para ajustar o processamento de guia conforme necessário por certos IC-LoRAs (por exemplo, aqueles com um reference_downscale_factor > 1). Quando encadeados, cada LTXVAddGuide usa apenas os parâmetros conectados a ele. | PARÂMETROS_IC_LORA | Não | - |

**Nota:** A imagem/vídeo de entrada deve ter um número de quadros seguindo o padrão 8*n + 1 (por exemplo, 1, 9, 17, 25 quadros). Se a entrada exceder esse padrão, ela será automaticamente cortada para o número mais próximo de validade.

**Nota sobre `iclora_parameters`:** Quando usar parâmetros IC-LoRA com um `reference_downscale_factor` maior que 1, as dimensões espaciais latentes (largura e altura) devem ser divisíveis por esse fator. O nó levantará um erro se essa condição não for atendida.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condição positiva atualizada com informações de guia de quadro-chave | CONDIÇÃO |
| `negative` | Condição negativa atualizada com informações de guia de quadro-chave | CONDIÇÃO |
| `latent` | Sequência latente com quadros de condição incorporados e máscara de ruído atualizada | LATENTE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/pt-BR.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
