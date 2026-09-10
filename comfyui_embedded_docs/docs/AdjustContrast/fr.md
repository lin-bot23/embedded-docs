# Ajuster le contraste

Le nœud Adjust Contrast ajuste le contraste d'une image d'entrée en mettant à l'échelle la différence entre les zones claires et sombres autour du point médian de la plage de couleurs. Un facteur de 1.0 laisse l'image inchangée, les valeurs inférieures à 1.0 réduisent le contraste et les valeurs supérieures à 1.0 l'augmentent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée dont le contraste doit être ajusté. | IMAGE | Oui | - |
| `facteur` | Facteur de contraste. 1.0 = aucun changement, <1.0 = moins de contraste, >1.0 = plus de contraste. (par défaut : 1.0) | FLOAT | Non | 0.0 - 2.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | L'image résultante avec le contraste ajusté. Les valeurs de pixel sont limitées à la plage 0.0–1.0. Si l'image d'entrée possède un canal alpha, ce canal est conservé inchangé. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/fr.md)

---
**Source fingerprint (SHA-256):** `489f840cc3d98339a5cf7b55e9179c60878c58b2f992740796c7d49642e05932`
