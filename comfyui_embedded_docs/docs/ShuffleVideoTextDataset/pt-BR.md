# Embaralhar Pares de Vídeo-Texto

### Visão Geral

Este nó embaralha aleatoriamente a ordem de pares de vídeo-texto em uma lista, mantendo cada vídeo associado ao seu texto correspondente. Ele recebe duas listas de comprimento igual e aplica a mesma permutação aleatória a ambas, garantindo que as combinações originais sejam preservadas após o embaralhamento. Um valor de semente controla a ordem do embaralhamento, permitindo que os resultados sejam reproduzidos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `videos` | Lista de vídeos a serem embaralhados. | VIDEO | Sim | Lista de itens de vídeo |
| `texts` | Lista de textos a serem embaralhados (os legendas associadas aos vídeos). | STRING | Sim | Lista de strings de texto |
| `seed` | Semente aleatória que determina a ordem do embaralhamento (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |

Nota: `videos` e `texts` devem ter o mesmo comprimento, pois o nó combina cada vídeo com o texto na mesma posição e preserva essas combinações quando embaralha. Internamente, o valor da semente é reduzido usando modulo 4294967295 (2^32 - 1) antes de gerar a ordem aleatória, então valores de semente muito grandes podem produzir o mesmo embaralhamento que valores menores.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `videos` | Vídeos embaralhados na nova ordem aleatória. | VIDEO |
| `texts` | Textos embaralhados na mesma nova ordem que os vídeos. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `834305718cd53a86211363750e887ffccdb54bc3b628dc17f049e546c234f9cb`
