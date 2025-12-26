"""
CLI for Items Menu and Item Menu.
"""

from rich import print as rprint

from case_rush.models.item import OwnedItem
from case_rush.utils import rich_string
from case_rush.menu_actions import open_web_inventory
from .confirm_menu import confirm_menu


def items_menu():
    while True:
        owned_items = OwnedItem.get_all()
        owned_items_count = len(owned_items)
        rprint("\n[bold]----- Items -----[/bold]\n")

        for idx, owned_item in enumerate(owned_items):
            rprint(
                f"{idx + 1}. {rich_string(owned_item.item.tier, f'{owned_item.item.name} ({owned_item.item.id})')}"
            )
        rprint(f"{owned_items_count + 1}. Open GUI")
        rprint(f"{owned_items_count + 2}. Go back")

        choice = int(input(f"\nChoose action (1-{owned_items_count + 2}): "))

        if choice > 0 and choice <= owned_items_count:
            owned_item = owned_items[choice - 1]
            item_menu(owned_item)
            break

        elif choice == owned_items_count + 1:
            success = open_web_inventory()

            if not success:
                rprint("[red]Failed opening in web browser.[/red]")

            rprint("[green]Opened in web browser.[/green]")

        elif choice == owned_items_count + 2:
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
