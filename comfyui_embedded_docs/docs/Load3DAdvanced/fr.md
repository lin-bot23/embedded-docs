# Charger 3D (Avancé)

Le nœud « Load 3D (Advanced) » charge un fichier de modèle 3D depuis le répertoire `input/3d` de ComfyUI et fournit les données du modèle ainsi que les informations de placement du modèle et de caméra capturées dans l’état de la fenêtre d’affichage du visualiseur 3D. Il prend en charge les formats de fichiers 3D courants et vous permet de définir la largeur et la hauteur de rendu de la fenêtre en pixels. Ce nœud est expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_file` | Le fichier de modèle 3D à charger. Sélectionnez « none » pour ignorer le chargement d’un fichier de modèle. | COMBO | Oui | `"none"`<br>Fichiers de modèles 3D disponibles dans le répertoire `input/3d` |
| `viewport_state` | L’état actuel de la fenêtre d’affichage contenant les informations de caméra et de modèle du visualiseur 3D. | LOAD3D | Oui | - |
| `width` | Largeur de rendu de la fenêtre en pixels (défaut : 1024). | INT | Oui | Min : 1<br>Max : 4096<br>Défaut : 1024<br>Pas : 1 |
| `height` | Hauteur de rendu de la fenêtre en pixels (défaut : 1024). | INT | Oui | Min : 1<br>Max : 4096<br>Défaut : 1024<br>Pas : 1 |

**Remarques sur les paramètres :**
- Le paramètre `model_file` ne répertorie que les fichiers portant les extensions suivantes : .gltf, .glb, .obj, .fbx, .stl
- Les fichiers doivent être placés dans le répertoire `input/3d` de votre installation ComfyUI ; les sous-dossiers sont également recherchés et les chemins de fichiers sont affichés de manière relative au répertoire d’entrée.
- Si `model_file` est défini sur « none », aucune donnée de modèle n’est chargée et la sortie `model_3d` sera vide.
- Si `model_file` est défini sur un fichier qui n’existe pas, le nœud renvoie une erreur de validation : « Invalid 3D model file: {model_file} »

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Fichier de modèle 3D chargé (glb/obj/stl/etc.). Vide si aucun fichier de modèle n’a été sélectionné. | FILE3DANY |
| `model_3d_info` | Placement de chaque modèle dans la scène : position, rotation et échelle (espace monde Y vers le haut). | LOAD3DMODELINFO |
| `camera_info` | Informations de la caméra de la fenêtre d’affichage : position, point cible (look-at), zoom et type. | LOAD3DCAMERA |
| `width` | Largeur de rendu de la fenêtre en pixels. | INT |
| `height` | Hauteur de rendu de la fenêtre en pixels. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `c79c53dde0c8b3afb7df7b972df749f5040c92d48b47e355c4497d9b0cbf1c22`
