import time
from rich import print as rprint
from case import Case
from item import OwnedItem
from utils import rich_string


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


def cases_menu():
    while True:
        cases = Case.get_all()
        cases_count = len(cases)
        rprint("\n[bold]----- Cases -----[/bold]\n")

        for idx, case in enumerate(cases):
            rprint(f"{idx + 1}. [italic]Case ({case.id})[/italic]")

        rprint(f"{cases_count + 1}. Go back")

        choice = int(input(f"\nChoose action (1-{cases_count + 1}): "))

        if choice > 0 and choice <= cases_count:
            case = cases[choice - 1]

            for t in range(5, 0, -1):
                rprint(
                    f"Unlocking case {case.id}... [italic]{t}s[/italic]",
                    end="\r",
                    flush=True,
                )
                time.sleep(1)

            item = case.open()
            rprint(f"\nYou found 1x {rich_string(item.tier, item.name)}")

        elif choice == cases_count + 1:
            break
        else:
            rprint("[red]Invalid choice, try again.[/red]")


def items_menu():
    while True:
        items = OwnedItem.get_all()
        items_count = len(items)
        rprint("\n[bold]----- Items -----[/bold]\n")

        for idx, item in enumerate(items):
            rprint(f"{idx + 1}. {rich_string(item.tier, f'{item.name} ({item.id})')}")
        rprint(f"{items_count + 1}. Go back")

        choice = int(input(f"\nChoose action (1-{items_count + 1}): "))

        if choice > 0 and choice <= items_count:
            items[choice - 1].open()

        elif choice == items_count + 1:
            break
        else:
            rprint("[red]Invalid choice, try again.[/red]")
