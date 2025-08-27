import pytest
from lib.employee import Employee
from lib.review import Review
from lib.db import CONN, CURSOR

def test_review_save():
    emp = Employee("Charlie").save()
    rev = Review(emp.id, "Great work").save()
    CURSOR.execute("SELECT content FROM review WHERE id = ?", (rev.id,))
    row = CURSOR.fetchone()
    assert row[0] == "Great work"
