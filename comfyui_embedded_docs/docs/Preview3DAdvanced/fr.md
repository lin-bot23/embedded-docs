# Aperçu 3D (Avancé)

Ce nœud affiche un aperçu d’un modèle 3D dans l’interface sans enregistrer le fichier dans le répertoire de sortie de ComfyUI. Il enregistre le modèle dans un fichier temporaire et transmet les données du modèle, les informations du modèle, les informations de caméra et les dimensions de l’aperçu pour un traitement ultérieur en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle 3D` | Fichier de modèle 3D provenant d’un nœud 3D en amont. | FILE3D | Oui | GLB, GLTF, FBX, OBJ, STL, USDZ, ou tout format 3D pris en charge |
| `infos_modèle_3d` | Métadonnées optionnelles d’informations sur le modèle. Option avancée. | LOAD3DMODELINFO | Non | - |
| `état de la vue` | État actuel de la fenêtre d’affichage contenant les informations de caméra et de modèle. | LOAD3D | Oui | - |
| `infos_caméra` | Configuration optionnelle de la caméra pour la vue 3D. Option avancée. | LOAD3DCAMERA | Non | - |
| `largeur` | Largeur de l’aperçu en pixels. Par défaut : 1024. | INT | Oui | 1 à 4096 |
| `hauteur` | Hauteur de l’aperçu en pixels. Par défaut : 1024. | INT | Oui | 1 à 4096 |

Remarque : Lorsque `camera_info` ou `model_3d_info` ne sont pas connectés, leurs valeurs sont extraites de `viewport_state` lorsqu’elles sont disponibles. Si `viewport_state` ne contient aucune information de caméra, `camera_info` est None. Si `viewport_state` ne contient aucune information de modèle, `model_3d_info` est défini par défaut sur une liste vide. Si `viewport_state` n’est pas un dictionnaire, il est traité comme vide.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `fichier_modèle` | Le fichier de modèle 3D transmis depuis l’entrée. | FILE3D |
| `infos_caméra` | Métadonnées d’informations sur le modèle, provenant de l’entrée ou de l’état de la fenêtre d’affichage. | LOAD3DMODELINFO |
| `infos_modèle_3d` | Configuration de la caméra, provenant de l’entrée ou de l’état de la fenêtre d’affichage. | LOAD3DCAMERA |
| `largeur` | Largeur de l’aperçu en pixels. | INT |
| `hauteur` | Hauteur de l’aperçu en pixels. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `46c14d6242cbcabd457e13ae193427bb4c1fed55e81e568d50719fff0f1a95a0`
