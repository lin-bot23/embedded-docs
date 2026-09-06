# ModelPatchLoader

Le nœud ModelPatchLoader charge un fichier de patch de modèle depuis le dossier `model_patches` et le prépare pour une utilisation dans un flux de travail. Il détecte automatiquement le type de patch contenu dans le fichier, construit l'architecture correspondante, charge les poids sauvegardés et enveloppe le tout dans un model patcher afin de pouvoir l'appliquer à d'autres modèles. Il prend en charge de nombreux formats de patch spécialisés, notamment les branches ControlNet supplémentaires, les modèles de plongement de caractéristiques, les adaptateurs et modules similaires.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom` | Le nom du fichier de patch de modèle à charger depuis le dossier model_patches. Sélectionnez l'un des fichiers de patch disponibles dans la liste. | COMBO | Oui | Liste générée dynamiquement de tous les fichiers de patch de modèle trouvés dans le dossier model_patches |

Remarque : Ce nœud est marqué comme expérimental. Le type de patch est détecté automatiquement à partir du contenu du fichier, aucune sélection manuelle du type n'est donc nécessaire.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL_PATCH` | Le patch de modèle chargé, enveloppé dans un ModelPatcher, prêt à être appliqué à un modèle dans le flux de travail | MODEL_PATCH |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/fr.md)

---
**Source fingerprint (SHA-256):** `2994f076f8b28e2576304d308a2a4d630a0e6cc330afbc8d11d799241dc27469`
