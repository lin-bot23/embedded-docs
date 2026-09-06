# Aperçu Nuage de Points

Le nœud Preview Point Cloud vous permet de visualiser un fichier de nuage de points 3D dans l’interface ComfyUI sans l’enregistrer dans le répertoire de sortie de ComfyUI. Il enregistre le nuage de points dans un emplacement temporaire et l’affiche dans une fenêtre d’aperçu 3D, tout en transmettant les données du modèle, les informations sur le modèle, les informations de caméra et les dimensions de l’aperçu pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de nuage de points (.ply) | FILE3D | Oui | - |
| `model_3d_info` | Informations sur le modèle 3D | LOAD3DMODELINFO | Non | - |
| `viewport_state` | État actuel de la fenêtre 3D | LOAD3D | Oui | - |
| `camera_info` | Informations de caméra pour la vue 3D | LOAD3DCAMERA | Non | - |
| `width` | Largeur de la fenêtre d’aperçu (défaut : 1024) | INT | Oui | 1 à 4096 |
| `height` | Hauteur de la fenêtre d’aperçu (défaut : 1024) | INT | Oui | 1 à 4096 |

Remarque : `model_3d_info` et `camera_info` sont des entrées avancées facultatives. Lorsqu’elles ne sont pas connectées, le nœud utilise les valeurs correspondantes stockées dans `viewport_state`. Le fichier de nuage de points est écrit dans le répertoire temporaire de ComfyUI plutôt que dans le répertoire de sortie. Ce nœud est un nœud de sortie (terminal), il est donc principalement utilisé pour afficher l’aperçu dans l’interface.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Les données du modèle de nuage de points | FILE3D |
| `model_3d_info` | Informations sur le modèle 3D | LOAD3DMODELINFO |
| `camera_info` | Informations de caméra pour la vue 3D | LOAD3DCAMERA |
| `width` | Largeur de la fenêtre d’aperçu | INT |
| `height` | Hauteur de la fenêtre d’aperçu | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/fr.md)

---
**Source fingerprint (SHA-256):** `a0b13d9d5658343a6a7c25408d5e5cd9249c92264b76aa448a6553b370f4d782`
