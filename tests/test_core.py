"""
Tests unitaires pour la classe LotProblem du package supplychain_lots.
"""

import pytest

from supplychain_lots.core import LotProblem


def test_patibulaire_solution():
    """Test sur le problème original du projet PATIBULAIRE."""
    A = [
        [500, 300, 800],
        [1000, 2000, 1500],
        [10, 20, 15],
        [100, 80, 15],
        [80, 120, 200]
    ]
    b = [100000, 200000, 100, 400, 400]
    c = [10, 12, 15]

    problem = LotProblem(A, b, c, name="Patibulaire")
    result = problem.solve()

    assert result["status"] == "Optimal"
    assert abs(result["objective_value"] - 1930.43) < 0.1
    assert len(result["solution"]) == 3
    assert result["solution"][0] == 0.0      # Lot 1 non utilisé
    assert result["solution"][1] > 8.0       # Lot 2 utilisé
    assert result["solution"][2] > 120.0     # Lot 3 utilisé


def test_generalisation():
    """Test sur un problème plus simple pour valider la généralisation."""
    A = [[100, 200], [150, 50]]
    b = [5000, 3000]
    c = [25, 18]

    problem = LotProblem(A, b, c, name="Test_Simple")
    result = problem.solve()

    assert result["status"] == "Optimal"
    assert result["objective_value"] > 0
    assert len(result["solution"]) == 2


def test_dimension_error():
    """Test que la classe lève correctement une erreur de dimension."""
    A = [[500, 300]]
    b = [100000, 200000]   # b a 2 éléments mais A n'a qu'une ligne
    c = [10, 12]

    with pytest.raises(ValueError, match="Dimension incompatible"):
        LotProblem(A, b, c)
