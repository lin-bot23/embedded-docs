# Tripo: Imagem para Modelo

Gera modelos 3D de forma sincronizada com base em uma única imagem utilizando a API da Tripo. Forneça uma imagem de entrada e o nó cria um modelo 3D final a partir dela, com controles opcionais para versão do modelo, geração de textura, nível de detalhe e formato de saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada usada para gerar o modelo 3D. Uma imagem deve ser fornecida; caso contrário, o nó gera um erro. | IMAGEM | Sim | - |
| `versão_do_modelo` | A versão do modelo a ser usada para a geração. | COMBO | Não | `"v1.4"`<br>`"v3.0"`<br>`"v3.5"`<br>`"v3.6"` |
| `estilo` | Não é mais suportado pela Tripo e ignorado. Mantido para fluxos de trabalho antigos. (padrão: `"None"`) | COMBO | Não | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `textura` | Gera mapas de textura. Desligado retorna geometria nua e ignora `pbr`. (padrão: True) | BOOLEAN | Não | True<br>False |
| `pbr` | Mapas de material PBR (cor de base, metálico, rugosidade, normal). Requer `texture`. (padrão: True) | BOOLEAN | Não | True<br>False |
| `semente_do_modelo` | Semente aleatória para a geração do modelo. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `orientação` | Configuração de orientação para o modelo gerado. (padrão: `"default"`) | COMBO | Não | `"default"`<br>`"front"`<br>`"back"`<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `semente_da_textura` | Semente aleatória para a geração de textura. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `qualidade_da_textura` | Nível de qualidade para a geração de textura: `detailed` = texturas HD, `extreme` = texturas Ultra 8K. (padrão: `"standard"`) | COMBO | Não | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `alinhamento_da_textura` | Método de alinhamento para a mapeamento de textura. (padrão: `"original_image"`) | COMBO | Não | `"original_image"`<br>`"geometry"` |
| `limite_de_faces` | Número máximo de faces. -1 permite que a Tripo escolha adaptivamente (aproximadamente 1,4M faces na versão 3.x padrão, 2M na detalhada). A Tripo limita silenciosamente: v2.5 em 500.000, malhas quadrangulares em 150.000. (padrão: -1) | INT | Não | -1 a 2000000 |
| `quad` | Saída de malha quadrangular. A Tripo entrega malhas quadrangulares em FBX, então o resultado chega no saída FBX e a saída GLB permanece vazia. (padrão: False) | BOOLEAN | Não | True<br>False |
| `qualidade_da_geometria` | Nível de qualidade para a geração de geometria. (padrão: `"standard"`) | COMBO | Não | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Malha low-poly com estilo topológico limpo e manual (500-20.000 faces, quadrangulares 500-10.000). Melhor para sujeitos simples; os complexos podem falhar. (padrão: False) | BOOLEAN | Não | True<br>False |
| `auto_size` | Escala modelos texturados para o tamanho real do mundo em metros. A Tripo armazena o tamanho como a transformação da cena do modelo e cozinha isso quando o modelo é convertido, equipado ou retargetado; ignorado sem textura. (padrão: True) | BOOLEAN | Não | True<br>False |

Nota: Uma `image` é obrigatória; se estiver ausente, o nó gera um RuntimeError. Quando `texture` é False, o modelo contém apenas geometria nua e `pbr` é forçado a False. Quando `smart_low_poly` está ativado, `face_limit` deve estar entre 500 e 20.000 para malhas triangulares, ou entre 500 e 10.000 quando `quad` também está ativado; se o limite for inválido, o nó gera um ValueError. Definindo `face_limit` como -1 (o padrão) não envia nenhum limite explícito para a API, permitindo que a Tripo escolha adaptivamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | O arquivo do modelo 3D gerado (apenas para compatibilidade reversa). | STRING |
| `task_id_do_modelo` | O ID da tarefa para rastrear o processo de geração do modelo. | ID_DA_TAREFA_DO_MODELO |
| `GLB` | O modelo 3D gerado no formato GLB. Fica vazio quando `quad` está ativado. | ARQUIVO3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. Somente preenchido quando `quad` está ativado. | ARQUIVO3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `79ebe76234036e8284640d7eaeee3a1220975b8adc043994de7de0ee161ccd45`
