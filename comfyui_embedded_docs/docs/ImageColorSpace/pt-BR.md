# Converter Espaço de Cor da Imagem

O nó ImageColorSpace converte imagens entre os espaços de cor sRGB (Rec.709), Rec.709 linear, HDR (Rec.2020 HLG) e HDR PQ (Rec.2020 PQ). Ao converter para saída SDR, ou de HDR PQ para HDR, ele aplica mapeamento de tons à luminância excedente em todo o lote e comprime cores fora da gama; conversões para linear e de linear para HDR preservam os valores estendidos sem mapeamento de tons. As conversões são calculadas em float32, e qualquer canal alfa é repassado sem alterações.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser convertida. | IMAGE | Sim | Qualquer imagem válida. |
| `source` | Espaço de cor dos pixels de entrada. Padrão: "sRGB". | COMBO | Sim | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |
| `destination` | Espaço de cor dos pixels de saída. Defina o nó de salvamento para este mesmo espaço de cor. Padrão: "sRGB". | COMBO | Sim | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem convertida no espaço de cor de destino especificado. | IMAGE |

## Observações

- Linear 1.0 usa o mesmo branco de referência de 203 nits que sRGB; HLG usa um display de referência de 1000 nits.
- Saídas lineares e conversões de linear para HDR preservam valores estendidos sem mapeamento de tons.
- Saída SDR e conversão de PQ para HLG aplicam mapeamento de tons à luminância excedente em todo o lote (compartilhando um único ponto de branco para que a exposição não mude quadro a quadro) e comprimem cores fora da gama.
- As conversões são calculadas em float32 e retornam o dispositivo e o dtype intermediários.
- O alfa straight não passa por transformação de cor; apenas os canais RGB são convertidos.
- Se `source` e `destination` forem iguais, nenhuma transformação de cor é aplicada — a imagem é apenas movida para o dispositivo e o dtype intermediários.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/pt-BR.md)

---
**Source fingerprint (SHA-256):** `04ae447a9f9805341e31755ad0fa56746ac0371fa2cb9bda95df3879c9dbead7`
