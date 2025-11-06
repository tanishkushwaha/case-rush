import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

query = """CREATE TABLE IF NOT EXISTS items (
  id CHAR(5) NOT NULL,
  tier CHAR(1) NOT NULL,
  path VARCHAR(100) NOT NULL UNIQUE,
  PRIMARY KEY (id)
);"""

cursor.execute(query)

query = """CREATE TABLE IF NOT EXISTS cases (
  id CHAR(4) NOT NULL,
  item_id CHAR(5) NOT NULL REFERENCES items(id)
);"""

cursor.execute(query)

query = """CREATE TABLE IF NOT EXISTS owned_items (
  id CHAR(4) NOT NULL PRIMARY KEY,
  item_id CHAR(5) NOT NULL REFERENCES items(id)
);"""

cursor.execute(query)
