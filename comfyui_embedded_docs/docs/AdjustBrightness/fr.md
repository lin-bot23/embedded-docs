# Ajuster la luminosité

Le nœud Adjust Brightness modifie la luminosité d'une image d'entrée. Il fonctionne en multipliant la valeur de chaque pixel par un facteur spécifié, puis en limitant les valeurs résultantes pour qu'elles restent dans une plage valide. Un facteur de 1.0 laisse l'image inchangée, les valeurs inférieures à 1.0 l'assombrissent, et les valeurs supérieures à 1.0 l'éclaircissent. Si l'image d'entrée possède un canal alpha, celui-ci est conservé tel quel afin de préserver la transparence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à ajuster. | IMAGE | Oui | - |
| `facteur` | Facteur de luminosité. 1.0 = aucun changement, <1.0 = plus sombre, >1.0 = plus clair. (défaut : 1.0) | FLOAT | Non | 0.0 - 2.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | L'image de sortie avec une luminosité ajustée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/fr.md)

---
**Source fingerprint (SHA-256):** `64c1499d16deb5922fa63538182cd227e8f2ba9ded5962064ce9f228a0f4a163`
