# Tripo: Modelo de Textura

### TripoTextureNode

O TripoTextureNode adiciona texturas a um modelo 3D existente do Tripo usando a API do Tripo. Ele recebe o ID da tarefa de um modelo criado por outro nó do Tripo e retorna um modelo GLB ou FBX texturizado após a conclusão da tarefa de textura. Você pode controlar mapas de materiais, qualidade de textura, alinhamento, semente e guiar as texturas com um prompt de texto, uma imagem de estilo ou imagens de referência.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | O ID da tarefa do Tripo do modelo a ser texturizado. Aceita IDs de tarefa de modelo e IDs de tarefa de segmentação. | MODEL_TASK_ID | Sim | - |
| `textura` | Ignorado: este nó sempre gera texturas. Mantido para fluxos de trabalho antigos. (padrão: True) | BOOLEAN | Não | true<br>false |
| `pbr` | Mapas de materiais PBR (cor base, metálico, rugosidade, normal); desligado oferece uma textura de cor plana. (padrão: True) | BOOLEAN | Não | true<br>false |
| `semente_textura` | Semente aleatória para a geração de texturas. Usar a mesma semente com os mesmos entradas produz o mesmo resultado. (padrão: 42) | INT | Não | 0 – 2147483647 |
| `qualidade_textura` | Qualidade de resolução da textura: detalhada = texturas HD, extrema = texturas Ultra 8K. (padrão: "standard"). Custo aproximado: standard $0.10, detalhada $0.20, extrema $0.30. | COMBO | Não | "standard"<br>"detailed"<br>"extreme" |
| `alinhamento_textura` | Método usado para alinhar as texturas geradas ao modelo. (padrão: "original_image") | COMBO | Não | "original_image"<br>"geometry" |
| `texture_prompt` | Guia opcional de textura em texto. Requerido na prática para modelos importados (Tripo: Importar Modelo), que não possuem imagem de origem para inferir cores. Não pode ser combinado com imagens de referência. (padrão: "") | STRING | Não | - |
| `model_version` | Versão do modelo de textura: v3.0 para malhas geradas com v3.x, v2.5 para malhas geradas com v2.5. (padrão: a última versão v3.0) | COMBO | Não | Múltiplas opções disponíveis |
| `style_image` | Imagem de referência para o estilo artístico das texturas. Usada apenas em conjunto com `texture_prompt`. | IMAGE | Não | - |
| `referência` | Imagens de referência que guiam as texturas. Não pode ser combinado com `texture_prompt` ou `style_image`. (padrão: "none") | DYNAMIC_COMBO | Não | "none"<br>"image"<br>"multiview" |
| `part_names` | Nomes de partes separados por vírgula do Tripo: Segmentar Modelo para textura. Texturas vazias para cada parte. (padrão: "") | STRING | Não | - |

### Entradas de referência "image"

Essas entradas estão disponíveis quando `reference` é definido como `"image"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | Imagem de referência única que as texturas devem seguir. | IMAGE | Não | - |

### Entradas de referência "multiview"

Essas entradas estão disponíveis quando `reference` é definido como `"multiview"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image_front` | Visão frontal (0°). | IMAGE | Não | - |
| `image_left` | Visão esquerda (90°). | IMAGE | Não | - |
| `image_back` | Visão traseira (180°). | IMAGE | Não | - |
| `image_right` | Visão direita (270°). | IMAGE | Não | - |

**Nota:** Os modos de referência `"image"` e `"multiview"` não podem ser combinados com um `texture_prompt` não vazio ou com `style_image`. O `style_image` requer um `texture_prompt` não vazio. Quando `texture_prompt` é deixado vazio, o modelo de origem deve já ter sua própria imagem de origem (por exemplo, modelos produzidos por text-to-model, image-to-model, multiview-to-model ou uma tarefa de textura anterior). Modelos que não possuem imagem de origem — como modelos importados, segmentados, completados ou retopologizados — devem ser texturizados com um `texture_prompt`; imagens de referência são aceitas apenas para modelos gerados pela própria API do Tripo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | O arquivo de modelo gerado (apenas para compatibilidade reversa). | STRING |
| `task_id_do_modelo` | O ID da tarefa de geração de textura concluída, usável como entrada para outros nós do Tripo. | MODEL_TASK_ID |
| `GLB` | O modelo texturizado gerado no formato GLB. Vazio quando a origem é uma malha quadrada ou uma importação FBX. | FILE3DGLB |
| `FBX` | O modelo texturizado gerado no formato FBX. O Tripo retorna FBX para malhas quadradas e importações FBX; vazio em outros casos. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `815c22a9d8f4785ef5219789e0f2eee804776ec7e4752099ec0db0a2b5ad4bb2`
