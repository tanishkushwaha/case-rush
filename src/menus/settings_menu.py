from rich import print as rprint

from src.utils import export_data, factory_reset, reset_config


def settings_menu():
    while True:
        rprint("\n[bold]----- Settings -----[/bold]\n")
        rprint("1. Export Data")
        rprint("2. Import Data")
        rprint("3. Factory Reset")
        rprint("4. Reset Config [italic](config.toml)[/italic] to default")
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
            factory_reset()

        elif choice == 4:
            reset_config()

        elif choice == 5:
            break

        else:
            rprint("[red]Invalid choice, try again.[/red]")
