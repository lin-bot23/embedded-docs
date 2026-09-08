# Options avancées OpenAI ChatGPT

# Options Avancées ChatGPT d'OpenAI

Le nœud Options Avancées ChatGPT d'OpenAI permet de définir des configurations supplémentaires pour les nœuds ChatGPT d'OpenAI. Ce nœud fournit des paramètres avancés qui contrôlent la manière dont le modèle génère des réponses, y compris le comportement de troncature, les limites de longueur des sorties et les instructions personnalisées.

## Aperçu

Le nœud Options Avancées ChatGPT d'OpenAI est conçu pour améliorer les fonctionnalités des nœuds ChatGPT d'OpenAI en permettant aux utilisateurs de spécifier des options de configuration avancées. Ces paramètres peuvent aider à adapter la génération de réponses du modèle aux exigences spécifiques.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `troncature` | Stratégie de troncature à utiliser pour la réponse du modèle. auto : Si le contexte de cette réponse et des précédentes dépasse la taille de la fenêtre de contexte du modèle, le modèle tronquera la réponse pour l'ajuster à la fenêtre de contexte en supprimant des éléments d'entrée au milieu de la conversation. disabled : Si une réponse du modèle dépasse la taille de la fenêtre de contexte pour un modèle, la requête échouera avec un code 400 (par défaut : "auto") | STRING | Oui | "auto"<br>"disabled" |
| `jetons_sortie_max` | Limite supérieure pour le nombre de tokens pouvant être générés pour une réponse, y compris les tokens de sortie visibles et les tokens de raisonnement (par défaut : 4096) | INT | Non | 16 à 16384 |
| `instructions` | Instructions pour le modèle sur la manière de générer la réponse (prise en charge des entrées en plusieurs lignes) | STRING | Non | - |
| `reasoning_effort` | Degré de raisonnement du modèle avant de répondre. 'default' laisse le choix au modèle. Les niveaux pris en charge varient selon le modèle : GPT-6 Astra low-max, GPT-5.6 none-max (sans minimal), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high ; GPT-4.1 n'a pas de raisonnement. Les niveaux non pris en charge sont rejetés avant l'envoi de la requête (par défaut : "default") | STRING | Non | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | Objet de configuration contenant les paramètres spécifiés pour utilisation avec les nœuds ChatGPT d'OpenAI | OPENAI_CHAT_CONFIG |

## Notes

- Le paramètre `max_output_tokens` définit une limite supérieure sur le nombre total de tokens, y compris les tokens de sortie visibles et les tokens de raisonnement.
- Le paramètre `reasoning_effort` permet de spécifier le niveau de raisonnement que le modèle doit appliquer avant de générer une réponse. Les niveaux pris en charge varient selon le modèle utilisé.
- Le paramètre `instructions` peut être utilisé pour fournir des instructions détaillées au modèle pour guider le processus de génération de la réponse.
- Le paramètre `truncation` détermine si le modèle doit tronquer automatiquement la réponse si elle dépasse la taille de la fenêtre de contexte ou échouer avec un code 400.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/fr.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
