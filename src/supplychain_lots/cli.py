"""
CLI minimaliste pour supplychain-lots.
"""

import typer
import json
from pathlib import Path

from supplychain_lots.core import LotProblem

def main():
    """Point d'entrée simple pour la CLI."""
    typer.echo("=== Supplychain-lots CLI ===\n")

    # Demande interactive du fichier
    input_path = typer.prompt("Entrez le chemin du fichier JSON", default="example.json")

    path = Path(input_path)
    if not path.exists():
        typer.secho(f"Erreur : Le fichier {path} n'existe pas.", fg=typer.colors.RED)
        raise typer.Exit(1)

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        problem = LotProblem(
            A=data["A"],
            b=data["b"],
            c=data["c"],
            name="CLI_Problem"
        )

        print(problem.get_solution_summary())

        typer.secho(f"\n✓ Résolution terminée - Coût total : {problem.objective_value:.2f} M$", fg=typer.colors.GREEN)

    except Exception as e:
        typer.secho(f"Erreur lors de la résolution : {e}", fg=typer.colors.RED)
        raise typer.Exit(1)


if __name__ == "__main__":
    main()