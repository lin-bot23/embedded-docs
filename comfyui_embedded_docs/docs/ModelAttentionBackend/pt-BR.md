# Backend de Atenção do Modelo

```markdown
# ModelAttentionBackend

## Visão Geral

O nó ModelAttentionBackend permite que você selecione uma implementação de atenção densa para um modelo. Ele patcha o modelo com o backend de atenção escolhido, que pode ser atenção PyTorch ou atenção Comfy Kitchen, quando disponível. Este nó é particularmente útil quando a atenção esparsa está inativa ou não suportada, garantindo que o modelo operate com o mecanismo de atenção densa especificado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo que será patchado com o backend de atenção escolhido. | MODEL | Sim |  |
| `attention` | O backend de atenção densa a ser aplicado ao modelo. As opções disponíveis são "atenção pytorch" e "atenção comfy kitchen" se a última estiver disponível no ambiente. | STRING | Sim | "atenção pytorch"<br> "atenção comfy kitchen" (quando disponível) |

- A opção "atenção comfy kitchen" utiliza atenção quantizada INT8 e é suportada apenas em GPUs Nvidia e AMD.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo de entrada com o backend de atenção escolhido aplicado. | MODEL |

## Nota

- Se o backend de atenção escolhido não estiver disponível, o nó recorrerá automaticamente ao uso da atenção PyTorch e logará um aviso.
- O nó ModelAttentionBackend é experimental e pode sofrer mudanças em futuras versões.
```

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
