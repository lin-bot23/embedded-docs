# Criar Imagem em Camadas

### Visão Geral

Este nó combina várias camadas de imagem em uma única imagem composta. Ele recebe uma pilha de camadas construída com o nó Adicionar Camada e, opcionalmente, aplica configurações de composição salvas do editor de compositor, mesclando as camadas conforme sua posição, tamanho, rotação, opacidade e modo de mesclagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `layers` | Pilha de camadas para composição; construa-a com Adicionar Camada. Os itens são empilhados pelo z_index, os quadros batch dentro de um item se expandem para camadas consecutivas, e a posição, opacidade e modo de mesclagem do item definem a composição inicial. Sem um canvas explícito do documento, o tamanho é o melhor esforço para a extensão máxima das camadas colocadas. Uma composição salva que coincide com os atuais entradas tem prioridade. | LAYERS | Sim | Máximo 50 camadas |
| `compositor` | Composição de camadas salva pelo editor de compositor. | COMPOSITOR | Não | Nenhum |

**Notas sobre restrições:**

- A pilha de camadas suporta um máximo de 50 camadas (quadros expandidos); fornecer mais gera um erro.
- Apenas camadas raster são suportadas atualmente; outros tipos de itens de camada geram um erro.
- A versão do documento `layers` deve ser 1; outras versões geram um erro.
- O estado salvo do `compositor` é reproduzido apenas quando seus impressões digitais de entrada coincidem com a pilha de camadas atual. Se não coincidirem, o nó recua para compor a partir das propriedades da camada e marca o estado salvo como desatualizado.
- A opacidade da camada é limitada ao intervalo 0.0 a 1.0.
- A posição horizontal/vertical da camada (`x`, `y`) é limitada ao limite máximo de resolução.
- A largura e altura da camada recuem para o tamanho natural da imagem quando definidas como zero ou menos, e são limitadas ao limite máximo de resolução.
- O tamanho do canvas composto não deve exceder o limite máximo de resolução.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | Imagem composta. Carrega um canal alfa quando a composição tem áreas transparentes (por exemplo, fundo oculto), caso contrário, RGB simples. | IMAGE |
| `MASK` | Transparência da composição (1 = completamente transparente). Todos os zeros quando a composição é opaca. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/pt-BR.md)

---
**Source fingerprint (SHA-256):** `76e5e57ade89f9ee172c5e1f0b82579d846d15bafb52b2052246f1f2ad7f0034`
