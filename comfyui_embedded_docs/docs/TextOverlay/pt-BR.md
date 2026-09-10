# Desenhar Sobreposição de Texto

Este nó desenha texto sobre uma imagem ou um lote de imagens. Ele constrói uma sobreposição de texto com tamanho de fonte, cor, posição vertical, alinhamento horizontal e contorno preto opcional configuráveis, e então compõe a sobreposição sobre as imagens originais.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagens` | A imagem de entrada ou lote de imagens sobre o qual desenhar o texto | IMAGE | Sim | |
| `texto` | O texto a ser sobreposto na imagem (padrão: ""). Suporta múltiplas linhas: as sequências de escape `\n` e `\t` são convertidas em quebras de linha e tabulações, e linhas longas são quebradas automaticamente para caber dentro da largura da imagem. | STRING | Sim | |
| `tamanho_da_fonte` | Tamanho da fonte como porcentagem da altura da imagem (padrão: 5.0) | FLOAT | Sim | 0.5 a 50.0 (passo 0.5) |
| `cor` | Cor do texto (padrão: "#ffffff") | STRING | Sim | |
| `posição` | Posição vertical do texto na imagem (padrão: "top") | COMBO | Sim | "top"<br>"bottom" |
| `alinhamento` | Alinhamento horizontal do texto (padrão: "left") | COMBO | Sim | "left"<br>"center"<br>"right" |
| `contorno` | Desenha um contorno preto ao redor do texto (padrão: True) | BOOLEAN | Sim | |

Observação: Se `text` estiver vazio ou contiver apenas espaços em branco, o nó retorna as imagens de entrada inalteradas. A sobreposição de texto é renderizada uma vez e aplicada a cada imagem do lote.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `imagens` | As imagens de entrada com a sobreposição de texto composta por cima | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`
