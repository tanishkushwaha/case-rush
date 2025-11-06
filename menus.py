from rich import print as rprint
from case import Case
from item import OwnedItem


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
        case_ids = Case.get_all()
        item_ids = OwnedItem.get_all()

        rprint("\n[bold]----- Inventory -----[/bold]\n")
        rprint(f"1. Cases ({len(case_ids)})")
        rprint(f"2. Items ({len(item_ids)})")
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
        case_ids = Case.get_all()
        cases_count = len(case_ids)
        rprint("\n[bold]----- Cases -----[/bold]\n")

        for idx, case in enumerate(case_ids):
            rprint(f"{idx + 1}. [italic]Case ({case})[/italic]")

        rprint(f"{cases_count + 1}. Go back")

        choice = int(input(f"\nChoose action (1-{cases_count + 1}): "))

        if choice > 0 and choice <= cases_count:
            case = Case.from_id(case_ids[choice - 1])
            case.open()

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

            if item.tier == "S":
                rprint(
                    f"{idx+1}. [italic yellow]{item.name} ({item.id})[/italic yellow]"
                )
            elif item.tier == "A":
                rprint(
                    f"{idx+1}. [italic magenta]{item.name} ({item.id})[/italic magenta]"
                )
            elif item.tier == "B":
                rprint(f"{idx+1}. [italic red]{item.name} ({item.id})[/italic red]")
            elif item.tier == "C":
                rprint(f"{idx+1}. [italic green]{item.name} ({item.id})[/italic green]")
            elif item.tier == "D":
                rprint(f"{idx+1}. [italic blue]{item.name} ({item.id})[/italic blue]")

        rprint(f"{items_count + 1}. Go back")

        choice = int(input(f"\nChoose action (1-{items_count + 1}): "))

        if choice > 0 and choice <= items_count:
            items[choice - 1].open()

        elif choice == items_count + 1:
            break
        else:
            rprint("[red]Invalid choice, try again.[/red]")
