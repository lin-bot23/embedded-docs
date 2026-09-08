# Charger une vidéo

Le nœud Load Video charge des fichiers vidéo depuis le répertoire d’entrée et les rend disponibles pour le traitement dans le workflow. Il lit les fichiers vidéo depuis le dossier d’entrée désigné et les produit sous forme de données vidéo pouvant être connectées à d’autres nœuds de traitement vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `fichier` | Le fichier vidéo à charger depuis le répertoire d’entrée. La liste déroulante est remplie dynamiquement avec tous les fichiers vidéo trouvés dans le dossier d’entrée de ComfyUI, et de nouveaux fichiers vidéo peuvent être téléversés directement via le sélecteur de fichiers. | COMBO | Oui | Plusieurs options disponibles (tous les fichiers vidéo du répertoire d’entrée) |

**Remarque :** Les options disponibles pour le paramètre `file` sont remplies dynamiquement à partir des fichiers vidéo présents dans le répertoire d’entrée. Seuls les fichiers vidéo dont les types de contenu sont pris en charge sont affichés. Vous pouvez également téléverser un nouveau fichier vidéo directement via l’interface du sélecteur de fichiers du nœud. Si un fichier vidéo précédemment sélectionné est introuvable, le nœud signale une erreur de fichier invalide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Les données vidéo chargées qui peuvent être transmises à d’autres nœuds de traitement vidéo pour une manipulation ou une analyse ultérieure. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/fr.md)

---
**Source fingerprint (SHA-256):** `dcdd252792ade2a106c11826bbe7344011f0bc08506b80d634043a4dc156e076`
