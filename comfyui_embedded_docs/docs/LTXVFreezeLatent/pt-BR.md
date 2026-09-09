# LTXVFreezeLatent

```markdown
# LTXV Freeze Latent

## Visão Geral

O nó LTXV Freeze Latent foi projetado para definir o noise_mask como 0 para um latent específico, garantindo que o latent permaneça limpo durante a amostragem. É particularmente útil para congelar latentes de áudio ou vídeo para evitar a desnuvem, que pode ser aplicada antes de concatenar áudio e vídeo para cross-attention ou para qualquer latent que não deve ser desnuvem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `latent` | Latente de vídeo ou áudio a ser congelado. O áudio é 4D; o vídeo é 5D. | LATENT | Sim | N/A |
| `samples` | O tensor contendo as amostras do latent. | TENSOR | Sim | Áudio: 4D (lote, canais, quadros, amostras); Vídeo: 5D (lote, canais, altura, largura, quadros) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `latent` | O latent com o noise_mask definido como 0, garantindo que ele permaneça limpo durante a amostragem. | LATENT |

## Notas

- O tensor `samples` deve ser um tensor simples e não um latent concatenado áudio-vídeo. Se for um latent concatenado, ele deve ser dividido usando o nó Separate AV Latent primeiro.
- A saída `latent` terá um noise_mask de zeros, que impede a desnuvem para o latent especificado.
- O nó suporta tanto latentes de áudio quanto de vídeo, com diferentes formas de tensor para cada um.
- Se a forma do tensor `samples` não corresponder à forma esperada de áudio ou vídeo, um ValueError será levantado.
```

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
