from db import Database

_tier_to_name = {
    "S": "Legendary Item",
    "A": "Epic Item",
    "B": "Rare Item",
    "C": "Uncommon Item",
    "D": "Common Item",
}

cursor, con = Database.connect()


class Item:
    def __init__(
        self,
        id: str | None = None,
        tier: str | None = None,
        path: str | None = None,
        name: str | None = None,
    ):
        self.id = id
        self.tier = tier
        self.path = path
        self.name = name

    @classmethod
    def from_db(cls, id: str):
        res = cursor.execute("SELECT * FROM items WHERE id = ?", (id,))
        item = res.fetchone()

        return cls(
            id=item[0], tier=item[1], path=item[2], name=_tier_to_name.get(item[1])
        )

    def save(self):
        cursor.execute(
            "INSERT OR IGNORE INTO items (id, tier, path) VALUES (?, ?, ?)",
            (self.id, self.tier, self.path),
        )
        con.commit()

    def open(self):
        print("Opening item:", self.id)
        print(self.path)


class OwnedItem:
    def __init__(self, owned_id: str, item: Item):
        self.owned_id = owned_id
        self.item = item

    @classmethod
    def from_db(cls, owned_id: str):
        res = cursor.execute("SELECT item_id FROM owned_items WHERE id = ?", (id,))
        item_id = res.fetchone()[0]

        item = Item.from_db(item_id)

        return cls(owned_id=owned_id, item=item)

    @classmethod
    def get_all(cls):
        res = cursor.execute("SELECT * FROM owned_items")
        rows = res.fetchall()

        return [Item.from_db(item_id) for _, item_id in rows]

    @staticmethod
    def get_count() -> int:
        res = cursor.execute("SELECT COUNT(id) FROM owned_items")
        rows = res.fetchone()

        return rows[0]
