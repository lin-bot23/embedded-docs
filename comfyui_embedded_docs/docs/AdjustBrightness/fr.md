# Ajuster la luminosité

Le nœud Adjust Brightness modifie la luminosité apparente d'une image. Il multiplie les valeurs de couleur de l'image par un facteur `factor` et conserve les résultats dans la plage valide de 0.0 à 1.0. Un facteur de 1.0 laisse l'image inchangée, les valeurs inférieures à 1.0 l'assombrissent, et les valeurs supérieures à 1.0 l'éclaircissent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à ajuster. Accepte une image unique ou un lot d'images. | IMAGE | Oui | - |
| `facteur` | Facteur de luminosité. 1.0 = aucun changement, <1.0 = plus sombre, >1.0 = plus clair. (valeur par défaut : 1.0) | FLOAT | Non | 0.0 - 2.0 |

Remarque : si l'image d'entrée possède un canal alpha (RGBA), seuls les canaux de couleur sont ajustés. Le canal alpha est copié depuis l'entrée sans modification, car il stocke la transparence, pas la couleur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | L'image de sortie avec la luminosité ajustée. Si l'entrée possède un canal alpha, les valeurs alpha restent inchangées. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/fr.md)

---
**Source fingerprint (SHA-256):** `64c1499d16deb5922fa63538182cd227e8f2ba9ded5962064ce9f228a0f4a163`
