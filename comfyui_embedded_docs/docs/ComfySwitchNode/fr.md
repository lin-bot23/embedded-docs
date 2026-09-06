# Commutateur

Le nœud Switch sélectionne entre deux entrées possibles en fonction d'une condition booléenne. Lorsque `switch` est activé (true), il transmet l'entrée `on_true` vers la sortie ; lorsqu'il est désactivé (false), il transmet `on_false`. Seule la branche sélectionnée est évaluée, l'autre entrée n'a donc pas besoin d'être connectée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `interrupteur` | Une condition booléenne qui détermine quelle entrée transmettre. Lorsqu'il est activé (true), l'entrée `on_true` est sélectionnée. Lorsqu'il est désactivé (false), l'entrée `on_false` est sélectionnée. | BOOLEAN | Oui |  |
| `faux` | Les données à transmettre à la sortie lorsque `switch` est désactivé (false). Cette entrée n'est requise que lorsque `switch` est false. | MATCH_TYPE | Non |  |
| `vrai` | Les données à transmettre à la sortie lorsque `switch` est activé (true). Cette entrée n'est requise que lorsque `switch` est true. | MATCH_TYPE | Non |  |

**Remarque sur les exigences d'entrée :** les entrées `on_false` et `on_true` sont requises de manière conditionnelle. Le nœud demande l'entrée `on_true` uniquement lorsque `switch` est true, et l'entrée `on_false` uniquement lorsque `switch` est false. Les deux entrées doivent être du même type de données et doivent correspondre au type de données de sortie. Si l'entrée sélectionnée n'est pas connectée, le nœud ne produit aucune valeur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sortie` | Les données sélectionnées. Il s'agit de la valeur provenant de l'entrée `on_true` lorsque `switch` est true, ou de la valeur provenant de l'entrée `on_false` lorsque `switch` est false. | MATCH_TYPE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/fr.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
