import time
from src.config import Config
from rich import print as rprint
from src.models.case import Case
from src.models.item import OwnedItem
from src.utils import rich_string


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
            case_menu(case)
            break

        elif choice == cases_count + 1:
            break
        else:
            rprint("[red]Invalid choice, try again.[/red]")


def case_menu(case: Case):
    while True:
        rprint(f"----- [bold]Case ({case.id})[/bold] -----\n")
        rprint("1. Open")
        rprint("2. Destroy")
        rprint("3. Go back")

        choice = int(input("Choose action (1-3): "))

        if choice == 1:
            for t in range(Config.get_delays().get("case_opening") or 5, 0, -1):
                rprint(
                    f"Opening case {case.id}... [italic]{t}s[/italic]",
                    end="\r",
                    flush=True,
                )
                time.sleep(1)

            item = case.open()
            rprint(f"\nYou found 1x {rich_string(item.tier, item.name)}")
            break

        elif choice == 2:
            if confirm_menu(
                f"Are you sure you want to [red]destroy[/red] [italic]Case ({case.id})[/italic]?"
            ):
                case.delete()
                rprint(f"Successfully destroyed [italic]Case ({case.id})[/italic]")
            break

        elif choice == 3:
            break
        else:
            rprint("[red]Invalid choice, try again.[/red]")


def items_menu():
    while True:
        owned_items = OwnedItem.get_all()
        owned_items_count = len(owned_items)
        rprint("\n[bold]----- Items -----[/bold]\n")

        for idx, owned_item in enumerate(owned_items):
            rprint(
                f"{idx + 1}. {rich_string(owned_item.item.tier, f'{owned_item.item.name} ({owned_item.item.id})')}"
            )
        rprint(f"{owned_items_count + 1}. Go back")

        choice = int(input(f"\nChoose action (1-{owned_items_count + 1}): "))

        if choice > 0 and choice <= owned_items_count:
            owned_item = owned_items[choice - 1]
            item_menu(owned_item)
            break

        elif choice == owned_items_count + 1:
            break
        else:
            rprint("[red]Invalid choice, try again.[/red]")


def item_menu(owned_item: OwnedItem):
    while True:
        rprint(f"----- [bold]Item ({owned_item.item.id})[/bold] -----\n")
        rprint("1. Destroy")
        rprint("2. Go back")

        choice = int(input("Choose action (1-2): "))

        if choice == 1:
            if confirm_menu(
                f"Are you sure you want to [red]destroy[/red] {rich_string(owned_item.item.tier, f'{owned_item.item.name} ({owned_item.item.id})')}?"
            ):
                owned_item.delete()
                rprint(
                    f"Successfully destroyed 1x {rich_string(owned_item.item.tier, f'{owned_item.item.name} ({owned_item.item.id})')}"
                )
            break

        elif choice == 2:
            break
        else:
            rprint("[red]Invalid choice, try again.[/red]")


def confirm_menu(question: str) -> bool:
    while True:
        rprint(question)
        rprint("1. [red]Yes[/red]")
        rprint("2. [green]No[/green]")

        choice = int(input("Choose action (1-2): "))

        if choice == 1:
            return True

        return False
