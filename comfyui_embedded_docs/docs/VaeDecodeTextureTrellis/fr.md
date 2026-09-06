# VaeDecodeTextureTrellis

Ce nœud décode un latent de texture Trellis2 en couleurs de voxels à l’aide d’un VAE. Le latent d’entrée contient des échantillons de caractéristiques éparses avec leurs coordonnées ; le nœud reconstruit la couleur de chaque voxel et renvoie le résultat sous forme de grille de voxels que les nœuds aval, tels que PaintMesh, peuvent utiliser pour colorer un maillage 3D.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `samples` | Le latent de texture à décoder. Il contient les caractéristiques des échantillons et les coordonnées éparses, et peut inclure des métadonnées facultatives telles que le nombre de coordonnées, la trame du modèle et la résolution des coordonnées. | LATENT | Oui | — |
| `vae` | Le VAE Trellis2 utilisé pour décoder le latent de texture en couleurs de voxels. | VAE | Oui | — |
| `shape_subdivides` | Informations de forme utilisées pour guider une reconstruction plus détaillée pendant le décodage. Elles aident à préserver la cohérence de la structure aux résolutions plus élevées. | SHAPE_SUBDIVIDES | Oui | — |

Remarque : lorsque le latent `samples` inclut des nombres de coordonnées, ceux-ci doivent être non négatifs, leur total doit correspondre au nombre de lignes de coordonnées, et chaque lot doit contenir exactement le nombre de lignes attendu ; sinon, le nœud génère une erreur. Si la trame du modèle du latent est « z_up », les coordonnées de voxels décodées sont remappées en Y-up afin de s’aligner sur les sommets du maillage. Lorsqu’une résolution de coordonnées est fournie, la résolution de la texture de sortie correspond à cette valeur multipliée par 16 ; sinon, elle est déduite de la plus grande coordonnée de voxel et arrondie à l’une des valeurs 256, 512, 1024, 1536 ou 2048 (1024 lorsqu’aucune coordonnée n’est disponible).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `voxel_colors` | Données de voxels décodées contenant les coordonnées, les caractéristiques de couleur et la résolution de texture. Chaque voxel possède 6 canaux de couleur : couleur de base (RVB), métallique, rugosité et alpha, tous dans la plage [0, 1]. Les consommateurs de couleurs par sommets tels que PaintMesh utilisent les 3 premiers canaux. | VOXEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/fr.md)

---
**Source fingerprint (SHA-256):** `952ea7d7a0147519392bebe352a0da731462db278c8640fa527aa5b6f64e4aa7`
