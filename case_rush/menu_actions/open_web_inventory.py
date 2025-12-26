from typing import Any
from jinja2 import Environment, PackageLoader

from case_rush.models import OwnedItem
from case_rush.paths import CACHE_DIR
from case_rush.utils import img_to_base64, open_html_silent


def open_web_inventory() -> bool:
    """
    Injects owned items into the html template and calls open_html_silent function.

    :return: Success
    :rtype: bool
    """
    env = Environment(loader=PackageLoader("case_rush", "templates"))

    template = env.get_template("inventory.html")

    items: Any = [
        {
            "obj": owned_item.item,
            "item_img_blob": (
                img_to_base64(owned_item.item.path) if owned_item.item.path else None
            ),
        }
        for owned_item in OwnedItem.get_all()
    ]

    output = template.render(items=items)

    with open(CACHE_DIR / "inventory.html", "w") as f:
        f.write(output)

    return open_html_silent(str(CACHE_DIR / "inventory.html"))
