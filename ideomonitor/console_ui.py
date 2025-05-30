from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def print_banner():
    console.print(
        Panel.fit(
            "[bold cyan]IdeoMonitor[/bold cyan] [dim]v0.1.1.0.2[/dim]\n"
            "[white]Pattern-based text scanner • Rootflux, 2025[/white]",
            border_style="cyan",
            padding=(1, 4),
        )
    )

def print_results(results):
    if not results:
        console.print("[green bold]No matches found.[/green bold] [dim]Clean as a whistle.[/dim]")
        return

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Line", width=6, style="white")
    table.add_column("Pattern", style="yellow")
    table.add_column("Context", style="dim", overflow="fold")
    for r in results:
        table.add_row(str(r['line']), r['pattern'], r['context'])
    console.print(table)

def print_error(message):
    console.print(f"[red bold]Error:[/red bold] {message}")

def prompt_file():
    return Prompt.ask("[bold]Text file to scan[/bold]", default="sample_text.txt")
