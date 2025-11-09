from rich import print as rprint

from src.models.case import Case
from .inventory_menu import inventory_menu


def main_menu():
    while True:
        rprint("\n[bold]----- STS2 Menu -----[/bold]\n")
        rprint("1. Open Inventory")
        rprint("2. Claim Daily Case")
        rprint("3. Exit")

        choice = int(input("\nChoose action (1-3): "))

        if choice == 1:
            inventory_menu()

        elif choice == 2:
            new_case = Case.generate()
            rprint(
                f"[bold green]Successfully claimed[/bold green] [italic]1x Case ({new_case.id})[/italic]"
            )

        elif choice == 3:
            break

        else:
            rprint("[red]Invalid choice, try again.[/red]")
