from pathlib import Path
import uuid
import os
import zipfile
from datetime import datetime

from src.models.item import Item


def index_items():
    base_dir = Path("./data/items")
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


def export_data() -> str:
    EXPORT_DIR = "export"

    os.makedirs(EXPORT_DIR, exist_ok=True)

    output_name = os.path.join(
        EXPORT_DIR, f'export_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.zip'
    )
    data_folder_path = "data"

    with zipfile.ZipFile(output_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(data_folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Keep folder structure inside ZIP
                arcname = os.path.relpath(file_path, data_folder_path)
                zipf.write(file_path, arcname)

    return output_name
