# Backend de Atenção do Modelo

Este nó seleciona o backend de atenção densa que um modelo usa para seus cálculos de atenção. Ele clona o modelo fornecido, aplica o backend escolhido e retorna o clone modificado. Quando usado com Block Sparse Attention, esse backend é utilizado sempre que a atenção esparsa estiver inativa ou não for suportada. Se o backend selecionado não estiver disponível, o nó recorre automaticamente à atenção PyTorch.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser modificado. | MODEL | Sim |  |
| `attention` | O backend de atenção densa a ser aplicado (padrão: "pytorch attention"). A atenção do Comfy Kitchen usa atenção INT8 quantizada e está disponível apenas em GPUs Nvidia e AMD. Se o backend selecionado não estiver disponível, a atenção PyTorch é usada como alternativa. | COMBO | Sim | "pytorch attention"<br>"comfy kitchen attention" |

Nota: A opção "comfy kitchen attention" só é listada quando o módulo de atenção INT8 do Comfy Kitchen está disponível no ambiente atual.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | Um clone do modelo de entrada com o backend de atenção selecionado aplicado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
