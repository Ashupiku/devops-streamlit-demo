#--Ensures the database can be created and accessed. Used in CI.--
import sqlite3
import os

def test_database_creation():
    db_name = "test.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS demo (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()
    conn.close()
    assert os.path.exists(db_name)
    os.remove(db_name)
