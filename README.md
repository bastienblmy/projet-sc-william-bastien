# supplychain-lots

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-managed-4B8BBE)](https://github.com/astral-sh/uv)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Ruff](https://img.shields.io/badge/linter-ruff-blue)]()
[![mypy](https://img.shields.io/badge/typed-mypy-blue)]()

**Librairie Python pour résoudre des problèmes d’achat de lots fractionnables en programmation linéaire.**

Projet de Supply Chain & Software Engineering — M1 MIAGE  
**Auteur : William Bastien**

---

## ✨ Fonctionnalités

- Résolution efficace de programmes linéaires (primal)
- Classe `LotProblem` réutilisable, typée et documentée
- Interface en ligne de commande
- Tests unitaires + couverture de code
- Code maintenable et professionnel

---

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/bastienblmy/projet-sc-william-bastien.git
cd projet-sc-william-bastien

# Installer l'environnement avec uv (recommandé)
uv sync --extra dev

# Installer le package en mode développement
uv pip install -e .