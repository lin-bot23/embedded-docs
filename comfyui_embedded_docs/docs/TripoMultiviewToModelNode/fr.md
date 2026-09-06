# Tripo : Multivue vers Modèle

Ce nœud génère des modèles 3D de manière synchrone via l’API de Tripo en traitant jusqu’à quatre images montrant différentes vues d’un objet (face avant, gauche, arrière, droite). Il nécessite une image de face et au moins une vue supplémentaire (gauche, arrière ou droite) pour construire le modèle 3D. La texture, le matériau PBR, la qualité de la géométrie et le format de sortie peuvent être contrôlés depuis le nœud.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `image` | Image de la vue de face de l’objet. | IMAGE | Oui | - |
| `image_left` | Image de la vue de gauche de l’objet. | IMAGE | Non | - |
| `image_back` | Image de la vue arrière de l’objet. | IMAGE | Non | - |
| `image_right` | Image de la vue de droite de l’objet. | IMAGE | Non | - |
| `model_version` | Version du modèle à utiliser pour la génération. | COMBO | Non | Plusieurs options disponibles |
| `orientation` | Réglage d’orientation du modèle 3D (par défaut : `"default"`). | COMBO | Non | Plusieurs options disponibles |
| `texture` | Génère les cartes de texture. Désactivé renvoie une géométrie brute et ignore pbr. (par défaut : True) | BOOLEAN | Non | - |
| `pbr` | Cartes de matériaux PBR (couleur de base, métallique, rugosité, normale). Nécessite la texture. (par défaut : True) | BOOLEAN | Non | - |
| `model_seed` | Graine aléatoire pour la génération du modèle (par défaut : 42). | INT | Non | 0 à 2 147 483 647 |
| `texture_seed` | Graine aléatoire pour la génération de la texture (par défaut : 42). | INT | Non | 0 à 2 147 483 647 |
| `texture_quality` | Niveau de qualité pour la génération de texture (par défaut : `"standard"`). `"detailed"` = textures HD, `"extreme"` = textures 8K Ultra. | COMBO | Non | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Méthode utilisée pour aligner les textures sur le modèle (par défaut : `"original_image"`). | COMBO | Non | `"original_image"`<br>`"geometry"` |
| `face_limit` | Nombre maximal de faces. -1 laisse Tripo choisir de manière adaptative (environ 1,4 million de faces en standard v3.x, 2 millions en détaillé). Tripo plafonne silencieusement : v2.5 à 500 000, maillages quad à 150 000. (par défaut : -1) | INT | Non | -1 à 2 000 000 |
| `quad` | Sortie de maillage quad. Tripo fournit les maillages quad en FBX, donc le résultat arrive sur la sortie FBX et la sortie GLB reste vide. (par défaut : False) | BOOLEAN | Non | - |
| `geometry_quality` | Niveau de qualité pour la génération de la géométrie (par défaut : `"standard"`). | COMBO | Non | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Maillage low-poly avec une topologie propre de style artisanal (500 à 20 000 faces, 500 à 10 000 pour les quad). Idéal pour les sujets simples ; les sujets complexes peuvent échouer. (par défaut : False) | BOOLEAN | Non | - |
| `auto_size` | Met à l’échelle les modèles texturés à leur taille réelle en mètres. Tripo stocke la taille comme transformation de scène du modèle et l’intègre lors de la conversion, de l’armature ou du retargeting ; ignoré sans texture. (par défaut : False) | BOOLEAN | Non | - |

**Remarque :** L’image de face (`image`) est toujours requise, et au moins une des images `image_left`, `image_back` ou `image_right` doit également être fournie. Désactiver `texture` désactive automatiquement `pbr`, car `pbr` nécessite la texture. Lorsque `smart_low_poly` est activé et que `face_limit` n’est pas laissé à -1, `face_limit` doit être compris entre 500 et 20 000 pour les maillages triangulaires ou entre 500 et 10 000 pour les maillages quad.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `model_file` | Chemin du fichier ou identifiant du modèle 3D généré (pour compatibilité ascendante uniquement). | STRING |
| `model task_id` | Identifiant de tâche pour suivre le processus de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Fichier du modèle 3D généré au format GLB. Vide lorsque `quad` est activé. | FILE3DGLB |
| `FBX` | Fichier du modèle 3D généré au format FBX. Uniquement rempli lorsque `quad` est activé. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `73f1259dcba75ce1d56aabb6f0435f11d21eee3268f93502c4c3293d562a6db0`
