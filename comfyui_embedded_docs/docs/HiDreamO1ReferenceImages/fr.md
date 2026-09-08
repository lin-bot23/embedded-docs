# Images de référence HiDream-O1

Ce nœud attache des images de référence aux conditionnements positif et négatif, afin que les nœuds en aval puissent les utiliser pour guider la génération. Les images de référence sont appliquées dans l’ordre numérique de leurs ports d’entrée. Si aucune image de référence n’est connectée, les conditionnements `positive` et `negative` sont transmis inchangés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positif` | Le conditionnement positif auquel attacher les images de référence. | CONDITIONING | Oui | - |
| `négatif` | Le conditionnement négatif auquel attacher les images de référence. | CONDITIONING | Oui | - |
| `images` | Les images de référence sont utilisées dans l’ordre numérique des ports. Lorsque des images sont fournies, elles sont attachées à la fois au conditionnement positif et au conditionnement négatif. | IMAGE | Non | 0 à 100 images (`image_1` à `image_100`) |

**Remarque sur le paramètre `images` :** Il s’agit d’une entrée à extension automatique qui fournit des ports numérotés `image_1` à `image_100`. Les images sont utilisées dans l’ordre numérique des ports. Cette entrée est facultative : si aucune image de référence n’est connectée, le nœud renvoie les conditionnements `positive` et `negative` inchangés. Lorsque des images sont connectées, le même ensemble d’images de référence est attaché aux deux sorties, et le conditionnement négatif est également marqué comme négatif avant que les images ne soient attachées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement `positive` avec les images de référence attachées. | CONDITIONING |
| `négatif` | Le conditionnement `negative` avec les images de référence attachées. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/fr.md)

---
**Source fingerprint (SHA-256):** `07f9f0ea19957523e95d04b9086dc994807bb0cd5262fe798dc784c1ecb4920d`
