# LTXVSeparateGeneratedKeyframes

```markdown
# LTXV Separar Geral de Chaves Geradas

## Visão Geral

O nó LTXV Separar Geral de Chaves Geradas remove chaves geradas de um latente amostrado e conditioning, permitindo que sejam tratadas separadamente antes de escalonar espacialmente o latente do vídeo. Ele é projetado para ser usado antes da escalonagem espacial e não deve ser executado após LTXV Recortar Guias, pois trata as chaves geradas como guias descartáveis e as descarta.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Conditioning positivo com metadados de chaves geradas removidos. | CONDITIONING | Sim | N/A |
| `negative` | Conditioning negativo com metadados de chaves geradas removidos. | CONDITIONING | Sim | N/A |
| `latent` | Latente do vídeo com as chaves geradas removidas. | LATENT | Sim | N/A |
| `keyframes_to_batch` | Retornar as chaves como um lote de latentes de único quadro. Deixe em branco para obter um único latente de múltiplos quadros, que é o que o escalonador de latente e o Add Geral de Chaves Geradas esperam. | BOOLEAN | Não | padrão: Falso |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Conditioning positivo com metadados de chaves geradas removidos. | CONDITIONING |
| `negative` | Conditioning negativo com metadados de chaves geradas removidos. | CONDITIONING |
| `latent` | Latente do vídeo com as chaves geradas removidas. | LATENT |
| `keyframes` | As chaves descobertas, rotuladas com generated_keyframe_indices e generated_keyframe_num_frames. Forneça essas chaves a um Add Geral de Chaves Geradas posterior para inicializar novos slots ou para Geral de Chaves Geradas para Guias para fixá-las como guias de imagem congelada (os índices são remapeados se o comprimento da tela mudar). | LATENT |

## Notas

- O parâmetro `keyframes_to_batch` determina se as chaves são retornadas como um lote de latentes de único quadro ou como um único latente de múltiplos quadros.
- O nó garante que as chaves geradas sejam removidas do conditioning e do latente antes de qualquer processamento adicional.
- A saída `keyframes` pode ser usada para inicializar novos slots para chaves geradas ou para fixá-las como guias de imagem congelada.
- O nó lança um `ValueError` se o latente não conter chaves geradas ou se as chaves não coincidirem com o formato esperado.
- O nó assume que as chaves geradas foram adicionadas usando o nó LTXV Adicionar Chaves Geradas e que são compatíveis com o latente atual.
```

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
