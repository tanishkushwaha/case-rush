import sqlite3
from typing import Tuple


class Database:
    _connection: sqlite3.Connection | None = None
    _cursor: sqlite3.Cursor | None = None

    @classmethod
    def connect(cls) -> Tuple[sqlite3.Cursor, sqlite3.Connection]:
        if cls._connection is None:
            cls._connection = sqlite3.connect("./data/data.db")
            cls._cursor = cls._connection.cursor()

        if cls._cursor is None:
            raise RuntimeError("Failed to create cursor.")

        return (cls._cursor, cls._connection)

    @classmethod
    def close(cls):
        if cls._connection:
            cls._connection.close()
            cls._connection = None
            cls._cursor = None

    @classmethod
    def init(cls):
        cursor, connection = cls.connect()
        cursor.executescript(
            """
        CREATE TABLE IF NOT EXISTS items (
            id CHAR(5) NOT NULL,
            tier CHAR(1) NOT NULL,
            path VARCHAR(100) NOT NULL UNIQUE,
            PRIMARY KEY (id)
        );

        CREATE TABLE IF NOT EXISTS cases (
            id CHAR(4) NOT NULL,
            item_id CHAR(5) NOT NULL REFERENCES items(id)
        );

        CREATE TABLE IF NOT EXISTS owned_items (
            id CHAR(4) NOT NULL PRIMARY KEY,
            item_id CHAR(5) NOT NULL REFERENCES items(id)
        );
        """
        )

        connection.commit()
