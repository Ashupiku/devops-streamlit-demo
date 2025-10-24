# Simple test: try to connect to the SQLite database
import sqlite3
import os


def test_database_creation():
    db_name = "test.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS demo (id INTEGER PRIMARY KEY, name TEXT)"
    )
    conn.commit()
    conn.close()
    # Check that file exists
    assert os.path.exists(db_name)
    os.remove(db_name)
