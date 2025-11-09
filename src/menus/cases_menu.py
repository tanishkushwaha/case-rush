import time
from rich import print as rprint

from src.config import Config
from src.models.case import Case
from src.utils import rich_string
from .confirm_menu import confirm_menu


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
