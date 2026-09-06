# Déplier les UV du maillage

Génère un atlas UV pour un maillage 3D. La surface du maillage est découpée en charts, chaque chart est aplati en deux dimensions, puis les charts aplatis sont regroupés dans un atlas UV [0,1]. Les sommets situés sur les coutures des charts sont dupliqués, de sorte que le maillage de sortie peut contenir plus de sommets que le maillage d’entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `maillage` | Le maillage d’entrée à déplier. Accepte un seul maillage ou un lot de maillages. | MESH | Oui | — |
| `segmenteur` | Algorithme de segmentation à utiliser. `pec` : segmentation rapide par contraction parallèle des arêtes sur GPU. `adaptive` : CPU, plus lent. (par défaut : "pec") | COMBO | Oui | "pec"<br>"adaptive" |
| `résolution` | Résolution cible de l’atlas pour la mise à l’échelle automatique de la densité de texels (0 = ajuster au contenu). (par défaut : 1024) | INT | Oui | 0 à 8192 (pas 256) |
| `marge` | Marge en texels entre les charts. (par défaut : 1) | INT | Oui | 0 à 16 |
| `weld_distance` | Rayon de fusion des sommets coïncidents, exprimé en fraction de l’étendue du maillage (0 = automatique). Augmentez la valeur jusqu’à ~0.001 si vous obtenez des charts par triangle (entrée non fusionnée). (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 (pas 0.0001) |

Remarque : si le maillage d’entrée contient des sommets non fusionnés, le nœud peut signaler une faible adjacence des faces et produire des charts UV par face ; l’augmentation de `weld_distance` fusionne les sommets coïncidents avant le dépliage.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `maillage` | Le maillage d’entrée avec un atlas UV généré dans l’intervalle [0,1]. Les sommets des coutures sont dupliqués, de sorte que le nombre de sommets en sortie peut dépasser celui du maillage d’entrée. Les couleurs de sommets et la texture du maillage d’entrée sont préservées. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/fr.md)

---
**Source fingerprint (SHA-256):** `fcab6f0b621693d862ee74b5ec498498d2f1f247a66f478704377598a6b39388`
