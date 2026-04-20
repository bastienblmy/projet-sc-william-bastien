"""
supplychain_lots.core
=====================

Module principal contenant la classe LotProblem pour résoudre
les problèmes d'achat de lots fractionnables en programmation linéaire.
"""

from __future__ import annotations

import pulp
import numpy as np
from typing import List, Dict, Any, Optional


class LotProblem:
    """
    Classe permettant de modéliser et résoudre un problème d'achat de lots fractionnables.

    Il s'agit d'un programme linéaire de la forme :
        min c'x
        s.t. A x >= b
             x >= 0

    Cette classe est conçue pour être réutilisable, typée et maintenable.
    """

    def __init__(self, A: List[List[float]], b: List[float], c: List[float], name: str = "LotProblem") -> None:
        """
        Initialise un nouveau problème de lots.

        Parameters
        ----------
        A : List[List[float]]
            Matrice de composition des lots (lignes = armes, colonnes = lots)
        b : List[float]
            Vecteur des demandes minimales pour chaque arme
        c : List[float]
            Vecteur des coûts des différents lots
        name : str
            Nom descriptif du problème (utilisé pour l'affichage et le solveur)
        """
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.c = np.array(c, dtype=float)
        self.name = name

        self._solution: Optional[List[float]] = None
        self._objective_value: Optional[float] = None

        # Vérifications de cohérence
        if self.A.shape[0] != len(self.b):
            raise ValueError(
                f"Dimension incompatible : {self.A.shape[0]} lignes dans A, "
                f"mais {len(self.b)} éléments dans b"
            )
        if self.A.shape[1] != len(self.c):
            raise ValueError(
                f"Dimension incompatible : {self.A.shape[1]} colonnes dans A, "
                f"mais {len(self.c)} coûts dans c"
            )

    def solve(self) -> Dict[str, Any]:
        """
        Résout le problème linéaire primal.

        Returns
        -------
        Dict[str, Any]
            Dictionnaire contenant le statut, la valeur objective et la solution
        """
        prob = pulp.LpProblem(f"{self.name}_Primal", pulp.LpMinimize)

        # Variables de décision
        n_lots = self.A.shape[1]
        x = [pulp.LpVariable(f"lot_{i+1}", lowBound=0) for i in range(n_lots)]

        # Fonction objectif
        prob += pulp.lpSum(self.c[i] * x[i] for i in range(n_lots))

        # Contraintes
        for i in range(self.A.shape[0]):
            prob += (
                pulp.lpSum(self.A[i, j] * x[j] for j in range(n_lots)) >= self.b[i],
                f"Demande_arme_{i+1}"
            )

        # Résolution
        prob.solve(pulp.PULP_CBC_CMD(msg=False))

        # Mise à jour des résultats internes
        self._solution = [x[i].varValue for i in range(n_lots)]
        self._objective_value = pulp.value(prob.objective)

        return {
            "status": pulp.LpStatus[prob.status],
            "objective_value": round(self._objective_value, 4) if self._objective_value is not None else None,
            "solution": [round(val, 4) for val in self._solution] if self._solution else None,
        }

    def get_solution_summary(self) -> str:
        """Retourne un résumé lisible de la dernière solution."""
        if self._solution is None:
            self.solve()

        summary = f"\n=== Solution : {self.name} ===\n"
        summary += f"Statut           : Optimal\n"
        summary += f"Coût total       : {self._objective_value:.2f} M$\n"
        summary += "Quantités optimales de lots :\n"
        for i, qty in enumerate(self._solution, 1):
            summary += f"   Lot {i:2d}      : {qty:.4f}\n"

        return summary

    @property
    def objective_value(self) -> Optional[float]:
        """Retourne la valeur optimale de la fonction objectif."""
        return self._objective_value

    @property
    def solution(self) -> Optional[List[float]]:
        """Retourne la solution optimale (quantités de lots)."""
        return self._solution