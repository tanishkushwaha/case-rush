import random
from typing import List
import uuid
from case_rush.db import Database
from case_rush.models.item import Item, OwnedItem
from case_rush.config import Config

cursor, con = Database.connect()


class Case:
    """
    Data model for Case.
    """

    def __init__(self, id: str, item: Item):
        self.id = id
        self.item = item

    @classmethod
    def generate(cls):
        population = ["S", "A", "B", "C", "D"]
        weights = list(Config.get_drop_rates().values())

        rolled_tier = random.choices(population=population, weights=weights)[0]

        items = Item.get_by_tier(rolled_tier)
        item = random.choice(items)

        new_case_id = uuid.uuid4().hex[:4]
        new_case = cls(id=new_case_id, item=item)
        new_case.save()

        return new_case

    @classmethod
    def from_db(cls, id: str) -> "Case":
        res = cursor.execute("SELECT item_id FROM cases WHERE id = ?", (id,))
        item_id = res.fetchone()[0]

        return cls(id=id, item=Item.from_db(item_id))

    @classmethod
    def get_all(cls) -> List["Case"]:
        res = cursor.execute("SELECT * from cases")
        rows = res.fetchall()

        return [
            cls(id=case_id, item=Item.from_db(item_id)) for case_id, item_id in rows
        ]

    @staticmethod
    def get_count() -> int:
        res = cursor.execute("SELECT COUNT(id) FROM cases")
        rows = res.fetchone()

        return rows[0]

    def save(self):
        cursor.execute(
            "INSERT OR IGNORE INTO cases (id, item_id) VALUES (?, ?)",
            (self.id, self.item.id),
        )
        con.commit()

    def delete(self):
        cursor.execute("DELETE FROM cases WHERE id = ?", (self.id,))
        con.commit()

    @staticmethod
    def delete_all():
        cursor.execute("DELETE FROM cases")
        con.commit()

    def open(self):
        new_owned_item_id = uuid.uuid4().hex[:4]
        new_owned_item = OwnedItem(new_owned_item_id, self.item)
        new_owned_item.save()

        self.delete()

        return self.item
