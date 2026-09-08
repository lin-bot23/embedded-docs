# ImageRGBToYUV

# Image RGB vers YUV

Le nœud ImageRGBToYUV effectue une conversion de l'espace de couleur RGB vers YUV. Il prend une image RGB en entrée et produit trois images séparées représentant les canaux YUV : Y (luminance), U (différence bleue) et V (différence rouge).

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|----------------|--------------|-------|
| `image`   | L'image RGB en entrée à convertir en espace de couleur YUV. Cette image doit être à trois canaux. | IMAGE | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `Y`           | Le canal Y représente la luminance (luminosité) de l'image. | IMAGE |
| `U`           | Le canal U représente le composant chroma de différence bleue. | IMAGE |
| `V`           | Le canal V représente le composant chroma de différence rouge. | IMAGE |

Les images de sortie auront les mêmes dimensions que l'image d'entrée.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/fr.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
