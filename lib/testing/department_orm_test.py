import pytest
from lib.department import Department
from lib.db import CONN, CURSOR

def test_department_save():
    dept = Department("HR").save()
    CURSOR.execute("SELECT name FROM department WHERE id = ?", (dept.id,))
    row = CURSOR.fetchone()
    assert row[0] == "HR"
