from lib.db import CONN, CURSOR
from lib.employee import Employee

class Review:
    def __init__(self, employee_id, content):
        self.employee_id = employee_id
        self.content = content

    def save(self):
        CURSOR.execute(
            "INSERT INTO review (employee_id, content) VALUES (?, ?)",
            (self.employee_id, self.content)
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        return self

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT id, employee_id, content FROM review")
        return [cls(row[1], row[2]) for row in CURSOR.fetchall()]
