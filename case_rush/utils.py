"""
Provides helper functions.
"""

from pathlib import Path
import uuid
import os
import subprocess
import zipfile
from datetime import datetime
import base64

from case_rush.models.item import Item
from case_rush.paths import DATA_DIR, EXPORT_DIR, ITEMS_DIR


def index_items():
    """
    Indexes items present in the base_dir to the database.
    """

    tiers = ["S", "A", "B", "C", "D"]

    for tier in tiers:
        for path in [str(item.resolve()) for item in (ITEMS_DIR / tier).rglob("*")]:
            id = f"{tier}{uuid.uuid4().hex[:4]}"

            item = Item(id, tier, path)
            item.save()


def rich_string(tier: str | None, text: str | None) -> str | None:
    """
    Prettifies the text based on item's tier.

    :param tier: Item tier (S, A, B, C, D)
    :type tier: str | None
    :param text: Text
    :type text: str | None
    :return: Prettified string
    :rtype: str | None
    """
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
    """
    Exports the contents of DATA_DIR to EXPORT_DIR.

    :return: Exported zip name
    :rtype: str
    """

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


def img_to_base64(path: str) -> str:
    """
    Encodes image to base64 and returns a data URI.

    :param path: Image file path
    :type path: str
    :return: Data URI
    :rtype: str
    """
    with open(path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


def open_html_silent(path: str):
    """
    Spawns a subprocess that opens a HTML in the browser without any stdouts.

    :param path: HTML file path
    :type path: str
    """
    url = Path(path).resolve().as_uri()
    try:
        subprocess.Popen(
            ["xdg-open", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        return True
    except Exception:
        return False


def save_claim_time():
    """
    Writes claim time to the DATA_DIR/last_claim.
    """

    with open(DATA_DIR / "last_claim", "w") as file:
        file.write(datetime.now().isoformat())


def load_claim_time() -> datetime | None:
    """
    Loads claim time from DATA_DIR/last_claim.

    :return: Last claim time
    :rtype: datetime | None
    """

    file_path = Path(DATA_DIR / "last_claim")

    if file_path.exists():
        try:
            with open(file_path, "r") as file:
                iso_str = file.read()
                return datetime.fromisoformat(iso_str)

        except Exception:
            return None
