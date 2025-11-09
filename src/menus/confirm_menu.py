from rich import print as rprint


def confirm_menu(question: str) -> bool:
    while True:
        rprint(question)
        rprint("1. [red]Yes[/red]")
        rprint("2. [green]No[/green]")

        choice = int(input("Choose action (1-2): "))

        if choice == 1:
            return True

        return False
