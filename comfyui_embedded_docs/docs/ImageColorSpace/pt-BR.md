# Convert Image Color Space

## Visão Geral

O nó ImageColorSpace converte imagens entre diferentes espaços de cores, incluindo sRGB, HDR (Rec.2020 HLG) e HDR PQ (Rec.2020 PQ). Ele suporta a redução de excesso de luminância em mapas de tons ao longo do lote e a compressão de cores fora do gamut, operando apenas nos canais RGB, com os canais alpha passados inalterados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser convertida. | IMAGEM | Sim | Qualquer formato de imagem válido. |
| `source` | O espaço de cores dos pixels de entrada. | COMBO | Sim | <br> "sRGB" <br> "HDR" <br> "HDR PQ" |
| `destination` | O espaço de cores dos pixels de saída. | COMBO | Sim | <br> "sRGB" <br> "HDR" <br> "HDR PQ" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem convertida no espaço de cores de saída especificado. | IMAGEM |

## Notas

- O nó usa um branco SDR de 203 nit e uma referência de exibição HLG de 1000 nit para conversões.
- As conversões são calculadas em float32 e retornam o dispositivo e o dtype intermediário.
- O canal alpha é passado inalterado sem transformação de cor.
- O nó suporta conversões entre os espaços de cores sRGB, HDR (Rec.2020 HLG) e HDR PQ (Rec.2020 PQ).
- O nó realiza a redução de mapas de tons e comprime cores fora do gamut para garantir conversões precisas.
- Os canais RGB são usados para conversões, e o canal alpha (se presente) é passado inalterado.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f0d38c6f5b524752a99d51b1a87f0e65c07f3ba36ecb0066d8d10c5b5032d36f`
