from lib.db import CONN, CURSOR

class Department:
    def __init__(self, name):
        self.name = name

    def save(self):
        CURSOR.execute("INSERT INTO department (name) VALUES (?)", (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT id, name FROM department")
        return [cls(row[1]) for row in CURSOR.fetchall()]
