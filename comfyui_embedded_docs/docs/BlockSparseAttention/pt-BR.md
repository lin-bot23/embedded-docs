# Atenção Esparsa em Blocos do Modelo

## Visão Geral

O nó de Bloco de Atenção Esparsa modifica um modelo do ComfyUI para aplicar um mecanismo de atenção esparsa por bloco. Este mecanismo reduz a carga computacional permitindo que cada bloco de consulta se concentre em um subconjunto de blocos de chave, em vez de atender a todos os possíveis blocos, o que é particularmente benéfico para sequências longas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo do ComfyUI ao qual aplicar a atenção esparsa por bloco. | MODEL | Sim | N/A |
| `selection` | O método usado para determinar quais blocos de chave devem ser atendidos. | DYNAMIC_COMBO | Sim | Opções: sol-attn (tau adaptativo), sla (top-k), vsa (Video Sparse Attention) |
| `tau` | O limiar na distribuição de scores em sigmas para o método sol-attn. | FLOAT | Não | padrão: 1.3, min: 0.0, max: 4.0, passo: 0.05 |
| `keep_percent` | A porcentagem de blocos de chave que cada bloco de consulta mantém exatamente para o método sla. | FLOAT | Não | padrão: 10.0, min: 0.5, max: 95.0, passo: 0.5 |
| `start_percent` | O ponto percentual quando a atenção esparsa começa. | FLOAT | Não | padrão: 0.2, min: 0.0, max: 1.0, passo: 0.01 |
| `end_percent` | O ponto percentual quando a atenção esparsa termina. | FLOAT | Não | padrão: 1.0, min: 0.0, max: 1.0, passo: 0.01 |
| `dense_blocks` | Uma string que representa os blocos do transformador que sempre executam atenção densa. | STRING | Não | padrão: "" |
| `min_tokens` | O número mínimo de tokens em uma sequência para o qual o modelo usa atenção densa. | INT | Não | padrão: 12288, min: 0, max: 1 << 20, passo: 512 |
| `extra_tokens` | O número de tokens de alto score adicionais que cada bloco de consulta deve atender além dos seus blocos selecionados. | INT | Não | padrão: 256, min: 0, max: 256, passo: 64 |
| `sink_conditioning` | As linhas de condição MiniMax-H3 a serem usadas para condição de escoamento. | COMBO | Não | Opções: exact_kv, exact_kv_and_rows, off |
| `verbose` | Habilita log detalhado. | BOOLEAN | Não | padrão: Falso |

### Notas

- O parâmetro `selection` permite escolher entre diferentes métodos para selecionar blocos de chave:
  - `sol-attn`: Usa um limiar adaptativo para selecionar blocos de chave com base na distribuição de scores.
  - `sla`: Mantém uma porcentagem fixa dos blocos de chave de alto score.
  - `vsa`: Aplica Atenção Esparsa de Vídeo (Video Sparse Attention), que usa mosaico de cubo 3D de vídeo e uma ramificação de atenção grossa aprendida.
- O parâmetro `dense_blocks` pode ser usado para especificar blocos do transformador que devem sempre usar atenção densa.
- O parâmetro `min_tokens` define o número mínimo de tokens em uma sequência para o qual é usada atenção densa.
- O parâmetro `extra_tokens` permite especificar o número de tokens de alto score adicionais que cada bloco de consulta deve atender.
- O parâmetro `sink_conditioning` é relevante apenas para modelos MiniMax-H3 e determina como as linhas de condição são tratadas.
- O parâmetro `verbose` habilita log detalhado, o que pode ser útil para depuração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo do ComfyUI com a atenção esparsa por bloco aplicada. | MODEL |

### Restrições e Limitações

- O método `sol-attn` requer um valor de `tau` entre 0.0 e 4.0.
- O método `sla` requer um valor de `keep_percent` entre 0.5 e 95.0.
- O método `vsa` é compatível apenas com modelos MiniMax-H3 e requer que o modelo tenha uma camada `to_gate_compress`.
- O parâmetro `min_tokens` deve ser um inteiro não negativo (com 0, toda a atenção permanece densa).
- O parâmetro `extra_tokens` deve ser um inteiro não negativo.
- As opções de `sink_conditioning` são aplicáveis apenas a modelos MiniMax-H3.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
