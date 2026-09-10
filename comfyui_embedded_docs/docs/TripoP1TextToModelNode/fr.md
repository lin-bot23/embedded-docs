# Tripo P1 : Texte vers Modèle

Tripo P1 texte-vers-3D. Ce nœud génère un modèle 3D à partir d'une description textuelle en utilisant l'API Tripo P1. Il est optimisé pour créer des maillages low-poly prêts pour le jeu avec une topologie stable, ce qui le rend adapté aux applications temps réel.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mode de sortie` | Contrôle si le modèle généré contient uniquement la géométrie ou également des textures de couleur/PBR. "Geometry only" renvoie un maillage sans texture. "Textured" ajoute des cartes de couleur/PBR et affiche les options de texture ci-dessous. | DYNAMIC_COMBO | Oui | `"Geometry only"`<br>`"Textured"` |
| `invite` | Description textuelle du modèle 3D à générer. Jusqu'à 1024 caractères. Obligatoire et ne peut pas être vide. | STRING | Oui | Jusqu'à 1024 caractères |
| `invite négative` | Description textuelle de ce que vous ne voulez pas dans le modèle généré. Jusqu'à 255 caractères. Par défaut : non défini. | STRING | Non | Jusqu'à 255 caractères |
| `graine d'image` | Valeur de graine utilisée pour contrôler l'aléatoire. Par défaut : 42. | INT | Non | 0 à 2147483647 |
| `limite de faces` | Nombre cible de faces, 48-20000. -1 laisse Tripo choisir de manière adaptative. Par défaut : -1. | INT | Non | -1 à 20000 |
| `graine du modèle` | Valeur de graine utilisée pour contrôler l'aléatoire. Par défaut : 42. | INT | Non | 0 à 2147483647 |
| `taille automatique` | Met à l'échelle la sortie pour approximer des mètres réels. Par défaut : False. | BOOLEAN | Non | True / False |
| `exporter UV` | Dépliage UV pendant la génération. Désactivez pour des exécutions géométriques seules plus rapides. Par défaut : True. | BOOLEAN | Non | True / False |
| `compresser la géométrie` | Applique la compression de géométrie meshopt (EXT_meshopt_compression). Fichiers plus petits, mais l'aperçu 3D de ComfyUI ne peut pas les afficher ; décompressez avant l'édition. Par défaut : False. | BOOLEAN | Non | True / False |

### Entrées Geometry only

Aucune entrée supplémentaire n'est disponible lorsque `output_mode` est défini sur `"Geometry only"`. Les paramètres liés aux textures ne sont pas envoyés à Tripo dans ce mode.

### Entrées Textured

Ces entrées n'apparaissent que lorsque `output_mode` est défini sur `"Textured"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `pbr` | Inclut les cartes PBR. Lorsque cette option est activée, la texture de base est également forcée. Par défaut : True. | BOOLEAN | Oui | True / False |
| `texture_quality` | Préréglage de qualité de texture. detailed = textures HD, extreme = textures 8K Ultra. Par défaut : "standard". | COMBO | Oui | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Valeur de graine pour la génération de texture, utilisée pour contrôler l'aléatoire. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `fichier modèle` | Nom du fichier du modèle généré, conservé uniquement pour la compatibilité ascendante. | STRING |
| `ID de tâche modèle` | ID de tâche unique pour la requête de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `53a5573384294612b912558436e82f3481717d2ba3d50b73f1e40c3065aff2a0`
