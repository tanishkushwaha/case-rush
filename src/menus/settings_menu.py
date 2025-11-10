from rich import print as rprint

from src.utils import export_data
from src.models import Case, Item, OwnedItem
from src.config import Config
from .confirm_menu import confirm_menu


def settings_menu():
    while True:
        rprint("\n[bold]----- Settings -----[/bold]\n")
        rprint("1. Export Data")
        rprint("2. Import Data")
        rprint("3. Factory Reset")
        rprint("4. Reset Config to default")
        rprint("5. Go back")

        choice = int(input("\nChoose action (1-5): "))

        if choice == 1:
            path = export_data()
            rprint(f"Data exported successfully in [italic]{path}[/italic]")

        elif choice == 2:
            rprint(
                "[yellow]Extract the contents of the exported [italic].zip[/italic] archive into the [bold]data/[/bold] directory.[/yellow]"
            )

        elif choice == 3:
            if confirm_menu(
                "This action will reset the [bold]inventory[/bold] and [bold]config[/bold].\n[italic]Note: it will not delete any item files but will reset the database.[/italic]\nAre you sure you want to continue?"
            ):
                Item.delete_all()
                Case.delete_all()
                OwnedItem.delete_all()
                Config.reset()

                rprint(
                    "[green]Reset completed. Please restart the application.[/green]"
                )

        elif choice == 4:
            if confirm_menu(
                "Are you sure you want to reset [italic]config.toml[/italic]?"
            ):
                Config.reset()

                rprint(
                    "[green]Config reset successful. Please restart the application.[/green]"
                )

        elif choice == 5:
            break

        else:
            rprint("[red]Invalid choice, try again.[/red]")
