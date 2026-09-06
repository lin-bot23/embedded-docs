# ImageYUVToRGB

# Image YUV vers RGB

Le nœud ImageYUVToRGB est conçu pour convertir des images du espace de couleur YUV en espace de couleur RGB. Il le fait en prenant trois images d'entrée distinctes qui représentent les canaux Y (luminance), U (projection bleue) et V (projection rouge) de l'image. Ces canaux sont ensuite combinés pour former une image RGB unique à l'aide d'une technique de conversion d'espace de couleur.

## Aperçu

Le nœud ImageYUVToRGB convertit des images YUV en images RGB en combinant les canaux Y, U et V. Cela est utile pour les applications nécessitant une conversion d'espace de couleur entre ces deux normes.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `Y`       | L'image d'entrée du canal Y, représentant les informations de luminance. | IMAGE | Oui | - |
| `U`       | L'image d'entrée du canal U, représentant la différence de couleur bleue. | IMAGE | Oui | - |
| `V`       | L'image d'entrée du canal V, représentant la différence de couleur rouge. | IMAGE | Oui | - |

**Note:** Les canaux Y, U et V doivent être fournis ensemble et devraient avoir les mêmes dimensions pour assurer une conversion correcte.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output`    | L'image RGB resulting after the YUV to RGB conversion. | IMAGE |

L'image de sortie aura les mêmes dimensions que les images d'entrée Y, U et V, mais avec les informations de couleur représentées dans l'espace de couleur RGB.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/fr.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
