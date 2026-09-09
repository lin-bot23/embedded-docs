# LTXVAddLatentGuide

```markdown
# Guia de Adição de Latente LTXV

## Visão Geral

O nó Guia de Adição de Latente LTXV fixa um latente já codificado como um guia, permitindo o uso de um guia que sai de uma etapa anterior em vez de uma imagem. Este nó evita a viagem de decodificação/encodificação do VAE e pode dilatar um guia espacialmente menor em uma grade rala para cobrir o canvas alvo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Entrada de condicionamento positivo. | CONDICIONAMENTO | Sim | N/A |
| `negative` | Entrada de condicionamento negativo. | CONDICIONAMENTO | Sim | N/A |
| `vae` | O modelo VAE a ser usado. | MODELO | Sim | N/A |
| `latent` | Latente de vídeo alvo em que o guia é fixado. | LATENTE | Sim | N/A |
| `guiding_latent` | Latente de guia. Seu tamanho espacial deve dividir o tamanho do alvo pelo mesmo número inteiro em ambos os eixos; tamanho igual fixa-o como está, metade do tamanho é tratado como uma referência IC-LoRA x2. | LATENTE | Sim | N/A |
| `latent_idx` | Índice do quadro latente para começar o guia, contado em quadros latentes em vez de quadros de pixel. Valores negativos colocam o guia em quadros antes do início do latente, não contados a partir do final. | INTEIRO | Sim | -9999 a 9999 |
| `strength` | Limitado a 1.0. Um guia dilatado marca suas posições de preenchimento com uma máscara de denoising negativa para que o modelo os descarte; valores acima de 1.0 farão com que as posições mantidas se tornem negativas e todo o guia será descartado. Amplifique além de 1.0 usando attention_mask em vez disso. | FLUTUANTE | Sim | 0.0 a 1.0, passo 0.01 |
| `attention_mask` | Máscara espacial opcional no espaço de pixels. Controla a influência de condicionamento por região via auto-atenção, multiplicada por força. | MÁSCARA | Não | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Saída de condicionamento positivo. | CONDICIONAMENTO |
| `negative` | Saída de condicionamento negativo. | CONDICIONAMENTO |
| `latent` | Saída latente com o guia aplicado. | LATENTE |

## Notas

- O tamanho espacial do `guiding_latent` deve dividir o tamanho do `latent` pelo mesmo número inteiro em ambos os eixos.
- O parâmetro `latent_idx` permite a colocação precisa do guia dentro dos quadros latentes.
- O parâmetro `strength` controla a intensidade do guia, com valores acima de 1.0 exigindo o uso de `attention_mask` para evitar posições negativas.
- O parâmetro `attention_mask` é opcional mas pode ser usado para ajustar a influência do guia em regiões específicas da imagem.
```

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
