# Tripo: Multiview para Modelo

Este nó gera modelos 3D de forma síncrona usando a API da Tripo, processando até quatro imagens que mostram diferentes vistas de um objeto (frente, esquerda, traseira, direita). Ele requer uma imagem da vista da frente e pelo menos uma vista adicional (esquerda, traseira ou direita) para construir o modelo 3D. Textura, material PBR, qualidade da geometria e formato de saída podem ser controlados a partir do nó.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | Imagem da vista da frente do objeto. | IMAGEM | Sim | - |
| `imagem_esquerda` | Imagem da vista da esquerda do objeto. | IMAGEM | Não | - |
| `imagem_traseira` | Imagem da vista da traseira do objeto. | IMAGEM | Não | - |
| `imagem_direita` | Imagem da vista da direita do objeto. | IMAGEM | Não | - |
| `versão_do_modelo` | Versão do modelo a ser usada para a geração. | COMBO | Não | Múltiplas opções disponíveis |
| `orientação` | Configuração de orientação para o modelo 3D (padrão: `"default"`). | COMBO | Não | Múltiplas opções disponíveis |
| `textura` | Gera mapas de textura. Desligar retorna geometria nua e ignora PBR. (padrão: True) | BOOLEAN | Não | - |
| `pbr` | Mapas de material PBR (cor de base, metálico, rugosidade, normal). Requer textura. (padrão: True) | BOOLEAN | Não | - |
| `semente_do_modelo` | Semente aleatória para a geração do modelo (padrão: 42). | INT | Não | 0 a 2,147,483,647 |
| `semente_da_textura` | Semente aleatória para a geração da textura (padrão: 42). | INT | Não | 0 a 2,147,483,647 |
| `qualidade_da_textura` | Nível de qualidade para a geração da textura (padrão: `"standard"`). `"detailed"` = Texturas em HD, `"extreme"` = Texturas Ultra em 8K. | COMBO | Não | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `alinhamento_da_textura` | Método usado para alinhar as texturas ao modelo (padrão: `"original_image"`). | COMBO | Não | `"original_image"`<br>`"geometry"` |
| `limite_de_faces` | Número máximo de faces. -1 permite que a Tripo escolha adaptativamente (aproximadamente 1,4M faces na versão 3.x padrão, 2M na detalhada). A Tripo limita silenciosamente: v2.5 em 500.000, malhas quadrangulares em 150.000. (padrão: -1) | INT | Não | -1 a 2.000.000 |
| `quad` | Saída de malha quadrangular. A Tripo fornece malhas quadrangulares em FBX, então o resultado chega no saída FBX e a saída GLB permanece vazia. (padrão: False) | BOOLEAN | Não | - |
| `qualidade_da_geometria` | Nível de qualidade para a geração da geometria (padrão: `"standard"`). | COMBO | Não | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Malha low-poly com estilo topologia manualmente fabricada limpa (500-20.000 faces, quadrangulares 500-10.000). Melhor para sujeitos simples; os complexos podem falhar. (padrão: False) | BOOLEAN | Não | - |
| `auto_size` | Escala modelos texturizados para o tamanho real do mundo em metros. A Tripo armazena o tamanho como a transformação da cena do modelo e cozinha isso quando o modelo é convertido, rigado ou retargetado; ignorado sem textura. (padrão: False) | BOOLEAN | Não | - |

**Nota:** A imagem da vista da frente (`image`) é sempre obrigatória, e pelo menos uma das imagens `image_left`, `image_back` ou `image_right` também deve ser fornecida. Desligar `texture` automaticamente desliga `pbr` também, pois `pbr` requer textura. Quando `smart_low_poly` está ativado e `face_limit` não é deixado em -1, `face_limit` deve estar entre 500 e 20.000 para malhas triangulares ou entre 500 e 10.000 para malhas quadrangulares.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_do_modelo` | Caminho ou identificador do arquivo do modelo 3D gerado (apenas para compatibilidade reversa). | STRING |
| `task_id_do_modelo` | Identificador da tarefa para rastreamento do processo de geração do modelo. | ID_TAREFA_MODELO |
| `GLB` | O modelo 3D gerado no formato GLB. Fica vazio quando `quad` está ativado. | ARQUIVO3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. Somente preenchido quando `quad` está ativado. | ARQUIVO3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `73f1259dcba75ce1d56aabb6f0435f11d21eee3268f93502c4c3293d562a6db0`
