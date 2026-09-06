# Desembrulhar UVs da malha

Gera um atlas UV para uma malha 3D. A superfície da malha é dividida em cartas, cada carta é achatada em duas dimensões e as cartas achatadas são empacotadas em um atlas UV de [0,1]. Os vértices nas junções das cartas são duplicados, então a malha de saída pode conter mais vértices do que a malha de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha de entrada a ser desdobrada. Aceita uma única malha ou um lote de malhas. | MESH | Sim | — |
| `segmenter` | Algoritmo de cartografia a ser usado. `pec`: cartografia paralela de collapse de borda rápida no GPU. `adaptive`: CPU, mais lento. (padrão: "pec") | COMBO | Sim | "pec"<br>"adaptive" |
| `resolution` | Resolução do atlas alvo para ajuste automático de densidade de texel (0 = ajuste ao conteúdo). (padrão: 1024) | INT | Sim | 0 a 8192 (passo 256) |
| `padding` | PADDING de texel entre cartas. (padrão: 1) | INT | Sim | 0 a 16 |
| `weld_distance` | Raio de junção de vértices coincidentes como fração da extensão da malha (0 = automático). Aumente para ~0.001 se você obter cartas por triângulo (entrada não soldada). (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.0001) |

Nota: se a malha de entrada contiver vértices não soldados, o nó pode avisar que a adjacência de faces é baixa e produzir cartas UV por face; aumentando `weld_distance` junta vértices coincidentes antes de desdobrar.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha de entrada com um atlas UV gerado na faixa [0,1]. Vértices de junção são duplicados, então o número de vértices da saída pode exceder o número de vértices da entrada. Cores e textura da malha de entrada são preservadas. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fcab6f0b621693d862ee74b5ec498498d2f1f247a66f478704377598a6b39388`
