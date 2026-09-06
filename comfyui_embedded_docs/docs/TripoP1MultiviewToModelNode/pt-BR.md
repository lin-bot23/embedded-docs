# Tripo P1: Multivisual para Modelo

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | Visão frontal (0°). Obrigatório. | IMAGEM | Sim | - |
| `imagem_esquerda` | Visão esquerda (90°), ou seja, o lado esquerdo do sujeito. | IMAGEM | Não | - |
| `imagem_traseira` | Visão traseira (180°). | IMAGEM | Não | - |
| `imagem_direita` | Visão direita (270°), ou seja, o lado direito do sujeito. | IMAGEM | Não | - |
| `modo_de_saida` | Escolha o tipo de modelo a ser gerado. "Apenas geometria" retorna uma malha sem textura. "Texturizado" adiciona mapas de cor/PBR. | COMBO DINÂMICO | Sim | "Apenas geometria"<br>"Texturizado" |
| `limite_de_faces` | Número alvo de faces, 48-20000. -1 permite que o Tripo escolha adaptivamente. (padrão: -1) | INTEIRO | Não | -1 a 20000 |
| `semente_do_modelo` | Semente para geração de modelo repetível. (padrão: 42) | INTEIRO | Não | 0 a 2147483647 |
| `tamanho_automático` | Escalar a saída para aproximar metros do mundo real. (padrão: Falso) | BOOLEANO | Não | True<br>False |
| `exportar_uv` | Desempacotar UV durante a geração. Desative para execução mais rápida de geometria apenas. (padrão: True) | BOOLEANO | Não | True<br>False |
| `comprimir_geometria` | Aplicar compressão de geometria meshopt (EXT_meshopt_compression). Arquivos menores, mas o preview 3D do ComfyUI não pode exibi-los; descomprima antes de editar. (padrão: False) | BOOLEANO | Não | True<br>False |

### Entradas de geometria apenas

Não há entradas adicionais exibidas para este modo. O modelo gerado é retornado sem textura.

### Entradas texturizadas

Essas entradas aparecem quando `output_mode` é definido como `"Texturizado"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `pbr` | Incluir mapas PBR. Quando ativado, o mapa de base também é forçado. (padrão: True) | BOOLEANO | Sim | True<br>False |
| `texture_quality` | Nível de qualidade do mapa de textura. `detailed` = texturas HD, `extreme` = texturas Ultra 8K. (padrão: "standard") | COMBO | Sim | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Priorizar a fidelidade visual à imagem de origem ou alinhamento à geometria da malha. (padrão: "original_image") | COMBO | Sim | "original_image"<br>"geometry" |
| `orientation` | Rotacionar a saída para coincidir com a imagem de origem. Apenas se aplicável quando texturizado. (padrão: "default") | COMBO | Sim | "default"<br>"align_image" |
| `texture_seed` | Semente usada para geração de textura. (padrão: 42) | INTEIRO | Sim | 0 a 2147483647 |

**Nota:** Você deve fornecer pelo menos 2 imagens: a visão frontal (`image`) mais pelo menos uma das outras visões (`image_left`, `image_back` ou `image_right`). Se menos de 2 imagens forem fornecidas, o nó emitirá um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_modelo` | O nome do arquivo do modelo gerado GLB (apenas para compatibilidade reversa). | STRING |
| `id_tarefa_modelo` | O ID de tarefa único para este pedido de geração de modelo. | ID_DE_TAREFA_DE_MODELO |
| `GLB` | O modelo 3D gerado no formato GLB. | ARQUIVO3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c26bf9d46f6b95ec57e4eb663cb6c602035c3ad00682e7f9622ce575ff54d228`
