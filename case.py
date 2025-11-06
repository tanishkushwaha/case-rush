import random
import uuid
from db import connection, cursor


class Case:
    def __init__(self, id: str, item_id: str):
        self.id = id
        self.item_id = item_id

    @classmethod
    def generate(cls):
        population = ["S", "A", "B", "C", "D"]
        weights = [0.02, 0.06, 0.12, 0.25, 0.5]

        roll = random.choices(population=population, weights=weights)[0]

        res = cursor.execute("SELECT id FROM items WHERE tier = ?", (roll))

        item_id = random.choice(res.fetchall())[0]
        case_id = uuid.uuid4().hex[:4]

        cursor.execute(
            "INSERT INTO cases (id, item_id) VALUES (?, ?)", (case_id, item_id)
        )
        connection.commit()

        return cls(id=case_id, item_id=item_id)

    @classmethod
    def from_id(cls, id: str) -> "Case":
        res = cursor.execute("SELECT item_id FROM cases WHERE id = ?", (id,))
        item_id = res.fetchall()[0][0]

        return cls(id=id, item_id=item_id)

    @staticmethod
    def get_all():
        res = cursor.execute("SELECT id from cases")
        rows = res.fetchall()
        cases = [item[0] for item in rows]

        return cases

    def open(self):
        print("Opening case", self.id)

        cursor.execute(
            "INSERT OR IGNORE INTO owned_items (id, item_id) VALUES (?, ?)",
            (uuid.uuid4().hex[:4], self.item_id),
        )
        cursor.execute("DELETE FROM cases WHERE id = ?", (self.id,))
        connection.commit()

        print(f"You found a {self.item_id}!")
