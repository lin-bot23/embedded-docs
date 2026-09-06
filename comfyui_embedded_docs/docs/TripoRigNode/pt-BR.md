# Tripo: Rig no modelo

### Visão Geral

Este nó recebe um modelo 3D existente do Tripo e cria uma versão equipada dele, o que significa que o modelo ganha um esqueleto para poder ser animado. Você fornece o ID da tarefa do modelo a ser equipado, escolhe a versão do equipamento, o tipo de esqueleto, o estilo de nomeação dos ossos e o formato do arquivo de saída, e o nó envia o trabalho para o Tripo, aguarda até que ele termine e, em seguida, retorna o resultado baixado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | O ID da tarefa do modelo 3D original a ser equipado. Este é geralmente o ID gerado por um nó de geração de modelo do Tripo anterior. | MODEL_TASK_ID | Sim | - |
| `model_version` | Versão do modelo de equipamento a ser usada. v1.0: personagens humanoides (bipedes) apenas, 90+ presets de animação. v2.5: criaturas não humanoides (quadrúpedes, hexápodes, octópodes, aves, serpentes, aquáticos). Padrão: `v1.0-20240301`. | COMBO | Não | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | Tipo de esqueleto. "auto" executa primeiro a verificação de equipamento livre do Tripo e usa o tipo recomendado. Outros valores forçam um tipo de esqueleto específico, como bipede para personagens humanoides. Padrão: "auto". | COMBO | Não | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | Esquema de nomeação dos ossos: nativo do Tripo ou compatível com Mixamo. O Tripo não pode retarget seus presets de animação em um esqueleto v1.0 feito com o spec do Mixamo; use tripo para Tripo: Retarget rigged model. Padrão: "tripo". | COMBO | Não | "tripo"<br>"mixamo" |
| `out_format` | Formato do arquivo de saída; o resultado chega no matching de saída. Padrão: "glb". | COMBO | Não | "glb"<br>"fbx" |

**Nota:** A versão do modelo v1.0 (`v1.0-20240301`) suporta apenas esqueletos bipedes. Se um `rig_type` não bipede for usado com esta versão, o nó gera um erro e instrui você a usar `v2.5-20260210` em vez disso.

**Nota:** Quando `rig_type` é "auto", o Tripo verifica primeiro se o modelo pode ser equipado e escolhe o tipo de esqueleto recomendado. Se o Tripo informar que o modelo não pode ser equipado, o nó falha com um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | O arquivo de modelo 3D gerado. Mantido apenas por compatibilidade com versões anteriores. | STRING |
| `rig task_id` | O ID da tarefa para rastrear o processo de geração de equipamento. | RIG_TASK_ID |
| `GLB` | O modelo equipado como um arquivo 3D GLB. Populado quando `out_format` é "glb". | FILE3DGLB |
| `FBX` | O modelo equipado como um arquivo 3D FBX. Populado quando `out_format` é "fbx". | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `54c3b0984835160b74884d2c30191ad6dac6ea447862e9276253ace7367bc419`
