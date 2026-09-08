# Tripo P1: Imagem para Modelo

Converta uma única imagem 2D em um modelo 3D usando a API do Tripo P1. É otimizado para gerar malhas de baixa poligonal, prontas para jogos, e permite escolher entre uma malha geométrica apenas ou um modelo texturizado com mapas PBR. O modelo final é retornado como um arquivo GLB.

## Entradas

### Entradas comuns

Esses parâmetros estão sempre disponíveis.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modo_de_saida` | Escolhe o tipo de resultado. "Geometry only" retorna uma malha não texturizada; "Textured" adiciona cores e mapas PBR e revela configurações extras de textura. | COMBO DINÂMICO | Sim | `"Geometry only"`<br>`"Textured"` |
| `imagem` | A imagem 2D de origem usada para gerar o modelo 3D. O nó requer uma única imagem e gera um erro se nenhuma for fornecida. | IMAGEM | Sim | - |
| `habilitar_autoajuste_imagem` | Pré-processa a imagem de entrada para melhorar a qualidade da geração. (padrão: Falso) | BOOLEAN | Não | True<br>False |
| `limite_de_faces` | Número alvo de faces, 48-20000. -1 permite que o Tripo escolha adaptivamente. (padrão: -1) | INT | Não | -1 a 20000 |
| `semente_do_modelo` | Semente usada para a geração geométrica para que os resultados possam ser reproduzidos. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `tamanho_automático` | Escala a saída para aproximar metros do mundo real. (padrão: Falso) | BOOLEAN | Não | True<br>False |
| `exportar_uv` | Desenvolve UV durante a geração. Desative para execução mais rápida de malhas geométricas apenas. (padrão: True) | BOOLEAN | Não | True<br>False |
| `comprimir_geometria` | Aplica compressão geométrica meshopt (EXT_meshopt_compression). Arquivos menores, mas o preview 3D do ComfyUI não pode exibi-los; descomprima antes de editar. (padrão: Falso) | BOOLEAN | Não | True<br>False |

### Entradas texturizadas

Esses parâmetros aparecem quando `output_mode` é definido como "Textured". O modo "Geometry only" não tem parâmetros extras.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `pbr` | Inclui mapas PBR. Quando ativado, o textura base também é forçada. (padrão: True) | BOOLEAN | Não | True<br>False |
| `texture_quality` | Nível de resolução da textura. "detailed" = texturas HD, "extreme" = texturas Ultra 8K. (padrão: "standard") | COMBO | Não | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Prioriza a fidelidade visual à imagem de origem ou alinhamento à geometria da malha. (padrão: "original_image") | COMBO | Não | `"original_image"`<br>`"geometry"` |
| `orientation` | Gira a saída para coincidir com a imagem de origem. Apenas se aplica quando texturizado. (padrão: "default") | COMBO | Não | `"default"`<br>`"align_image"` |
| `texture_seed` | Semente usada para a geração de textura para que os resultados texturizados possam ser reproduzidos. (padrão: 42) | INT | Não | 0 a 2147483647 |

Nota: Quando `output_mode` é "Geometry only", a textura é desativada para a solicitação. No modo "Textured", uma textura de cor sempre é solicitada; desativar `pbr` remove os mapas PBR, mas mantém a textura de cor base, enquanto ativar `pbr` força a textura base.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `arquivo_modelo` | O resultado do modelo 3D gerado. Mantido apenas por compatibilidade reversa. | STRING |
| `id_tarefa_modelo` | O ID de tarefa único retornado pela API do Tripo para o trabalho de geração completo. | ID_TAREFA_MODELO |
| `GLB` | O modelo 3D gerado no formato GLB. | ARQUIVO3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db5dc76518a4efcd28d388dc00ad0810f619481482f20fa456c4ff2478192aa3`
