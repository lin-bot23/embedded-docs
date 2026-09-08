# Tripo: Converter modelo

Este nó converte um modelo 3D existente do Tripo para outro formato de arquivo 3D. Ele recebe o ID da tarefa de um modelo previamente criado ou processado por uma operação do Tripo (tais como geração de modelo, rigging, retargeting ou segmentação), envia uma tarefa de conversão para a API do Tripo, aguarda que a tarefa seja concluída e, em seguida, retorna o arquivo do modelo convertido.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | ID da tarefa do modelo Tripo a ser convertido. Deve vir de uma geração de modelo, rigging, retargeting ou segmentação do Tripo anterior. Se o ID estiver ausente ou vazio, o nó lança um erro. | STRING (ID da tarefa do Tripo) | Sim | ID_DA_TAREFA_DO_MODELO<br>ID_DA_TAREFA_DE_RIG<br>ID_DA_TAREFA_DE_RETARGET<br>ID_DA_TAREFA_DE_SEGMENTAÇÃO |
| `formato` | Formato de arquivo-alvo para o modelo 3D convertido. | COMBO | Sim | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `quad` | Converte triângulos em quádricos quando ativado (padrão: Falso). | BOOLEAN | Não | True or False |
| `limite_de_faces` | Número máximo de faces no modelo convertido. Defina como -1 para sem limite (padrão: -1). | INT | Não | -1 a 2000000 |
| `tamanho_da_textura` | Resolução das texturas de saída em pixels (padrão: 4096). | INT | Não | 128 a 8192 |
| `formato_da_textura` | Formato de arquivo usado para texturas exportadas (padrão: JPEG). | COMBO | Não | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `forçar_simetria` | Força o modelo a ser simétrico quando ativado (padrão: Falso). | BOOLEAN | Não | True or False |
| `achatar_base` | Aplanar a parte inferior do modelo quando ativado (padrão: Falso). | BOOLEAN | Não | True or False |
| `limite_achatamento_base` | Profundidade de aplanamento usada com `flatten_bottom` (padrão: 0.01). Este valor é aplicado apenas quando `flatten_bottom` está ativado. | FLOAT | Não | 0.01 a 1.0 |
| `pivô_para_centro_base` | Move o ponto de pivô para o centro inferior do modelo quando ativado (padrão: Falso). | BOOLEAN | Não | True or False |
| `fator_de_escala` | Fator de escala aplicado ao modelo convertido (padrão: 1.0). | FLOAT | Não | 0.01 e acima |
| `com_animação` | Manter o esqueleto e a animação de modelos rigados ou retargeted (padrão: True). | BOOLEAN | Não | True or False |
| `empacotar_uv` | Rearranjar as coordenadas UV quando ativado (padrão: Falso). | BOOLEAN | Não | True or False |
| `bake` | Assar materiais avançados nas texturas básicas para maior compatibilidade (padrão: True). | BOOLEAN | Não | True or False |
| `nomes_das_partes` | Lista separada por vírgula de nomes de partes do modelo a serem enviados para a conversão. Entradas vazias são ignoradas e nomes duplicados são removidos. Deixe vazio para omitir esta opção (padrão: vazio). | STRING | Não | Lista separada por vírgula de nomes de partes |
| `preset_fbx` | Preset de compatibilidade FBX. `bake_scale` assa a transformação de escala na geometria (padrão: blender). | COMBO | Não | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `exportar_cores_dos_vértices` | Exportar cores de vértice quando ativado (padrão: Falso). | BOOLEAN | Não | True or False |
| `exportar_orientação` | Eixo direcional do modelo exportado. `default` mantém o +x do Tripo (padrão: default). | COMBO | Não | default<br>+x<br>-x<br>+y<br>-y |
| `animar_no_local` | Animar o modelo no local quando ativado (padrão: Falso). | BOOLEAN | Não | True or False |

**Nota:** Exceto por `original_model_task_id` e `format`, todas as entradas são configurações avançadas opcionais. Configurações deixadas nos valores padrão são omitidas da solicitação de conversão para que a API do Tripo use seu comportamento padrão. A entrada `flatten_bottom_threshold` só é significativa quando `flatten_bottom` está ativado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_3d` | Modelo convertido no formato solicitado. O OBJ é entregue pelo Tripo como um arquivo ZIP (malha, material e texturas). | ARQUIVO_3D |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5fd181d15025576083769e1ce31fb20cabb33096a01c67be50c3d9bb332739bf`
