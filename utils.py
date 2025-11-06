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
