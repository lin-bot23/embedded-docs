# Tripo : Image vers Modèle

Génère des modèles 3D de manière synchrone à partir d'une seule image via l'API de Tripo. Fournissez une image d'entrée et le nœud crée un modèle 3D fini à partir de celle-ci, avec des contrôles facultatifs pour la version du modèle, la génération de textures, le niveau de détail et le format de sortie.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `image` | L'image d'entrée utilisée pour générer le modèle 3D. Une image doit être fournie, sinon le nœud lève une erreur. | IMAGE | Oui | - |
| `version_modèle` | La version du modèle à utiliser pour la génération. | COMBO | Non | `"v1.4"`<br>`"v3.0"`<br>`"v3.5"`<br>`"v3.6"` |
| `style` | N'est plus pris en charge par Tripo et est ignoré. Conservé pour les anciens workflows. (défaut : `"None"`) | COMBO | Non | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `texture` | Génère les cartes de texture. Désactivé renvoie une géométrie nue et ignore `pbr`. (défaut : True) | BOOLEAN | Non | True<br>False |
| `pbr` | Cartes de matériaux PBR (couleur de base, métallique, rugosité, normale). Nécessite `texture`. (défaut : True) | BOOLEAN | Non | True<br>False |
| `graine_modèle` | Graine aléatoire pour la génération du modèle. (défaut : 42) | INT | Non | 0 à 2147483647 |
| `orientation` | Paramètre d'orientation du modèle généré. (défaut : `"default"`) | COMBO | Non | `"default"`<br>`"front"`<br>`"back"`<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `graine_texture` | Graine aléatoire pour la génération de la texture. (défaut : 42) | INT | Non | 0 à 2147483647 |
| `qualité_texture` | Qualité de la génération de textures : `detailed` = textures HD, `extreme` = textures Ultra 8K. (défaut : `"standard"`) | COMBO | Non | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `alignement_texture` | Méthode d'alignement pour le mappage de texture. (défaut : `"original_image"`) | COMBO | Non | `"original_image"`<br>`"geometry"` |
| `limite_faces` | Nombre maximal de faces. -1 permet à Tripo de choisir de manière adaptative (environ 1,4 M de faces sur la version standard v3.x, 2 M sur `detailed`). Tripo limite silencieusement : v2.5 à 500 000, les maillages quad à 150 000. (défaut : -1) | INT | Non | -1 à 2000000 |
| `quad` | Sortie en maillage quad. Tripo fournit les maillages quad en FBX, donc le résultat arrive sur la sortie FBX et la sortie GLB reste vide. (défaut : False) | BOOLEAN | Non | True<br>False |
| `geometry_quality` | Niveau de qualité pour la génération de la géométrie. (défaut : `"standard"`) | COMBO | Non | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Maillage low-poly avec une topologie propre, de style artisanal (500 à 20 000 faces, quad 500 à 10 000). Idéal pour les sujets simples ; les sujets complexes peuvent échouer. (défaut : False) | BOOLEAN | Non | True<br>False |
| `auto_size` | Mesure les modèles texturés à leur taille réelle en mètres. Tripo stocke la taille comme transformation de scène du modèle et l'intègre lorsque le modèle est converti, riggé ou retargeté ; ignoré sans texture. (défaut : True) | BOOLEAN | Non | True<br>False |

Remarque : une `image` est obligatoire ; si elle manque, le nœud lève une RuntimeError. Lorsque `texture` est False, le modèle ne contient que la géométrie nue et `pbr` est forcé à False. Lorsque `smart_low_poly` est activé, `face_limit` doit être compris entre 500 et 20 000 pour les maillages triangulaires, ou entre 500 et 10 000 lorsque `quad` est également activé ; si la limite est invalide, le nœud lève une ValueError. Définir `face_limit` à -1 (la valeur par défaut) n'envoie aucune limite explicite de faces à l'API, ce qui laisse Tripo choisir de manière adaptative.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `fichier_modèle` | Le fichier de modèle 3D généré (uniquement pour la rétrocompatibilité). | STRING |
| `modèle task_id` | L'ID de tâche permettant de suivre le processus de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. Vide lorsque `quad` est activé. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. Rempli uniquement lorsque `quad` est activé. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `79ebe76234036e8284640d7eaeee3a1220975b8adc043994de7de0ee161ccd45`
