# Obtenir la taille de l'image

GetImageSize lit une image d’entrée et renvoie sa largeur, sa hauteur et sa taille de lot. Le nœud affiche également ces valeurs mesurées directement sur son interface.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `image` | L’image d’entrée à partir de laquelle la largeur, la hauteur et la taille du lot sont extraites | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `width` | La largeur de l’image d’entrée en pixels | INT |
| `height` | La hauteur de l’image d’entrée en pixels | INT |
| `batch_size` | Le nombre d’images contenues dans le lot d’entrée | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/fr.md)

---
**Source fingerprint (SHA-256):** `dc29add37a3362384e63cb1e57f03758a82f77811c78797fdffd486462cb19b8`
