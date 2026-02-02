from __future__ import annotations

import json
from pathlib import Path

import typer
from rich import print

from promptguard.audit import audit_pairs
from promptguard.io import load_pairs_csv

app = typer.Typer(no_args_is_help=True)


@app.command()
def audit(
        input: Path = typer.Option(..., "--input", "-i", help="CSV file with prompt/output pairs"),
        out: Path = typer.Option(Path("results/report.json"), "--out", "-o", help="Output report path"),
        limit: int = typer.Option(0, "--limit", "-l", help="Limit number of rows (0 = all)"),
        prompt_col: str = typer.Option("prompt", help="Prompt column name"),
        output_col: str = typer.Option("output", help="Output column name"),
):
    """
    Run batch audit over a CSV dataset and write a JSON report.
    """
    pairs = load_pairs_csv(input, prompt_col=prompt_col, output_col=output_col, limit=limit)
    report = audit_pairs(pairs)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[green]OK[/green] audited {report['count']} items")
    print(f"[cyan]Report:[/cyan] {out}")


if __name__ == "__main__":
    app()