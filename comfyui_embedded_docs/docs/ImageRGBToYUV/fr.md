# ImageRGBToYUV

Le nœud ImageRGBToYUV convertit une image RVB dans l’espace colorimétrique YUV. Il décompose l’image en trois composantes — Y (luminance, ou luminosité), U (chrominance de différence bleue) et V (chrominance de différence rouge) — et renvoie chaque composante sous forme d’image distincte, de même taille que l’image d’entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image RVB d’entrée à convertir en YUV. Si l’image contient un canal alpha, seuls les trois premiers canaux (RVB) sont utilisés. | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------------|
| `Y` | La composante de luminance (luminosité) de l’espace colorimétrique YUV | IMAGE |
| `U` | La composante de chrominance de différence bleue de l’espace colorimétrique YUV | IMAGE |
| `V` | La composante de chrominance de différence rouge de l’espace colorimétrique YUV | IMAGE |

Chaque sortie a la même largeur, la même hauteur et le même nombre de canaux que l’image d’entrée. La composante correspondante Y, U ou V est répétée sur tous les canaux afin que chaque sortie soit renvoyée sous forme d’image standard.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/fr.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
