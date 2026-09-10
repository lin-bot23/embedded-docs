# Enregistrer 3D (Avancé)

Save3DAdvanced enregistre un modèle 3D dans un fichier du répertoire de sortie de ComfyUI et crée un aperçu de la scène enregistrée. Il transmet également le modèle 3D, son placement dans la scène, les informations de caméra et les dimensions de la fenêtre d’affichage aux nœuds en aval. Lorsque le placement du modèle ou les informations de caméra ne sont pas connectés, le nœud utilise les valeurs stockées dans l’état de la fenêtre d’affichage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Fichier de modèle 3D provenant d’un nœud 3D en amont. | FILE3D | Oui | GLB<br>GLTF<br>FBX<br>OBJ<br>STL<br>USDZ<br>Any |
| `filename_prefix` | Préfixe utilisé pour le nom du fichier enregistré (par défaut : « 3d/ComfyUI »). | STRING | Oui | Free text |
| `viewport_state` | État de la fenêtre d’affichage contenant les informations de caméra et de placement du modèle, généralement issu d’un nœud Load 3D. | LOAD3D | Oui | - |
| `model_3d_info` | Placement de chaque modèle dans la scène : position, rotation et échelle (espace monde, Y vers le haut). Remplace le placement du modèle stocké dans `viewport_state` lorsqu’il est connecté. | LOAD3DMODELINFO | Non | - |
| `camera_info` | Informations de caméra de la fenêtre d’affichage : position, point visé, zoom et type. Remplace les informations de caméra stockées dans `viewport_state` lorsqu’il est connecté. | LOAD3DCAMERA | Non | - |
| `width` | Largeur de rendu de la fenêtre d’affichage en pixels (par défaut : 1024). | INT | Oui | 1 to 4096 |
| `height` | Hauteur de rendu de la fenêtre d’affichage en pixels (par défaut : 1024). | INT | Oui | 1 to 4096 |

Remarque : `model_3d_info` et `camera_info` sont facultatifs. Lorsque l’une de ces entrées n’est pas connectée, le nœud utilise par défaut les valeurs correspondantes stockées dans `viewport_state`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Le fichier de modèle 3D transmis depuis l’entrée. | FILE3D |
| `model_3d_info` | Placement de chaque modèle dans la scène : position, rotation et échelle (espace monde, Y vers le haut). | LOAD3DMODELINFO |
| `camera_info` | Informations de caméra de la fenêtre d’affichage : position, point visé, zoom et type. | LOAD3DCAMERA |
| `width` | La valeur de largeur de rendu transmise depuis l’entrée. | INT |
| `height` | La valeur de hauteur de rendu transmise depuis l’entrée. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`
