# Seletor de Resolução

### Resolução do Seletor

O nó Resolução do Seletor calcula a largura e a altura em pixels com base em uma proporção de aspecto escolhida e uma resolução total em megapixels. É útil para gerar dimensões consistentes para outros nós, como o nó Imagem Latente Vazia.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `proporção_de_aspecto` | A proporção de aspecto para as dimensões de saída (padrão: `"1:1 (Quadrado)"`). | COMBO | Sim | `"1:1 (Quadrado)"`<br>`"2:3 (Retrato)"`<br>`"3:2 (Fotografia)"`<br>`"3:4 (Retrato Padrão)"`<br>`"4:3 (Padrão)"`<br>`"9:16 (Retrato de Cinema)"`<br>`"16:9 (Cinema)"`<br>`"21:9 (Ultrawide)"` |
| `megapixels` | Megapixels totais alvo. 1.0 MP ≈ 1024x1024 para quadrado (padrão: 1.0). | FLOAT | Sim | 0.1 - 16.0 (passo: 0.1) |
| `pré-visualização` | Visualização ao vivo da resolução calculada. Este widget de leitura-only atualiza automaticamente e não aceita entrada do usuário. | RESOLUÇÃO_VISUALIZAÇÃO | Não | N/A |
| `múltiplo` | Multiplo mais próximo do resultado para definir a resolução selecionada (padrão: 8). | INT | Não | 8 - 128 (passo: 4) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `largura` | Largura calculada em pixels multiplicada pelo múltiplo selecionado. | INT |
| `altura` | Altura calculada em pixels multiplicada pelo múltiplo selecionado. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dd4c7f977ed69a873a48da4b01c5c8f0b6563cfd743740235fc0ad5762579697`
