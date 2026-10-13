# StockPilot — Soumission 1

Gestion de stock pour une petite boutique, en Python.

**Équipe :** Ilyas Safour, Zakaria Aouinat et Hajar Sellab.
**Cours :** Langage de script — 420-LS3-AS, Automne 2026.
**Numéro du groupe :** à compléter avant le dépôt.

## Exécution
Installer Python 3.10 ou plus récent. Aucune dépendance externe.
Dans un terminal ouvert dans ce dossier :

```bash
python main.py
```

Sous Windows, `py main.py` convient aussi. Pour les tests :

```bash
python test_stock.py
```

## Fonctionnalités réalisées
- Consulter trois produits fictifs.
- Enregistrer une sortie avec validation et mise à jour du stock.
- Afficher les alertes lorsque quantité <= seuil.
- Refuser les choix de menu invalides.

Les entrées de stock, l'ajout de produits et l'historique sont prévus aux étapes suivantes.
Les données restent en mémoire : elles reviennent à leur état initial après fermeture.
Ce prototype ne gère ni ventes, ni paiements, ni comptes utilisateurs.

## Démonstration courte
1. Choisir 1 : P001 contient 20 cahiers.
2. Choisir 2, P001, 15 : il reste 5 cahiers et une alerte apparaît.
3. Choisir 2, P001, 6 : sortie refusée, le stock reste à 5.
4. Choisir 3 : les cahiers et les classeurs sont à commander.
5. Choisir 0 pour fermer.

## Fichiers
- `main.py` : prototype en console.
- `test_stock.py` : 11 scénarios reproductibles.
- `docs/Proposition_Soumission1.pdf` : proposition, algorithme, deux organigrammes et tests.
- `docs/resultats_tests.txt` : résultats réellement obtenus.
- `docs/Guide_GitHub.md` : étapes du dépôt.
- `docs/Comprendre_le_projet.md` : explications des fonctions et préparation à la démonstration.
- `docs/Verification_avant_remise.md` : vérifications finales.

## Avant la remise
Compléter le numéro du groupe et renommer le PDF selon la convention :
`GroupeXX - StockPilot - Soumission1 - LangageScript.pdf`.
Vérifier l'échéance dans Léa et l'accès du professeur au dépôt.
Chaque membre doit exécuter le prototype et comprendre son fonctionnement.

## Aide et contributions
Une IA générative a aidé à préparer le code, la documentation et les tests.
Le prototype a été exécuté et vérifié dans l'environnement de préparation.
L'équipe doit relire, adapter et comprendre le travail, et vérifier que cette aide
est autorisée par l'enseignant. Les contributions personnelles effectivement réalisées
seront consignées par les membres dans Git ; aucune répartition fictive n'est déclarée.
