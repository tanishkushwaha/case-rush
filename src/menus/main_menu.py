from rich import print as rprint
from datetime import datetime
from pathlib import Path
import time

from src.models.case import Case
from src.config import Config
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
            last_claim_time = load_claim_time()

            if last_claim_time is None:
                can_claim = True
            else:
                cooldown = Config.get_delays().get("claim_cooldown") or 3600

                diff = int((datetime.now() - last_claim_time).total_seconds())
                if diff < cooldown:
                    rprint(
                        f"You can claim next case in {time.strftime("%Hh %Mm %Ss", time.gmtime(cooldown - diff))}."
                    )
                    can_claim = False
                else:
                    can_claim = True

            if can_claim:
                save_claim_time()
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


def save_claim_time():
    with open("data/last_claim", "w") as file:
        file.write(datetime.now().isoformat())


def load_claim_time() -> datetime | None:
    file_path = Path("data/last_claim")

    if file_path.exists():
        try:
            with open(file_path, "r") as file:
                iso_str = file.read()
                return datetime.fromisoformat(iso_str)

        except Exception:
            return None
