# Pré-visualizar como Texto

PreviewAny converte qualquer valor de entrada em texto legível, permitindo que você o insira. Strings passam inalteradas, números e booleanos se tornam texto puro, e outros tipos de dados são serializados em JSON quando possível (recaindo para sua forma de string simples se a serialização falhar). O texto resultante é exibido na interface do usuário e também retornado como uma string de saída para processamento adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `source` | Aceita qualquer tipo de dados de entrada para exibição de pré-visualização. Se nenhum valor for fornecido, o pré-visualização mostra 'Nenhum'. | QUALQUER | Sim | Qualquer tipo de dados |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `result` | O valor de entrada convertido para formato de texto. O mesmo texto também é exibido na interface do usuário. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/pt-BR.md)

---
**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`
