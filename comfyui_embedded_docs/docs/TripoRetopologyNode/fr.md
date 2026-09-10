# Tripo : Retopologie

Tripo: Retopology prend un modèle 3D high-poly généré par un nœud Tripo précédent et le reconstruit en une version low-poly avec une topologie propre. Il soumet le modèle au service de retopologie Tripo, attend la fin de la tâche, puis télécharge le modèle terminé et expose son ID de tâche pour être utilisé par d'autres nœuds Tripo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_task_id` | ID de tâche du modèle high-poly source. Accepte un ID de tâche de modèle provenant d'un nœud de génération Tripo ou un ID de tâche de segmentation provenant de Tripo: Segment Model. | STRING | Oui | ID de tâche Tripo |
| `face_limit` | Nombre de faces cible : 500 à 20 000 triangles ou 500 à 10 000 quads. -1 laisse Tripo choisir. (par défaut : -1) | INT | Oui | -1 (automatic)<br>500 à 20 000 (triangles)<br>500 à 10 000 (quads) |
| `quad` | Sortie de maillage en quads. Tripo livre les maillages quads au format FBX, donc le résultat arrive sur la sortie FBX et la sortie GLB reste vide. (par défaut : False) | BOOLEAN | Oui | True<br>False (par défaut) |
| `bake` | Cuire les textures source sur le maillage low-poly. (par défaut : True) | BOOLEAN | Non | True (par défaut)<br>False |
| `part_names` | Noms de parties séparés par des virgules provenant de Tripo: Segment Model. Vide traite le modèle entier. (par défaut : "") | STRING | Non | Noms de parties du modèle ou vide |

Remarque : Lorsque `face_limit` est défini sur -1, Tripo décide automatiquement du nombre de faces. Lorsque `quad` est activé, la limite maximale de faces est de 10 000 quads au lieu de 20 000 triangles, et le résultat est fourni au format FBX (la sortie GLB reste vide). Lorsque `part_names` est vide, le modèle entier est traité. Si `face_limit` est différent de -1 et se trouve en dehors de la plage autorisée, le nœud lève une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Sortie rétrocompatible qui identifie le fichier de modèle terminé. Les flux de travail plus récents doivent plutôt utiliser les sorties GLB ou FBX. | STRING |
| `ID de tâche du modèle` | ID de tâche du résultat de retopologie terminé. Peut être transmis à d'autres nœuds Tripo pour référencer ce modèle. | STRING |
| `GLB` | Le modèle low-poly retopologisé au format GLB. Vide lorsque `quad` est activé. | GLB FILE |
| `FBX` | Le modèle low-poly retopologisé au format FBX. Rempli uniquement lorsque `quad` est activé. | FBX FILE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/fr.md)

---
**Source fingerprint (SHA-256):** `b0e967eb4987a70242b6cfce93f09e0caffb7f4bdd3e4f1439e68f33f9138bb5`
