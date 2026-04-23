# supplychain-lots

**Librairie Python pour résoudre des problèmes d’achat de lots fractionnables en programmation linéaire.**

Projet de Supply Chain & Software Engineering — **MECEN 1**  
**Auteur : William BE--GUIESSE & Bastien BARTHELEMY**

---

## Objectif du projet

Ce projet consiste à modéliser et résoudre un problème d’optimisation linéaire (achat de lots d’armement pour le pays PATIBULAIRE) en suivant une démarche structurée :

- **Phase 1** : Résolution manuelle, problème dual et analyse de sensibilité
- **Phase 2** : Généralisation en une classe réutilisable `LotProblem`
- **Phase 3** : Développement d’une librairie propre, typée, testée et documentée
- **Phase 4** : Interface en ligne de commande + README professionnel

---

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/bastienblmy/projet-sc-william-bastien.git
cd projet-sc-william-bastien

# Installer l'environnement avec uv
uv sync --extra dev

# Installer le package en mode développement
uv pip install -e .
```

## Utilisation 
### Via l’interface interactive :

```bash
uv run supplychain-lots
```  

Le programme vous demandera le chemin du fichier JSON.

### Exemple de fichier example.json

```bash
{
  "A": [
    [500, 300, 800],
    [1000, 2000, 1500],
    [10, 20, 15],
    [100, 80, 15],
    [80, 120, 200]
  ],
  "b": [100000, 200000, 100, 400, 400],
  "c": [10, 12, 15]
}
```

### Exemple de sortie

```bash
=== Solution : CLI_Problem ===
Statut           : Optimal
Coût total       : 1930.43 M$
Quantités optimales de lots :
   Lot  1      : 0.0000
   Lot  2      : 8.6957
   Lot  3      : 121.7391

✓ Résolution terminée - Coût total : 1930.43 M$
```
## Contenu du projet 

- notebooks/ → Phases 1 et 2 (résolution manuelle + généralisation)
- src/supplychain_lots/ → Package principal (core.py, cli.py)
- tests/ → Tests unitaires
- example.json → Données du problème PATIBULAIRE

## Outils utilisés

- uv — Gestion des dépendances
- PuLP — Solveur linéaire
- Ruff — Linting & formatage
- mypy — Typage statique
- pytest — Tests unitaires