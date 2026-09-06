# Re-maillage du maillage (DC à bande étroite)

Remesh Mesh reconstruit un maillage avec une tessellation propre et uniforme en échantillonnant un champ de distance à bande étroite autour de la surface d’origine et en l’extrayant par Dual Contouring. Cette opération normalise les topologies désordonnées, non-manifold ou auto-intersectées. Elle est conçue pour être exécutée avant Decimate Mesh afin d’atteindre un nombre de faces exact. Le traitement s’exécute sur le périphérique de calcul actif et le maillage de sortie reste fusionné.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Le maillage d’entrée à remailler. | MESH | Oui | — |
| `resolution` | Résolution de la grille de voxels (densité de sortie). 256 ~ 100k faces, 512 ~ 1M. Pour un nombre de faces exact, utilisez ensuite Decimate Mesh. (défaut : 512) | INT | Oui | 32 - 2048 |
| `sign_mode` | Mode d’extraction de surface. « "udf" » est robuste aux entrées désordonnées/non-manifold ; « "sdf" » produit une surface unique et propre avec récupération des arêtes vives par QEF (fonction d’erreur quadratique), mais nécessite un enroulement cohérent. La sélection d’un mode révèle ses sous-options spécifiques. (défaut : "udf") | DYNAMIC_COMBO | Oui | "udf"<br>"sdf" |
| `band` | Largeur de la bande étroite en unités de voxel. En mode UDF, décale également la surface. (avancé, défaut : 1.0) | FLOAT | Oui | 0.5 - 4.0 |
| `project_back` | Interpole linéairement les sommets vers la surface d’origine (0 = DC pur, 1 = projeté sur la surface). (avancé, défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 |
| `fix_poles` | Fusionne les paires de sommets de valence 3 (artefact de jonction en T du DC). (avancé, défaut : false) | BOOLEAN | Oui | true / false |
| `smooth_iters` | Itérations de lissage de Taubin (0 = désactivé). 2-3 nettoient les artefacts en escalier du DC ; des valeurs plus élevées lissent excessivement les arêtes QEF. (défaut : 0) | INT | Oui | 0 - 20 |
| `drop_small_components` | Supprime les composantes dont le nombre de faces est inférieur à cette fraction de la plus grande. 0 désactive l’option. (avancé, défaut : 0.01) | FLOAT | Oui | 0.0 - 0.5 |
| `precluster_max_verts` | Limite le nombre de sommets en entrée avant les requêtes de champ ; les maillages au-dessus de cette valeur sont d’abord décimés par clusters jusqu’à cette cible. Évite les dépassements de mémoire sur les très gros maillages. (avancé, défaut : 20,000,000) | INT | Oui | 0 - 100,000,000 |

### Entrées du mode "udf"

Ces paramètres apparaissent lorsque `sign_mode` est défini sur `"udf"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `qef` | Placement des sommets duaux par QEF (fonction d’erreur quadratique) pour des arêtes plus nettes. (défaut : false) | BOOLEAN | Non | true / false |
| `drop_inverted_components` | Supprime les composantes fermées à normale rentrante (volume négatif) — la coque interne de l’UDF. (défaut : false) | BOOLEAN | Non | true / false |
| `drop_enclosed_components` | Supprime les composantes situées dans la boîte englobante de la plus grande qui échouent au test de raycast point-dans-maillage. Désactivez cette option pour conserver les pièces imbriquées légitimes. (défaut : false) | BOOLEAN | Non | true / false |

### Entrées du mode "sdf"

Ces paramètres apparaissent lorsque `sign_mode` est défini sur `"sdf"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `qef` | Placement des sommets duaux par QEF (fonction d’erreur quadratique), ce qui permet de retrouver les arêtes vives, plutôt qu’un centroïde d’intersections d’arêtes. (défaut : true) | BOOLEAN | Non | true / false |
| `manifold` | Dual Contouring manifold : 1 à 4 sommets duaux par voxel pour les cas à plusieurs nappes. Plus lent. (défaut : false) | BOOLEAN | Non | true / false |

Remarque : l’option `qef` a une valeur par défaut différente selon le mode sélectionné — false en mode "udf", true en mode "sdf". Lorsque `precluster_max_verts` est supérieur à 0 et que le maillage d’entrée contient plus de sommets que cette valeur, le maillage est d’abord décimé par clusters jusqu’à cette cible avant les requêtes de champ. Après le traitement, le nœud affiche le changement du nombre de faces entre l’entrée et la sortie (par exemple, « faces : 1.23M → 200K (-84%) »).

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `mesh` | Le maillage remaillé avec une tessellation uniforme et une topologie fusionnée. Les couleurs de sommets sont conservées lorsqu’elles sont présentes sur l’entrée ; les UV, normales et tangentes ne sont pas reportées. | MESH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/fr.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`
