# Aperçu Splat

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `modèle_3d` | Un fichier de splat gaussien 3D. | FILE3D | Oui | splat<br>ply<br>spz<br>ksplat |
| `info_modèle_3d` | Informations de métadonnées optionnelles sur le modèle 3D. Lorsqu'il n'est pas connecté, le nœud utilise les informations du modèle provenant de `viewport_state`. | LOAD3DMODELINFO | Non | - |
| `état_vue` | L'état actuel de la fenêtre d'affichage 3D, incluant les informations de caméra et de modèle. | LOAD3D | Oui | - |
| `info_caméra` | Informations de caméra optionnelles pour l'aperçu. Lorsqu'il n'est pas connecté, le nœud utilise les informations de caméra de `viewport_state`. | LOAD3DCAMERA | Non | - |
| `largeur` | La largeur du rendu d'aperçu en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |
| `hauteur` | La hauteur du rendu d'aperçu en pixels (par défaut : 1024). | INT | Oui | 1 à 4096 |

Remarque : lorsque `camera_info` ou `model_3d_info` ne sont pas fournis, le nœud utilise les informations de caméra et de modèle stockées dans `viewport_state`.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `modèle_3d` | Le fichier de splat gaussien 3D d'entrée, transmis tel quel. | FILE3D |
| `info_modèle_3d` | Informations de métadonnées sur le modèle 3D, soit à partir de l'entrée, soit dérivées de l'état de la fenêtre d'affichage. | LOAD3DMODELINFO |
| `info_caméra` | Informations de caméra pour l'aperçu, soit à partir de l'entrée, soit dérivées de l'état de la fenêtre d'affichage. | LOAD3DCAMERA |
| `largeur` | La largeur du rendu d'aperçu. | INT |
| `hauteur` | La hauteur du rendu d'aperçu. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/fr.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`
