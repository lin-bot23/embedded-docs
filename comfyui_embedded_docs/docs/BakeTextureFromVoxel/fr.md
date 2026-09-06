# Pré-calculer la texture depuis le voxel

Ce nœud cuit des textures PBR sur un maillage 3D à l’aide de la disposition UV existante du maillage. Il échantillonne les attributs de couleur et de matériau dans un volume de voxels épars pour chaque texel et produit une image de couleur de base ainsi que des cartes de métallicité et de rugosité. Il ne déplie pas le maillage : un nœud de dépliage UV doit donc être connecté en amont.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage 3D sur lequel cuire les textures. Il doit déjà comporter une disposition UV ; un nœud de dépliage UV doit être connecté en amont. | MESH | Oui | |
| `voxel_colors` | Volume de voxels épars contenant des couleurs par voxel et des attributs PBR facultatifs (canaux de métallicité et de rugosité). | VOXEL | Oui | |
| `texture_size` | Résolution de l’atlas UV carré (nom affiché : « resolution », valeur par défaut : 2048). | INT | Oui | 64 à 8192 |
| `reference_mesh` | Maillage dense facultatif correspondant à l’état avant décimation ; il rétroprojette chaque texel sur sa surface réelle avant l’échantillonnage, supprimant ainsi l’aspect facetté de la cuisson sur les maillages grossiers. | MESH | Non | |

Remarques :

- Le maillage d’entrée doit avoir des UV. Si aucun UV n’est présent, le nœud lève une erreur. Les UV doivent être en correspondance 1:1 avec les sommets (un UV par sommet).
- Lorsque le maillage et les coordonnées de voxels contiennent une dimension de lot, chaque élément du lot est cuit séparément. Si un élément du lot n’a ni voxels ni faces, il est ignoré et une texture noire est générée pour celui-ci.
- Lorsque `reference_mesh` est fourni pour un lot, il est apparié par index de lot, sauf s’il ne contient qu’un seul maillage, auquel cas ce maillage est utilisé pour tous les éléments.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `base_color` | Carte de texture de couleur de base RVB. Les valeurs sont des flottants dans la plage 0–1. | IMAGE |
| `metallic` | Carte de métallicité en niveaux de gris (flottant, 0–1). Noire lorsque les couleurs des voxels ne contiennent aucun canal de métallicité. | IMAGE |
| `roughness` | Carte de rugosité en niveaux de gris (flottant, 0–1). Noire lorsque les couleurs des voxels ne contiennent aucun canal de rugosité. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/fr.md)

---
**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`
