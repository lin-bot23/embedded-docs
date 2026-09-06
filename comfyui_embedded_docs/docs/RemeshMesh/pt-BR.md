# Remesh Mesh (Narrow-Band DC)

## Reestruturação de Malha

A reestruturação de malha (Remesh Mesh) recria uma malha com uma tesselação limpa e uniforme, através da amostragem de um campo de distância estreito ao redor da superfície original e da extração com Contorno Duplo (Dual Contouring). Isso normaliza topologias bagunçadas, não-manifold ou auto-intersecantes e deve ser executada antes de Decimar Malha (Decimate Mesh) para alcançar um número exato de faces. O processamento é executado no dispositivo de computação ativo e a malha de saída permanece soldada.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `malha` | A malha de entrada a ser reestruturada. | MESH | Sim | — |
| `resolução` | Resolução da grade de voxel (densidade de saída). 256 ~ 100k faces, 512 ~ 1M. Para um número exato de faces, siga com Decimar Malha. (padrão: 512) | INT | Sim | 32 - 2048 |
| `sign_mode` | Modo de extração de superfície. "udf" é robusto a entradas bagunçadas/não-manifold; "sdf" gera uma superfície limpa e única com recuperação de características afiadas usando QEF (Função de Erro Quadrática), mas requer reviravolta consistente. A seleção de um modo revela suas opções específicas. (padrão: "udf") | COMBO DINÂMICO | Sim | "udf"<br>"sdf" |
| `banda` | Largura da banda estreita em unidades de voxel. No modo UDF também desloca a superfície. (avançado, padrão: 1.0) | FLOAT | Sim | 0.5 - 4.0 |
| `project_back` | Interpola linearmente os vértices em direção à superfície original (0 = pura DC, 1 = ajustada). (avançado, padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |
| `fix_poles` | Colapsa pares de vértices de valência 3 (artefato de entroncamento DC). (avançado, padrão: falso) | BOOLEAN | Sim | verdadeiro / falso |
| `smooth_iters` | Iterações de suavização de Taubin (0 = desligado). 2-3 limpa artefatos de escada DC; valores mais altos podem suavizar excessivamente os bordas QEF. (padrão: 0) | INT | Sim | 0 - 20 |
| `drop_small_components` | Descarta componentes abaixo dessa fração do número de faces da maior. 0 desativa. (avançado, padrão: 0.01) | FLOAT | Sim | 0.0 - 0.5 |
| `precluster_max_verts` | Limita o número de vértices de entrada antes das consultas de campo; entradas acima desse valor são decimadas para ele primeiro. Previne OOM em malhas enormes. (avançado, padrão: 20,000,000) | INT | Sim | 0 - 100,000,000 |

### Entradas do Modo "udf"

Esses parâmetros aparecem quando `sign_mode` é definido como `"udf"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `qef` | Posicionamento de vértice dual usando QEF (Função de Erro Quadrática) para bordas mais afiadas. (padrão: falso) | BOOLEAN | Não | verdadeiro / falso |
| `drop_inverted_components` | Descarta componentes com volume negativo (normal interna invertida) — a casca interna do UDF. (padrão: falso) | BOOLEAN | Não | verdadeiro / falso |
| `drop_enclosed_components` | Descarta componentes dentro do bbox da maior que falham no raio de ponto na malha. Desative para partes legítimas aninhadas. (padrão: falso) | BOOLEAN | Não | verdadeiro / falso |

### Entradas do Modo "sdf"

Esses parâmetros aparecem quando `sign_mode` é definido como `"sdf"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `qef` | Posicionamento de vértice dual usando QEF (Função de Erro Quadrática) para recuperação de características afiadas em vez do centroide de cruzamento de borda. (padrão: verdadeiro) | BOOLEAN | Não | verdadeiro / falso |
| `manifold` | Contorno Duplo Manifold: 1-4 vértices duplos/voxel para casos de múltiplas folhas. Mais lento. (padrão: falso) | BOOLEAN | Não | verdadeiro / falso |

Nota: A opção `qef` tem um padrão diferente dependendo do modo selecionado — falso no modo "udf", verdadeiro no modo "sdf". Quando `precluster_max_verts` é maior que 0 e a malha de entrada tem mais vértices do que esse valor, a malha é decimada para esse valor-alvo antes das consultas de campo. Após o processamento, o nó exibe a mudança no número de faces de entrada para saída no nó (por exemplo, "faces: 1.23M → 200K (-84%)").

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `malha` | A malha reestruturada com tesselação uniforme e topologia soldada. As cores dos vértices são preservadas quando presentes na entrada; qualquer UV, normais e tangentes não são transferidos. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`
