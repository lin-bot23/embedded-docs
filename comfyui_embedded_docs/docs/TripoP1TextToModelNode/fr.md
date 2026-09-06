# Tripo P1 : Texte vers Modèle

Ce nœud génère un modèle 3D à partir d’une description textuelle via l’API Tripo P1. Il est optimisé pour créer des maillages low-poly prêts pour le jeu avec une topologie stable, ce qui le rend adapté aux applications temps réel.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `output_mode` | Contrôle si le modèle généré contient uniquement la géométrie ou également des textures couleur/PBR. La sélection de « Textured » ajoute des entrées de texture ci-dessous. « Geometry only » renvoie un maillage non texturé ; « Textured » ajoute des cartes couleur/PBR. | DYNAMIC_COMBO | Oui | `"Geometry only"`<br>`"Textured"` |
| `prompt` | La description textuelle du modèle 3D que vous souhaitez générer. Jusqu’à 1024 caractères. | STRING | Oui | Jusqu’à 1024 caractères |
| `negative_prompt` | Une description textuelle de ce que vous ne voulez pas voir dans le modèle généré. Jusqu’à 255 caractères. | STRING | Non | Jusqu’à 255 caractères |
| `image_seed` | Une valeur de graine pour la génération d’images, utilisée pour contrôler le caractère aléatoire. Défaut : 42. | INT | Non | 0 à 2147483647 |
| `face_limit` | Nombre de faces cible, 48-20000. Une valeur de -1 laisse Tripo choisir de manière adaptative. Défaut : -1. | INT | Non | -1 à 20000 |
| `model_seed` | Une valeur de graine pour la génération du modèle, utilisée pour contrôler le caractère aléatoire. Défaut : 42. | INT | Non | 0 à 2147483647 |
| `auto_size` | Met à l’échelle la sortie pour se rapprocher des mètres du monde réel. Défaut : False. | BOOLEAN | Non | True / False |
| `export_uv` | Dépliage UV pendant la génération. Désactivez pour des exécutions géométrie seule plus rapides. Défaut : True. | BOOLEAN | Non | True / False |
| `compress_geometry` | Applique la compression de géométrie meshopt (EXT_meshopt_compression). Fichiers plus petits, mais l’aperçu 3D de ComfyUI ne peut pas les afficher ; décompressez avant de modifier. Défaut : False. | BOOLEAN | Non | True / False |

### Entrées « Geometry only »

Aucune entrée supplémentaire n’est disponible lorsque `output_mode` est défini sur `"Geometry only"`. Les paramètres liés aux textures ne sont pas envoyés à Tripo dans ce mode.

### Entrées « Textured »

Ces entrées n’apparaissent que lorsque `output_mode` est défini sur `"Textured"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `pbr` | Inclut les cartes PBR. Lorsqu’elle est activée, la texture de base est également forcée. Défaut : True. | BOOLEAN | Oui | True / False |
| `texture_quality` | Préréglage de qualité de texture. detailed = textures HD, extreme = textures Ultra 8K. Défaut : « standard ». | COMBO | Oui | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Une valeur de graine pour la génération de textures, utilisée pour contrôler le caractère aléatoire. Défaut : 42. | INT | Oui | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Le chemin d’accès au fichier du modèle 3D généré, conservé uniquement pour la compatibilité ascendante. | STRING |
| `model task_id` | L’identifiant unique de la tâche pour la demande de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `63781a990f892e6b1f241179039d1fb24778ba7aa7dccda7d14557cbf190b712`
