# Tripo : Texte vers Modèle

Génère des modèles 3D finis à partir d’une description textuelle à l’aide de l’API Tripo. Le nœud attend la fin de la génération, puis renvoie le fichier du modèle, éventuellement avec des textures et des matériaux PBR.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description textuelle du modèle 3D à générer (multiligne). Ce paramètre est requis et ne peut pas être vide. | STRING | Oui | - |
| `negative_prompt` | Description textuelle de ce qu’il faut éviter dans le modèle généré (multiligne). Jusqu’à 255 caractères. Envoyé à l’API uniquement s’il n’est pas vide. | STRING | Non | Jusqu’à 255 caractères |
| `model_version` | Version du modèle Tripo à utiliser pour la génération (défaut : v3.1-20260211). | COMBO | Non | Plusieurs options disponibles |
| `style` | Style appliqué au modèle généré (défaut : None). N’est plus pris en charge par Tripo et est ignoré ; conservé pour les anciens workflows. | COMBO | Non | Plusieurs options disponibles |
| `texture` | Indique s’il faut générer des cartes de textures. Désactivé renvoie une géométrie nue et ignore `pbr` (défaut : True). | BOOLEAN | Non | true / false |
| `pbr` | Indique s’il faut générer des cartes de matériaux PBR (couleur de base, métallique, rugosité, normale). Nécessite `texture` ; forcé à off lorsque `texture` est off (défaut : True). | BOOLEAN | Non | true / false |
| `image_seed` | Graine utilisée pour l’étape de génération d’image (défaut : 42). | INT | Non | 0 à 2147483647 |
| `model_seed` | Graine utilisée pour l’étape de génération du modèle (défaut : 42). | INT | Non | 0 à 2147483647 |
| `texture_seed` | Graine utilisée pour l’étape de génération des textures (défaut : 42). | INT | Non | 0 à 2147483647 |
| `texture_quality` | Qualité des textures générées. detailed = textures HD, extreme = textures 8K Ultra (défaut : standard). | COMBO | Non | "standard"<br>"detailed"<br>"extreme" |
| `face_limit` | Nombre maximal de faces. -1 laisse Tripo choisir de manière adaptative (environ 1,4 M de faces sur v3.x standard, 2 M sur detailed). Tripo limite silencieusement : v2.5 à 500 000, les maillages quad à 150 000. (défaut : -1) | INT | Non | -1 à 2000000 |
| `quad` | Sortie de maillage quad. Tripo fournit les maillages quad en FBX, donc le résultat arrive sur la sortie FBX et la sortie GLB reste vide. (défaut : False) | BOOLEAN | Non | true / false |
| `geometry_quality` | Qualité de la géométrie générée (défaut : standard). | COMBO | Non | "standard"<br>"detailed" |
| `smart_low_poly` | Maillage low-poly avec une topologie propre, de style artisanal (500 à 20 000 faces, quad 500 à 10 000). Idéal pour les sujets simples ; les sujets complexes peuvent échouer. (défaut : False) | BOOLEAN | Non | true / false |
| `auto_size` | Met à l’échelle les modèles texturés selon leur taille réelle en mètres. Tripo stocke la taille comme transformation de scène du modèle et l’intègre lors de la conversion, du montage (rigging) ou du retargeting du modèle ; ignoré sans texture. (défaut : True) | BOOLEAN | Non | true / false |

**Remarques :**
- Le paramètre `prompt` est obligatoire : une invite vide provoque une erreur du nœud.
- `pbr` nécessite `texture`. Lorsque `texture` est off, le nœud force `pbr` à off et ignore sa valeur. `auto_size` n’a également aucun effet sans `texture`.
- Lorsque `smart_low_poly` est activé et que `face_limit` est défini sur une valeur autre que -1, la limite de faces doit être comprise entre 500 et 20 000 pour une sortie en triangles, ou entre 500 et 10 000 lorsque `quad` est activé ; sinon le nœud génère une erreur.
- Lorsque `quad` est activé, le maillage quad généré est fourni en FBX, donc la sortie FBX est remplie et la sortie GLB reste vide.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------------|
| `model_file` | Le fichier de modèle 3D généré, conservé uniquement pour la compatibilité ascendante. | STRING |
| `model task_id` | L’identifiant unique de la tâche pour le processus de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. Vide lorsque `quad` est activé. | FILE3DGLB |
| `FBX` | Le modèle 3D généré au format FBX. Uniquement rempli lorsque `quad` est activé. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `3f4bc09d125fedb6c30968f31804cfc7ec6d2f068a7c28d90b006137803020b0`
