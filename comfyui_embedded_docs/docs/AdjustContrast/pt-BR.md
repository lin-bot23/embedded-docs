# Ajustar Contraste

O nó Adjust Contrast modifica o nível de contraste de uma imagem de entrada. Ele funciona ajustando a diferença entre as áreas claras e escuras da imagem. Um fator de 1.0 mantém a imagem inalterada, valores abaixo de 1.0 reduzem o contraste e valores acima de 1.0 aumentam. Se a imagem de entrada tiver um canal alfa, ele será mantido inalterado para preservar a transparência.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada que terá o contraste ajustado. | IMAGE | Sim | - |
| `fator` | Fator de contraste. 1.0 = sem alteração, <1.0 = menos contraste, >1.0 = mais contraste. (padrão: 1.0) | FLOAT | Não | 0.0 - 2.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagens` | A imagem resultante com contraste ajustado. Os valores de pixel são limitados ao intervalo de 0.0–1.0. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/pt-BR.md)

---
**Source fingerprint (SHA-256):** `489f840cc3d98339a5cf7b55e9179c60878c58b2f992740796c7d49642e05932`
