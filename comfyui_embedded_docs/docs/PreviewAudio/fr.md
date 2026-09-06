# AperçuAudio

Le nœud Preview Audio vous permet d'écouter l'audio directement dans l'interface de ComfyUI, sans avoir à l'enregistrer dans le répertoire de sortie. Il prend des données audio en entrée, vérifie qu'elles sont présentes, puis les transmet tout en affichant un lecteur audio temporaire afin que vous puissiez entendre le résultat.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Les données audio à prévisualiser. Le nœud lève une ValueError si l'entrée est None, ce qui peut se produire lorsque la vidéo source ne comporte pas de piste audio. | AUDIO | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | Les données audio transmises telles quelles depuis l'entrée. | AUDIO |
| `ui` | Affiche un widget lecteur audio dans l'interface pour prévisualiser l'audio. | UI |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/fr.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`
