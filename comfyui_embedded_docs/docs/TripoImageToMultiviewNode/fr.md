# Tripo : Image vers multivue

Génère les vues avant, gauche, arrière et droite du sujet à partir d'une seule image d'entrée à l'aide de l'API Tripo. L'image est téléversée, une tâche de génération multivue est lancée et interrogée jusqu'à son achèvement, puis les quatre vues résultantes sont renvoyées avec l'identifiant de tâche. Il s'agit d'une tâche payante facturée environ 0,10 USD.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image source du sujet à partir de laquelle Tripo génère les vues avant, gauche, arrière et droite. Une seule image est utilisée pour la requête, même si un lot est fourni. | IMAGE | Oui | Image unique |

Remarque : Le nœud appelle l'API cloud de Tripo et attend la fin de la tâche de génération. Une tâche typique prend environ 25 secondes. L'authentification est gérée automatiquement via les entrées masquées du nœud, donc aucune clé API Tripo ne doit être fournie dans le workflow. Le nœud exige les quatre URL de vue dans la réponse de Tripo (`front_view_url`, `left_view_url`, `back_view_url`, `right_view_url`) ; si une vue est manquante, l'exécution échoue avec une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `task_id multivue` | L'identifiant de tâche renvoyé par Tripo pour la requête de génération d'image multivue. Il peut être utilisé pour référencer la tâche terminée, par exemple lors du raffinement des vues avec Tripo: Edit Multiview. | MULTIVIEW_TASK_ID |
| `avant` | La vue avant générée du sujet. | IMAGE |
| `gauche` | La vue gauche générée du sujet. | IMAGE |
| `arrière` | La vue arrière générée du sujet. | IMAGE |
| `droite` | La vue droite générée du sujet. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/fr.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`
