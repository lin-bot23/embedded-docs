# Aperçu 3D (Avancé)

Ce nœud affiche un aperçu du modèle 3D dans l’interface sans enregistrer le fichier dans le répertoire de sortie de ComfyUI. Il enregistre le modèle dans un fichier temporaire et transmet les données du modèle, les informations du modèle, les informations de caméra et les dimensions d’aperçu pour un traitement ultérieur en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `modèle 3D` | Fichier de modèle 3D provenant d’un nœud 3D en amont. | FILE3D | Oui | GLB, GLTF, FBX, OBJ, STL, USDZ, ou tout format 3D pris en charge |
| `infos_modèle_3d` | Placement de chaque modèle dans la scène : position, rotation et échelle (espace monde avec Y vers le haut). Facultatif. Option avancée. | LOAD3DMODELINFO | Non | - |
| `état de la vue` | État actuel de la fenêtre d’affichage contenant les informations de caméra et de modèle. | LOAD3D | Oui | - |
| `infos_caméra` | Informations de caméra de la fenêtre d’affichage : position, cible du regard, zoom et type. Facultatif. Option avancée. | LOAD3DCAMERA | Non | - |
| `largeur` | Largeur de rendu de la fenêtre d’affichage en pixels. Par défaut : 1024. | INT | Oui | 1 à 4096 |
| `hauteur` | Hauteur de rendu de la fenêtre d’affichage en pixels. Par défaut : 1024. | INT | Oui | 1 à 4096 |

Remarque : lorsque `camera_info` ou `model_3d_info` ne sont pas connectés, leurs valeurs sont reprises depuis `viewport_state` lorsqu’elles sont disponibles. Si `viewport_state` ne contient aucune information de caméra, `camera_info` est None. Si `viewport_state` ne contient aucune information de modèle, `model_3d_info` prend par défaut une liste vide. Si `viewport_state` n’est pas un dictionnaire, il est traité comme vide.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `fichier_modèle` | Fichier de modèle 3D (glb/obj/stl/etc.) provenant d’un nœud 3D en amont, transmis tel quel. | FILE3D |
| `infos_caméra` | Placement de chaque modèle dans la scène : position, rotation et échelle (espace monde avec Y vers le haut). Utilise la valeur d’entrée ou, à défaut, la valeur stockée dans `viewport_state`. | LOAD3DMODELINFO |
| `infos_modèle_3d` | Informations de caméra de la fenêtre d’affichage : position, cible du regard, zoom et type. Utilise la valeur d’entrée ou, à défaut, la valeur stockée dans `viewport_state`. | LOAD3DCAMERA |
| `largeur` | Largeur de rendu de la fenêtre d’affichage en pixels. | INT |
| `hauteur` | Hauteur de rendu de la fenêtre d’affichage en pixels. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `f2d3d35ed35fe68edebcde8fd8421d26850b04e3ae5b7147f1020c8ed904c480`
