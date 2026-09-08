# Tripo : Modèle de texture

Le nœud TripoTextureNode ajoute des textures à un modèle 3D Tripo existant via l’API Tripo. Il prend l’ID de tâche d’un modèle créé par un autre nœud Tripo et renvoie un modèle texturé GLB ou FBX une fois la tâche de texturation terminée. Vous pouvez contrôler les cartes de matériaux, la qualité des textures, l’alignement, la graine, et guider les textures à l’aide d’une invite de texte, d’une image de style ou d’images de référence.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `modèle_id_tâche` | L’ID de tâche Tripo du modèle à texturer. Accepte les ID de tâche de modèle et les ID de tâche de segmentation. | MODEL_TASK_ID | Oui | - |
| `texture` | Ignoré : ce nœud génère toujours des textures. Conservé pour les anciens workflows. (par défaut : True) | BOOLEAN | Non | true<br>false |
| `pbr` | Cartes de matériaux PBR (couleur de base, métallique, rugosité, normale) ; désactivé, donne une texture de couleur unie. (par défaut : True) | BOOLEAN | Non | true<br>false |
| `texture_graine` | Graine aléatoire (seed) pour la génération de textures. Utiliser la même graine avec les mêmes entrées produit le même résultat. (par défaut : 42) | INT | Non | 0 – 2147483647 |
| `qualité_texture` | Qualité de résolution des textures : detailed = textures HD, extreme = textures 8K Ultra. (par défaut : « standard »). Coût approximatif : standard $0.10, detailed $0.20, extreme $0.30. | COMBO | Non | "standard"<br>"detailed"<br>"extreme" |
| `alignement_texture` | Méthode utilisée pour aligner les textures générées sur le modèle. (par défaut : « original_image »). | COMBO | Non | "original_image"<br>"geometry" |
| `texture_prompt` | Guidage textuel facultatif pour la texturation. En pratique, requis pour les modèles importés (Tripo : Import Model), qui ne comportent pas d’image source permettant d’en déduire les couleurs. Ne peut pas être combiné avec des images de référence. (par défaut : "") | STRING | Non | - |
| `model_version` | Modèle de texturation : v3.0 pour les maillages générés avec v3.x, v2.5 pour les maillages générés avec v2.5. (par défaut : la dernière version v3.0) | COMBO | Non | Plusieurs options disponibles |
| `style_image` | Image de référence pour le style artistique des textures. Utilisée uniquement avec `texture_prompt`. | IMAGE | Non | - |
| `reference` | Images de référence guidant les textures. Ne peut pas être combiné avec `texture_prompt` ou `style_image`. (par défaut : « none ») | DYNAMIC_COMBO | Non | "none"<br>"image"<br>"multiview" |
| `part_names` | Noms des pièces à texturer, séparés par des virgules, issus du nœud Tripo : Segment Model. Si la valeur est vide, toutes les pièces sont texturées. (par défaut : "") | STRING | Non | - |

### Entrées de référence « image »

Ces entrées sont disponibles lorsque `reference` est défini sur `"image"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | Image de référence unique que les textures doivent suivre. | IMAGE | Non | - |

### Entrées de référence « multiview »

Ces entrées sont disponibles lorsque `reference` est défini sur `"multiview"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `image_front` | Vue de face (0°). | IMAGE | Non | - |
| `image_left` | Vue de gauche (90°). | IMAGE | Non | - |
| `image_back` | Vue arrière (180°). | IMAGE | Non | - |
| `image_right` | Vue de droite (270°). | IMAGE | Non | - |

**Remarque :** Les modes de référence `"image"` et `"multiview"` ne peuvent pas être combinés avec un `texture_prompt` non vide ni avec `style_image`. L’entrée `style_image` requiert un `texture_prompt` non vide. Lorsque `texture_prompt` est laissé vide, le modèle source doit déjà posséder sa propre image source (par exemple, les modèles produits par text-to-model, image-to-model, multiview-to-model, ou par une tâche de texturation antérieure). Les modèles qui ne possèdent pas d’image source — comme les modèles importés, segmentés, complétés ou retopologisés — doivent être texturés avec un `texture_prompt` ; les images de référence ne sont acceptées que pour les modèles générés par l’API Tripo elle-même.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `fichier_modèle` | Le fichier de modèle généré (uniquement pour la rétrocompatibilité). | STRING |
| `modèle task_id` | L’ID de la tâche de génération de textures terminée, utilisable comme entrée pour d’autres nœuds Tripo. | MODEL_TASK_ID |
| `GLB` | Le modèle texturé généré au format GLB. Vide lorsque la source est un maillage en quadrilatères ou une importation FBX. | FILE3DGLB |
| `FBX` | Le modèle texturé généré au format FBX. Tripo renvoie un FBX pour les maillages en quadrilatères et les importations FBX ; vide autrement. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/fr.md)

---
**Source fingerprint (SHA-256):** `815c22a9d8f4785ef5219789e0f2eee804776ec7e4752099ec0db0a2b5ad4bb2`
