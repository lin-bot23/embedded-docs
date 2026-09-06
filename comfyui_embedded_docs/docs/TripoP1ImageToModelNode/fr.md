# Tripo P1 : Image vers Modèle

Tripo P1: Image to Model convertit une seule image 2D en un modèle 3D à l’aide de l’API Tripo P1. Il est optimisé pour générer des maillages à faible nombre de polygones, prêts pour le jeu, et vous permet de choisir entre un maillage en mode géométrie seule ou un modèle texturé avec des cartes PBR. Le modèle final est renvoyé sous forme de fichier GLB.

## Entrées

### Entrées communes

Ces paramètres sont toujours disponibles.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|----------------|--------|-------|
| `output_mode` | Choisit le type de résultat. « Geometry only » renvoie un maillage non texturé ; « Textured » ajoute de la couleur et des cartes PBR et révèle des paramètres de texture supplémentaires. | DYNAMIC_COMBO | Oui | `"Geometry only"`<br>`"Textured"` |
| `image` | L’image 2D source utilisée pour générer le modèle 3D. Le nœud requiert une seule image et lève une erreur si aucune n’est fournie. | IMAGE | Oui | - |
| `enable_image_autofix` | Prétraite l’image d’entrée pour améliorer la qualité de génération. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `face_limit` | Nombre de faces cible, 48-20000. -1 laisse Tripo choisir de manière adaptative. (par défaut : -1) | INT | Non | -1 à 20000 |
| `model_seed` | Graine utilisée pour la génération de la géométrie afin que les résultats soient reproductibles. (par défaut : 42) | INT | Non | 0 à 2147483647 |
| `auto_size` | Met à l’échelle le résultat pour se rapprocher des dimensions réelles en mètres. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `export_uv` | Dépliage UV pendant la génération. Désactivez cette option pour des exécutions plus rapides en mode géométrie seule. (par défaut : True) | BOOLEAN | Non | True<br>False |
| `compress_geometry` | Applique la compression de géométrie meshopt (EXT_meshopt_compression). Fichiers plus petits, mais l’aperçu 3D de ComfyUI ne peut pas les afficher ; décompressez-les avant de les modifier. (par défaut : False) | BOOLEAN | Non | True<br>False |

### Entrées texturées

Ces paramètres apparaissent lorsque `output_mode` est défini sur « Textured ». Le mode « Geometry only » n’a aucun paramètre supplémentaire.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|----------------|--------|-------|
| `pbr` | Inclut les cartes PBR. Quand cette option est activée, la texture de base est également forcée. (par défaut : True) | BOOLEAN | Non | True<br>False |
| `texture_quality` | Niveau de résolution de texture. « detailed » = textures HD, « extreme » = textures 8K Ultra. (par défaut : « standard ») | COMBO | Non | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Privilégie la fidélité visuelle à l’image source ou l’alignement avec la géométrie du maillage. (par défaut : « original_image ») | COMBO | Non | `"original_image"`<br>`"geometry"` |
| `orientation` | Fait pivoter le résultat pour l’aligner sur l’image source. Ne s’applique que si le résultat est texturé. (par défaut : « default ») | COMBO | Non | `"default"`<br>`"align_image"` |
| `texture_seed` | Graine utilisée pour la génération de la texture afin que les résultats texturés soient reproductibles. (par défaut : 42) | INT | Non | 0 à 2147483647 |

Remarque : lorsque `output_mode` est défini sur « Geometry only », la texturation est désactivée pour la requête. En mode « Textured », une texture en couleur est toujours demandée ; désactiver `pbr` supprime les cartes PBR mais conserve la texture de base en couleur, tandis que l’activer force également l’activation de la texture de base.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Le résultat du modèle 3D généré. Conservé uniquement pour la rétrocompatibilité. | STRING |
| `model task_id` | L’identifiant unique de tâche renvoyé par l’API Tripo pour la tâche de génération terminée. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `db5dc76518a4efcd28d388dc00ad0810f619481482f20fa456c4ff2478192aa3`
