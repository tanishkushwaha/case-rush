from pathlib import Path
import uuid
from item import Item


def index_items():
    base_dir = Path("./items")
    tiers = ["S", "A", "B", "C", "D"]

    for tier in tiers:
        for path in [str(item.resolve()) for item in (base_dir / tier).rglob("*")]:
            id = f"{tier}{uuid.uuid4().hex[:4]}"

            item = Item(id, tier, path)
            item.save()


def rich_string(tier: str | None, text: str | None) -> str | None:
    if tier is None or text is None:
        return None

    string_by_tier = {
        "S": f"[bold yellow]{text}[/bold yellow]",
        "A": f"[bold magenta]{text}[/bold magenta]",
        "B": f"[bold red]{text}[/bold red]",
        "C": f"[bold green]{text}[/bold green]",
        "D": f"[bold blue]{text}[/bold blue]",
    }

    return string_by_tier.get(tier)
