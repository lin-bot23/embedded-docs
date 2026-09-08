# OpenAI ChatGPT

Ce nœud génère des réponses textuelles à partir d'un modèle OpenAI. Il prend un texte d'invite et, en option, des images ou des fichiers en tant que contexte, puis envoie cette information à un modèle OpenAI pour générer une réponse textuelle.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `invite` | Entrées textuelles pour le modèle, utilisées pour générer une réponse. Ce est le texte auquel le modèle doit répondre. | STRING | Oui | - |
| `conserver_contexte` | Ce paramètre est obsolète et n'a aucun effet. Il est inclus pour la compatibilité ascendante mais n'influence pas le comportement du nœud. | BOOLEAN | Non | - |
| `modèle` | Le modèle utilisé pour générer la réponse. Sélectionnez parmi les modèles OpenAI disponibles. | COMBO | Oui | gpt-6-astra<br>gpt-5.6-sol<br>gpt-5.6-terra<br>gpt-5.6-luna<br>gpt-5.5-pro<br>gpt-5.5<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br>gpt-4.1<br>gpt-4.1-mini<br>gpt-4.1-nano<br>o4-mini<br>o3<br>o1-pro<br>o1 |
| `images` | Images optionnelles à utiliser en tant que contexte pour le modèle. Pour inclure plusieurs images, utilisez le nœud Batch Images. | IMAGE | Non | - |
| `fichiers` | Fichiers optionnels à utiliser en tant que contexte pour le modèle. Accepte les entrées du nœud OpenAI Chat Input Files. | OPENAI_INPUT_FILES | Non | - |
| `options_avancées` | Configuration optionnelle pour le modèle. Accepte les entrées du nœud OpenAI Chat Advanced Options. | OPENAI_CHAT_CONFIG | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output_text` | La réponse textuelle générée par le modèle OpenAI. Ce est le texte généré en fonction de l'invite d'entrée et du contexte. | STRING |

## Notes

- Le paramètre `persist_context` est obsolète et n'a aucun effet. Il est inclus pour la compatibilité ascendante mais ne doit pas être utilisé.
- L'entrée `images` peut être utilisée pour fournir un contexte supplémentaire au modèle. Si plusieurs images sont fournies, elles doivent être connectées à l'aide du nœud Batch Images.
- L'entrée `files` permet de fournir un contexte supplémentaire sous forme de fichiers. Ces fichiers doivent être connectés à partir du nœud OpenAI Chat Input Files.
- L'entrée `advanced_options` permet une configuration plus détaillée du comportement du modèle. Cela doit être connecté à partir du nœud OpenAI Chat Advanced Options.
- Le coût d'utilisation de ce nœud dépend du modèle sélectionné. Le coût est calculé en fonction du nombre de jetons utilisés par le modèle. Le coût exact sera affiché dans l'UI du nœud.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/fr.md)

---
**Source fingerprint (SHA-256):** `687a6b1110518a2eaf23e240f43991b4ff91d6f01cae6c3ef55bcdac810e7a89`
