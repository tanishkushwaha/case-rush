from rich import print as rprint

from src.models.case import Case
from .inventory_menu import inventory_menu
from .settings_menu import settings_menu


def main_menu():
    while True:
        rprint("\n[bold]----- Case Rush -----[/bold]\n")
        rprint("1. Open Inventory")
        rprint("2. Claim Daily Case")
        rprint("3. Settings")
        rprint("4. Exit")

        choice = int(input("\nChoose action (1-4): "))

        if choice == 1:
            inventory_menu()

        elif choice == 2:
            new_case = Case.generate()
            rprint(
                f"[bold green]Successfully claimed[/bold green] [italic]1x Case ({new_case.id})[/italic]"
            )

        elif choice == 3:
            settings_menu()

        elif choice == 4:
            break

        else:
            rprint("[red]Invalid choice, try again.[/red]")
