# Aperçu de n'importe quel

PreviewAny convertit toute valeur d’entrée en texte lisible afin que vous puissiez l’inspecter. Les chaînes de caractères sont transmises telles quelles, les nombres et les booléens deviennent du texte brut, et les autres types de données sont sérialisés en JSON lorsque c’est possible (en revenant à leur forme de chaîne simple si la sérialisation échoue). Le texte obtenu est affiché dans l’interface utilisateur et également renvoyé sous forme de chaîne de sortie pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `source` | Accepte tout type de données en entrée pour l’affichage de l’aperçu. Si aucune valeur n’est fournie, l’aperçu affiche « None ». | ANY | Oui | Tout type de données |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `result` | La valeur d’entrée convertie au format texte. Le même texte est également affiché dans l’interface utilisateur. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/fr.md)

---
**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`
