from typing import List, Optional
import sqlite3

from lesson24.join import cursor
from models import Item
from database import get_db_connection

def create_item(item: Item) -> Item:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, description) values (?,?)",
        (item.name, item.description)
    )
    conn.commit()
    item.id =cursor.lastrowid
    conn.close()
    return item

def get_items() -> List[Item]:
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()































