# Backend d’attention du modèle

## Aperçu

Le nœud ModelAttentionBackend vous permet de sélectionner une implémentation d'attention dense pour un modèle. Il applique le backend d'attention sélectionné au modèle, ce qui peut être soit l'attention PyTorch ou l'attention Comfy Kitchen lorsque disponible. Ce nœud est particulièrement utile lorsque l'attention sparse est inactive ou non prise en charge, assurant ainsi que le modèle fonctionne avec le mécanisme d'attention dense spécifié.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `modèle` | Le modèle qui sera corrigé avec le backend d'attention sélectionné. | MODEL | Oui |  |
| `attention` | Le backend d'attention dense à appliquer au modèle. Les options disponibles sont "attention pytorch" et "attention comfy kitchen" si la dernière est disponible dans l'environnement. | STRING | Oui | "attention pytorch"<br> "attention comfy kitchen" (quand disponible) |

- L'option "attention comfy kitchen" utilise une attention quantifiée INT8 et est prise en charge uniquement sur les GPU Nvidia et AMD.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `model` | Le modèle d'entrée avec le backend d'attention sélectionné appliqué. | MODEL |

## Note

- Si le backend d'attention sélectionné n'est pas disponible, le nœud bascule automatiquement à l'attention PyTorch et enregistre un avertissement.
- Le nœud ModelAttentionBackend est expérimental et peut être soumis à des modifications dans les versions futures.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/fr.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
