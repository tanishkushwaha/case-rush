from rich import print as rprint

from src.models.case import Case
from src.models.item import OwnedItem
from .cases_menu import cases_menu
from .items_menu import items_menu


def inventory_menu():
    while True:
        cases_count = Case.get_count()
        items_count = OwnedItem.get_count()

        rprint("\n[bold]----- Inventory -----[/bold]\n")
        rprint(f"1. Cases ({cases_count})")
        rprint(f"2. Items ({items_count})")
        rprint("3. Go back")

        choice = int(input("\nChoose action (1-3): "))

        if choice == 1:
            cases_menu()
        elif choice == 2:
            items_menu()
        elif choice == 3:
            break
        else:
            rprint("[red]Invalid choice, try again.[/red]")
