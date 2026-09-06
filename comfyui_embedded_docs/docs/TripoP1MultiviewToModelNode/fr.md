# Tripo P1 : Multivues vers Modèle

Ce nœud génère un modèle 3D à partir de deux à quatre images de référence d’un objet ou d’un personnage. Fournissez la vue de face ainsi qu’une combinaison quelconque des vues gauche, arrière et droite, et le nœud renvoie le sujet reconstruit sous forme de maillage GLB.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Vue de face (0°). Requise. | IMAGE | Oui | - |
| `image_left` | Vue gauche (90°), c’est-à-dire le côté gauche du sujet. | IMAGE | Non | - |
| `image_back` | Vue arrière (180°). | IMAGE | Non | - |
| `image_right` | Vue droite (270°), c’est-à-dire le côté droit du sujet. | IMAGE | Non | - |
| `output_mode` | Choisissez le type de modèle à générer. « Geometry only » renvoie un maillage sans texture. « Textured » ajoute des cartes de couleur/PBR. | DYNAMIC_COMBO | Oui | "Geometry only"<br>"Textured" |
| `face_limit` | Nombre de faces cible, de 48 à 20 000. -1 laisse Tripo choisir de manière adaptative. (défaut : -1) | INT | Non | -1 à 20000 |
| `model_seed` | Graine pour la génération reproductible du modèle. (défaut : 42) | INT | Non | 0 à 2147483647 |
| `auto_size` | Met la sortie à l’échelle pour approximer des mètres réels. (défaut : False) | BOOLEAN | Non | True<br>False |
| `export_uv` | Dépliage UV pendant la génération. Désactivez-le pour des exécutions géométrie seule plus rapides. (défaut : True) | BOOLEAN | Non | True<br>False |
| `compress_geometry` | Applique la compression de géométrie meshopt (EXT_meshopt_compression). Fichiers plus petits, mais l’aperçu 3D de ComfyUI ne peut pas les afficher ; décompressez-les avant de les modifier. (défaut : False) | BOOLEAN | Non | True<br>False |

### Entrées Geometry only

Aucune entrée supplémentaire n’est affichée pour ce mode. Le modèle généré est renvoyé sans texture.

### Entrées Textured

Ces entrées apparaissent lorsque `output_mode` est défini sur `"Textured"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `pbr` | Inclure les cartes PBR. Lorsque cette option est activée, la texture de base est également forcée. (défaut : True) | BOOLEAN | Oui | True<br>False |
| `texture_quality` | Niveau de qualité de la texture. `detailed` = textures HD, `extreme` = textures 8K Ultra. (défaut : "standard") | COMBO | Oui | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Privilégier la fidélité visuelle à l’image source, ou l’alignement sur la géométrie du maillage. (défaut : "original_image") | COMBO | Oui | "original_image"<br>"geometry" |
| `orientation` | Faire pivoter la sortie pour correspondre à l’image source. Ne s’applique que lorsque le modèle est texturé. (défaut : "default") | COMBO | Oui | "default"<br>"align_image" |
| `texture_seed` | Graine utilisée pour la génération de la texture. (défaut : 42) | INT | Oui | 0 à 2147483647 |

**Remarque :** Vous devez fournir au moins 2 images : la vue de face (`image`) plus au moins une des autres vues (`image_left`, `image_back` ou `image_right`). Si moins de 2 images sont fournies, le nœud générera une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Le nom de fichier du modèle GLB généré (uniquement pour la rétrocompatibilité). | STRING |
| `model_task_id` | L’identifiant de tâche unique pour cette demande de génération de modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `c26bf9d46f6b95ec57e4eb663cb6c602035c3ad00682e7f9622ce575ff54d228`
