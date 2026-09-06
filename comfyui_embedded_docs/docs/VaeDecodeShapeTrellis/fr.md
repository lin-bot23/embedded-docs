# VaeDecodeShapeTrellis

Ce nœud décode les représentations latentes de forme Trellis2 en un maillage 3D. Il utilise un VAE pour convertir les données latentes de forme éparses en géométrie de maillage et génère également les données de subdivision de forme produites lors du décodage. Le nœud prend en charge les entrées latentes individuelles et par lots et ajuste automatiquement l’orientation du maillage au repère de coordonnées attendu.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `samples` | Les échantillons latents à décoder, y compris le tenseur d’échantillons et les données de coordonnées éparses. Le dictionnaire latent peut également contenir des champs facultatifs : `coord_counts` pour les formes par lots, `coord_resolution` pour contrôler la résolution du maillage, et `model_frame` pour l’orientation des coordonnées. | LATENT | Oui | None |
| `vae` | Le modèle VAE utilisé pour décoder le latent de forme en un maillage. | VAE | Oui | None |

### Remarques sur `samples`

- L’entrée `samples` est un dictionnaire latent qui doit contenir le tenseur `samples` et les coordonnées éparses `coords`.
- Si `coord_counts` est présent, il doit s’agir d’un tenseur 1D d’entiers non négatifs, et la somme de tous les compteurs doit être égale au nombre total de lignes de coordonnées. Chaque compteur représente une forme du lot.
- Si `coord_resolution` est fourni, la résolution du maillage est calculée comme `coord_resolution * 16`. Sinon, le tampon de résolution intégré au VAE est utilisé (valeur par défaut : 1024).
- Si `model_frame` est défini sur `"z_up"`, les sommets du maillage décodé sont pivotés d’un système de coordonnées Z-up vers la convention Y-up utilisée par glTF. La valeur par défaut est `"y_up"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mesh` | Le maillage 3D décodé, contenant les positions des sommets et les indices de faces. Lors du décodage de plusieurs formes, les maillages sont renvoyés sous la forme d’un seul tenseur empilé s’ils partagent tous la même forme, ou d’un lot empaqueté de taille variable sinon. | MESH |
| `shape_subdivides` | Données de subdivision de forme produites à chaque étape du processus de décodage. | SHAPE_SUBDIVIDES |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/fr.md)

---
**Source fingerprint (SHA-256):** `28bd0f69c0ea58ca499f6523471cf6071c041c21242126715d56f362484377a2`
