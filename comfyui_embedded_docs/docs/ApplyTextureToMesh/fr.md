# Appliquer une texture au maillage

Ce nœud attache des images de textures cuites à la disposition UV d'un maillage afin qu'elles puissent être exportées avec le maillage par le nœud SaveGLB. Connectez le même maillage déplié UV que vous avez utilisé pour la cuisson, ainsi que les cartes d'images cuites. Les cartes optionnelles de métallique, de rugosité et d'occlusion sont regroupées dans une seule texture ORM, et la fourniture d'une carte normale stocke également les normales lisses et les tangentes nécessaires à un ombrage correct.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `mesh` | Le maillage déplié UV auquel les textures cuites seront attachées. Doit être le même maillage que celui utilisé lors de la cuisson ; une erreur est déclenchée si le maillage n'a pas d'UV. | MESH | Oui | — |
| `base_color` | L'image de couleur de base cuite. Stockée comme texture du maillage et limitée à la plage 0-1. | IMAGE | Oui | — |
| `metallic` | La carte de métallique cuite. Utilisée comme canal bleu de la texture ORM combinée ; la valeur par défaut est 0 lorsqu'elle n'est pas fournie. | IMAGE | Non | — |
| `roughness` | La carte de rugosité cuite. Utilisée comme canal vert de la texture ORM combinée ; la valeur par défaut est 1 lorsqu'elle n'est pas fournie. | IMAGE | Non | — |
| `occlusion` | La carte d'occlusion ambiante cuite. Utilisée comme canal rouge de la texture ORM combinée ; la valeur par défaut est 1 lorsqu'elle n'est pas fournie. Lorsqu'elle est fournie, la texture ORM est également marquée comme texture d'occlusion pour SaveGLB. | IMAGE | Non | — |
| `normal_map` | La carte normale cuite dans l'espace tangent. Lorsqu'elle est fournie, le nœud recalcule la base tangente par sommet et exporte des normales de sommet lisses afin que la carte normale ombrage correctement. | IMAGE | Non | — |

Remarque : lorsque l'un des paramètres `metallic`, `roughness` ou `occlusion` est connecté, les trois sont regroupés dans une seule texture ORM glTF avec les canaux R = occlusion, G = rugosité, B = métallique. Les cartes manquantes sont remplies avec les valeurs par défaut (occlusion 1, rugosité 1, métallique 0), et les cartes de résolutions différentes sont redimensionnées à la largeur et à la hauteur les plus grandes. Lorsque `normal_map` est connecté, les normales du maillage sont remplacées par des normales de sommet lisses calculées et une base tangente est ajoutée. Les coordonnées UV en dehors de la plage [0,1] sont mises à l'échelle uniformément dans [0,1] tout en préservant le rapport hauteur/largeur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage d'entrée avec les images de textures attachées à sa disposition UV, prêt à être sauvegardé par SaveGLB. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/fr.md)

---
**Source fingerprint (SHA-256):** `7492922c9c7c0117366cb8b9017fc192eb8dd6b6594fd429044d60408693210e`
