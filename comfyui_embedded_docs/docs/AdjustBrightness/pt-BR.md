# Ajustar Brilho

O nó Adjust Brightness modifica o quão brilhante uma imagem parece. Ele multiplica os valores de cor da imagem por um `factor` e mantém os resultados dentro do intervalo válido de 0.0 a 1.0. Um fator de 1.0 deixa a imagem inalterada, valores abaixo de 1.0 a deixam mais escura e valores acima de 1.0 a deixam mais clara.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada para ajustar. Aceita uma única imagem ou um lote de imagens. | IMAGE | Sim | - |
| `fator` | Fator de brilho. 1.0 = sem alteração, <1.0 = mais escura, >1.0 = mais clara. (padrão: 1.0) | FLOAT | Não | 0.0 - 2.0 |

Observação: Se a imagem de entrada tiver um canal alfa (RGBA), apenas os canais de cor serão ajustados. O canal alfa é copiado da entrada sem alterações, pois ele armazena transparência, não cor.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagens` | A imagem de saída com o brilho ajustado. Se a entrada tiver um canal alfa, os valores alfa permanecem inalterados. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/pt-BR.md)

---
**Source fingerprint (SHA-256):** `64c1499d16deb5922fa63538182cd227e8f2ba9ded5962064ce9f228a0f4a163`
