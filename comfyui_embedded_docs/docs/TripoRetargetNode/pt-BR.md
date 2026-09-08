# Tripo: Retarget para modelo com rig

### Visão Geral

O TripoRetargetNode aplica uma animação pré-definida em um modelo 3D existente e equipado. Ele recebe o ID da tarefa de um modelo que foi previamente equipado, envia uma solicitação de retargetamento para a API do Tripo e baixa o arquivo animado resultante. O modelo animado pode ser retornado no formato GLB ou FBX, com geometria de malha opcional e reprodução local opcional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `id_da_tarefa_do_modelo_original` | O ID da tarefa do modelo 3D previamente equipado para retargetamento. A tarefa referenciada deve ser uma tarefa de equipamento; um equipamento feito com a especificação do Mixamo na versão do modelo v1.0 não pode ser usado para retargetamento. | RIG_TASK_ID | Sim | - |
| `animação` | A animação pré-definida a ser aplicada ao modelo equipado. As animações `preset:*` funcionam com modelos de equipamento; as animações `preset:biped:*` requerem um equipamento feito com o modelo v1.0-20240301. | COMBO | Sim | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>plus additional `"preset:biped:*"` options shown in the UI |
| `out_format` | Formato do arquivo de saída; o resultado chega no matching output. (padrão: glb) | COMBO | Não | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | Incluir a malha na exportação; a opção off exporta apenas o esqueleto animado. (padrão: True) | BOOLEAN | Não | True<br>False |
| `animate_in_place` | Reproduzir a animação localmente, sem deslocamento de raiz. (padrão: False) | BOOLEAN | Não | True<br>False |
| `auth_token_comfy_org` | Token de autenticação para o acesso à API do Comfy.org (parâmetro oculto). | AUTH_TOKEN_COMFY_ORG | Não | - |
| `api_key_comfy_org` | Chave de API para o acesso ao serviço do Comfy.org (parâmetro oculto). | API_KEY_COMFY_ORG | Não | - |
| `unique_id` | Identificador único para rastreamento da operação (parâmetro oculto). | UNIQUE_ID | Não | - |

Nota: As animações no grupo `preset:*` funcionam com modelos de equipamento, enquanto as animações no grupo `preset:biped:*` requerem um equipamento feito com o modelo v1.0-20240301. Se o equipamento referenciado foi criado com a especificação do Mixamo e uma versão do modelo começando com `v1.0`, a chamada de retargetamento falha com um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | O arquivo do modelo 3D animado gerado (apenas para compatibilidade reversa). | STRING |
| `task_id_de_retarget` | O ID da tarefa para rastreamento da operação de retargetamento. | RETARGET_TASK_ID |
| `GLB` | O modelo 3D animado no formato GLB. Populado quando `out_format` é glb. | FILE3DGLB |
| `FBX` | O modelo 3D animado no formato FBX. Populado quando `out_format` é fbx. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e5417a8fa584285ba9e57526e65b091c2383374c70364df9053777a3ce09541a`
