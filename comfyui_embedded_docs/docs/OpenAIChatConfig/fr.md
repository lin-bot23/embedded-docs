# Options avancées OpenAI ChatGPT

Le nœud OpenAIChatConfig vous permet de définir des options avancées qui contrôlent la façon dont le nœud OpenAI Chat génère les réponses. Vous pouvez définir la stratégie de troncature, limiter le nombre de jetons de sortie, fournir des instructions personnalisées et choisir à quel point le modèle doit raisonner avant de répondre.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `troncature` | La stratégie de troncature à utiliser pour la réponse du modèle. auto : si le contexte de cette réponse et des réponses précédentes dépasse la taille de la fenêtre de contexte du modèle, le modèle tronque la réponse pour l’adapter à la fenêtre de contexte en supprimant des éléments d’entrée au milieu de la conversation. disabled : si la réponse d’un modèle dépasse la taille de la fenêtre de contexte de ce modèle, la requête échoue avec une erreur 400 (défaut : « auto ») | COMBO | Oui | « auto »<br>« disabled » |
| `jetons_sortie_max` | Une limite supérieure du nombre de jetons pouvant être générés pour une réponse, y compris les jetons de sortie visibles et les jetons de raisonnement (défaut : 4096) | INT | Non | 16 à 16384 |
| `instructions` | Instructions données au modèle sur la manière de générer la réponse (saisie multiligne prise en charge) | STRING | Non | - |
| `reasoning_effort` | Le degré de raisonnement que le modèle applique avant de répondre. « default » laisse le choix au modèle. Les niveaux pris en charge varient selon le modèle : GPT-6 Astra low-max, GPT-5.6 none-max (pas de minimum), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high ; GPT-4.1 n’effectue aucun raisonnement. Les niveaux non pris en charge sont rejetés avant l’envoi de la requête. (défaut : « default ») | COMBO | Non | « default »<br>« none »<br>« minimal »<br>« low »<br>« medium »<br>« high »<br>« xhigh »<br>« max » |

Remarque : bien que `top_p` et `temperature` soient répertoriés comme propriétés dans la spécification API, ils ne sont pas pris en charge pour tous les modèles et ne sont donc pas exposés comme entrées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `OPENAI_CHAT_CONFIG` | Objet de configuration contenant les paramètres spécifiés pour une utilisation avec les nœuds OpenAI Chat | OPENAI_CHAT_CONFIG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/fr.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
