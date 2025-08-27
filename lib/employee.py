from lib.db import CONN, CURSOR
from lib.department import Department

class Employee:
    def __init__(self, name, department_id=None):
        self.name = name
        self.department_id = department_id

    def save(self):
        CURSOR.execute(
            "INSERT INTO employee (name, department_id) VALUES (?, ?)",
            (self.name, self.department_id)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT id, name, department_id FROM employee")
        return [cls(row[1], row[2]) for row in CURSOR.fetchall()]
