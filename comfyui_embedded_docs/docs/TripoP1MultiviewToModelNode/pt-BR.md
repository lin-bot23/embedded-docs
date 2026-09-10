# Tripo P1: Multivisual para Modelo

Este nó gera um modelo 3D a partir de duas a quatro imagens de referência de um objeto ou personagem. Forneça a vista frontal mais qualquer combinação das vistas esquerda, traseira e direita, e o nó retorna o sujeito reconstruído como uma malha GLB.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | Vista frontal (0°). Obrigatória. | IMAGE | Sim | - |
| `imagem_esquerda` | Vista esquerda (90°), ou seja, o lado esquerdo do sujeito. | IMAGE | Não | - |
| `imagem_traseira` | Vista traseira (180°). | IMAGE | Não | - |
| `imagem_direita` | Vista direita (270°), ou seja, o lado direito do sujeito. | IMAGE | Não | - |
| `modo_de_saida` | Escolha o tipo de modelo a gerar. "Geometry only" retorna uma malha sem textura. "Textured" adiciona mapas de cor/PBR. | DYNAMIC_COMBO | Sim | "Geometry only"<br>"Textured" |
| `limite_de_faces` | Contagem alvo de faces, 48-20000. -1 permite que o Tripo escolha de forma adaptativa. (padrão: -1) | INT | Não | -1 a 20000 |
| `semente_do_modelo` | Semente para geração reproduzível do modelo. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `tamanho_automático` | Dimensiona a saída para aproximar metros do mundo real. (padrão: False) | BOOLEAN | Não | True<br>False |
| `exportar_uv` | Desdobramento UV durante a geração. Desative para execuções mais rápidas somente com geometria. (padrão: True) | BOOLEAN | Não | True<br>False |
| `comprimir_geometria` | Aplica compressão de geometria meshopt (EXT_meshopt_compression). Arquivos menores, mas a pré-visualização 3D do ComfyUI não consegue exibi-los; descomprima antes de editar. (padrão: False) | BOOLEAN | Não | True<br>False |

### Entradas do modo Geometry only

Nenhuma entrada adicional é exibida para este modo. O modelo gerado é retornado sem textura.

### Entradas do modo Textured

Estas entradas aparecem quando `output_mode` está definido como `"Textured"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `pbr` | Inclui mapas PBR. Quando ativado, a textura base também é forçada. (padrão: True) | BOOLEAN | Sim | True<br>False |
| `texture_quality` | Nível de qualidade da textura. `detailed` = texturas HD, `extreme` = texturas 8K Ultra. (padrão: "standard") | COMBO | Sim | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Prioriza a fidelidade visual à imagem de origem ou o alinhamento à geometria da malha. (padrão: "original_image") | COMBO | Sim | "original_image"<br>"geometry" |
| `orientation` | Rotaciona a saída para corresponder à imagem de origem. Aplica-se apenas quando texturizado. (padrão: "default") | COMBO | Sim | "default"<br>"align_image" |
| `texture_seed` | Semente usada para a geração da textura. (padrão: 42) | INT | Sim | 0 a 2147483647 |

**Nota:** Você deve fornecer pelo menos 2 imagens: a vista frontal (`image`) mais pelo menos uma das outras vistas (`image_left`, `image_back` ou `image_right`). Se menos de 2 imagens forem fornecidas, o nó gerará um erro.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `arquivo_modelo` | O nome do arquivo do modelo GLB gerado (apenas para compatibilidade retroativa). | STRING |
| `id_tarefa_modelo` | O ID de tarefa exclusivo para esta solicitação de geração de modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1153f74ac76603829142959844e701f3c8f16be080e3de849951cffdda322d12`
