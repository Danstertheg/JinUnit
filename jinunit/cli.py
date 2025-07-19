# cli.py
import typer
from pathlib import Path
from .core.generator import generate_test
import sys

app = typer.Typer(help="🧪 Generate JUnit tests for Java classes")

@app.command()
def generate(
    file: Path = typer.Argument(..., help="Path to a Java file or directory"),
    output_dir: Path = typer.Option("tests", help="Directory to save generated test files"),
    overwrite: bool = typer.Option(False, "--overwrite", "-o", help="Overwrite existing test files"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Print generated test instead of saving"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
):
    """
    Generate JUnit tests for Java files.
    """
    java_files = []

    if file.is_dir():
        java_files = list(file.rglob("*.java"))
    elif file.is_file():
        java_files = [file]
    else:
        typer.echo(f"❌ Invalid path: {file}")
        raise typer.Exit(1)

    if not java_files:
        typer.echo("⚠️  No Java files found.")
        raise typer.Exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    for java_file in java_files:
        if verbose:
            typer.echo(f"📄 Processing {java_file}")

        test_code = generate_test(java_file)

        output_file = output_dir / f"Test{java_file.stem}.java"
        if output_file.exists() and not overwrite:
            typer.echo(f"⏭️  Skipping existing file: {output_file}")
            continue

        if dry_run:
            typer.echo(f"\n--- {output_file} ---\n")
            typer.echo(test_code)
        else:
            output_file.write_text(test_code)
            typer.echo(f"✅ Test written to {output_file}")

    raise typer.Exit(0)

if __name__ == "__main__":
    app()
