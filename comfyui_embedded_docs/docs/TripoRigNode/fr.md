# Tripo : Modèle squeletté

Ce nœud prend un modèle 3D Tripo existant et en crée une version riggée (avec squelette), ce qui signifie que le modèle obtient un squelette pour pouvoir être animé. Vous fournissez l’identifiant de tâche du modèle à rigger, puis choisissez la version du rig, le type de squelette, la convention de nommage des os et le format de fichier de sortie ; le nœud envoie la tâche à Tripo, attend qu’elle se termine, puis renvoie le résultat téléchargé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `ID_tâche_modèle_original` | L’identifiant de tâche du modèle 3D d’origine à rigger. Il s’agit généralement de l’identifiant produit par un nœud précédent de génération de modèle Tripo. | MODEL_TASK_ID | Oui | - |
| `model_version` | Version du modèle de rig à utiliser. v1.0 : personnages humanoïdes (bipèdes) uniquement, plus de 90 préréglages d’animation. v2.5 : créatures non humanoïdes (quadrupèdes, hexapodes, octopodes, aviaires, serpentines, aquatiques). Par défaut : `v1.0-20240301`. | COMBO | Non | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | Type de squelette. « auto » lance d’abord une vérification gratuite de rigging de Tripo et utilise le type recommandé. Les autres valeurs imposent un type de squelette spécifique, par exemple « biped » pour les personnages humanoïdes. Par défaut : « auto ». | COMBO | Non | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | Convention de nommage des os : Tripo native ou compatible Mixamo. Tripo ne peut pas réutiliser (retarget) ses préréglages d’animation sur un rig v1.0 créé avec la spécification mixamo ; utilisez tripo pour le nœud « Tripo: Retarget rigged model ». Par défaut : « tripo ». | COMBO | Non | "tripo"<br>"mixamo" |
| `out_format` | Format de fichier de sortie ; le résultat arrive sur la sortie correspondante. Par défaut : « glb ». | COMBO | Non | "glb"<br>"fbx" |

**Remarque :** La version de modèle v1.0 (`v1.0-20240301`) ne prend en charge que les squelettes bipèdes. Si un `rig_type` non-bipède est utilisé avec cette version, le nœud lève une erreur et vous invite à utiliser `v2.5-20260210` à la place.

**Remarque :** Lorsque `rig_type` est « auto », Tripo vérifie d’abord si le modèle peut être riggé et choisit le type de squelette recommandé. Si Tripo signale que le modèle ne peut pas être riggé, le nœud échoue avec une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `fichier_modèle` | Le fichier de modèle 3D riggé généré. Conservé uniquement pour la rétrocompatibilité. | STRING |
| `rig task_id` | L’identifiant de tâche pour suivre le processus de génération du rig. | RIG_TASK_ID |
| `GLB` | Le modèle riggé sous forme de fichier 3D GLB. Rempli lorsque `out_format` est « glb ». | FILE3DGLB |
| `FBX` | Le modèle riggé sous forme de fichier 3D FBX. Rempli lorsque `out_format` est « fbx ». | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/fr.md)

---
**Source fingerprint (SHA-256):** `54c3b0984835160b74884d2c30191ad6dac6ea447862e9276253ace7367bc419`
