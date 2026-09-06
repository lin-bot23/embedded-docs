# Tripo : Modèle squeletté redirigé

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|----------------|--------|-------|
| `original_model_task_id` | L’identifiant de tâche du modèle 3D préalablement riggé à retargeter. La tâche référencée doit être une tâche de rig ; un rig réalisé avec la spécification Mixamo sur la version de modèle v1.0 ne peut pas être utilisé pour le retarget. | RIG_TASK_ID | Oui | - |
| `animation` | L’animation prédéfinie à appliquer au modèle riggé. Les animations `preset:*` fonctionnent avec les deux modèles de rig ; les animations `preset:biped:*` nécessitent un rig réalisé avec la version de modèle v1.0-20240301. | COMBO | Oui | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>plus d’autres options `"preset:biped:*"` affichées dans l’interface |
| `out_format` | Format du fichier de sortie ; le résultat arrive sur la sortie correspondante. (défaut : glb) | COMBO | Non | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | Inclure le maillage dans l’export ; si désactivé, seul le squelette animé est exporté. (défaut : True) | BOOLEAN | Non | True<br>False |
| `animate_in_place` | Jouer l’animation sur place, sans déplacement de la racine. (défaut : False) | BOOLEAN | Non | True<br>False |
| `auth_token_comfy_org` | Jeton d’authentification pour l’accès à l’API Comfy.org (paramètre masqué). | AUTH_TOKEN_COMFY_ORG | Non | - |
| `api_key_comfy_org` | Clé API pour l’accès au service Comfy.org (paramètre masqué). | API_KEY_COMFY_ORG | Non | - |
| `unique_id` | Identifiant unique pour le suivi de l’opération (paramètre masqué). | UNIQUE_ID | Non | - |

Remarque : Les animations du groupe `preset:*` fonctionnent avec les deux modèles de rig, tandis que les animations du groupe `preset:biped:*` nécessitent un rig réalisé avec la version de modèle v1.0-20240301. Si le rig référencé a été créé avec la spécification Mixamo et une version de modèle commençant par `v1.0`, l’appel de retarget échoue avec une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Le fichier de modèle 3D animé généré (uniquement pour la rétrocompatibilité). | STRING |
| `retarget task_id` | L’identifiant de tâche pour le suivi de l’opération de retarget. | RETARGET_TASK_ID |
| `GLB` | Le modèle 3D animé au format GLB. Renseigné lorsque `out_format` est `glb`. | FILE3DGLB |
| `FBX` | Le modèle 3D animé au format FBX. Renseigné lorsque `out_format` est `fbx`. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/fr.md)

---
**Source fingerprint (SHA-256):** `e5417a8fa584285ba9e57526e65b091c2383374c70364df9053777a3ce09541a`
