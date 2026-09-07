# Ajustar Brilho

O nó Adjust Brightness modifica o brilho de uma imagem de entrada. Ele funciona multiplicando o valor de cada pixel por um fator especificado e, em seguida, limitando os valores resultantes para permanecerem dentro de um intervalo válido. Um fator de 1.0 mantém a imagem inalterada, valores abaixo de 1.0 a tornam mais escura e valores acima de 1.0 a tornam mais brilhante. Se a imagem de entrada tiver um canal alfa, ele será mantido inalterado para preservar a transparência.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada para ajustar. | IMAGE | Sim | - |
| `fator` | Fator de brilho. 1.0 = sem alteração, <1.0 = mais escura, >1.0 = mais brilhante. (padrão: 1.0) | FLOAT | Não | 0.0 - 2.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagens` | A imagem de saída com brilho ajustado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/pt-BR.md)

---
**Source fingerprint (SHA-256):** `64c1499d16deb5922fa63538182cd227e8f2ba9ded5962064ce9f228a0f4a163`
