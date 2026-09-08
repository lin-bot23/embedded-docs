# Block Sparse Attention

## Visão Geral

O nó de Atenção Esparsa por Bloco aplica um mecanismo de atenção esparsa por bloco a um modelo do ComfyUI, reduzindo a computação de atenção permitindo que cada bloco de consulta atenda apenas a um subconjunto selecionado de blocos de chave exatamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo do ComfyUI ao qual aplicar a atenção esparsa por bloco. | MODEL | Sim | N/A |
| `selection` | O método de seleção para escolher quais blocos de chave atender. | DYNAMIC_COMBO | Sim | Opções: Sol-Attn (tau adaptativo), top-k (SLA), VSA (FastVideo) |
| `tau` | O limiar na distribuição de scores sigmas para a seleção Sol-Attn (tau adaptativo). | FLOAT | Não | padrão: 1.3, min: 0.0, max: 4.0, passo: 0.05 |
| `keep_percent` | A porcentagem de blocos de chave que cada bloco de consulta mantém exatamente para a seleção top-k (SLA). | FLOAT | Não | padrão: 10.0, min: 0.5, max: 95.0, passo: 0.5 |
| `start_percent` | A porcentagem do cronograma antes da qual o modelo usa atenção densa. | FLOAT | Não | padrão: 0.2, min: 0.0, max: 1.0, passo: 0.01 |
| `end_percent` | A porcentagem do cronograma após a qual o modelo usa atenção densa. | FLOAT | Não | padrão: 1.0, min: 0.0, max: 1.0, passo: 0.01 |
| `dense_blocks` | Uma string que representa os blocos do transformador que sempre executam atenção densa. | STRING | Não | padrão: "" |
| `min_tokens` | O número mínimo de tokens em uma sequência para o qual o modelo usa atenção densa. | INT | Não | padrão: 12288, min: 0, max: 1 << 20, passo: 512 |
| `extra_tokens` | O número de tokens extra de alto score que cada bloco de consulta atende além dos seus blocos selecionados. | INT | Não | padrão: 256, min: 0, max: 256, passo: 64 |
| `sink_conditioning` | As linhas de condição MiniMax-H3 a serem usadas para condição de escoamento. | COMBO | Não | Opções: exact_kv, exact_kv_and_rows, off |
| `verbose` | Se habilitar o log detalhado. | BOOLEAN | Não | padrão: Falso |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo do ComfyUI com atenção esparsa por bloco aplicada. | MODEL |

### Notas

- O parâmetro `selection` determina como os blocos de chave são escolhidos. As opções são:
  - Sol-Attn (tau adaptativo): Cada bloco de consulta atende a um subconjunto selecionado de blocos de chave com base em um limiar adaptativo.
  - top-k (SLA): Cada bloco de consulta mantém uma porcentagem fixa de blocos de chave exatamente.
  - VSA (FastVideo): Cada bloco de consulta mantém uma porcentagem fixa de cubos de vídeo exatamente, usando o mosaico de cubos e rama grossa do FastH3-VSA.
- O parâmetro `dense_blocks` permite que você especifique os blocos do transformador que sempre executam atenção densa.
- O parâmetro `min_tokens` define o número mínimo de tokens em uma sequência para o qual o modelo usa atenção densa.
- O parâmetro `extra_tokens` permite que você especifique o número de tokens extra de alto score que cada bloco de consulta atende além dos seus blocos selecionados.
- O parâmetro `sink_conditioning` determina as linhas de condição MiniMax-H3 a serem usadas para condição de escoamento.
- O parâmetro `verbose` habilita o log detalhado.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6a27aee45593883f5958ae1aac74a2077362742a0fdf74fc9dbfd68eddc6d259`
