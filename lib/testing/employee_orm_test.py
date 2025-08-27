import pytest
from lib.employee import Employee
from lib.department import Department
from lib.db import CONN, CURSOR

def test_employee_save():
    dept = Department("IT").save()
    emp = Employee("Alice", dept.id).save()
    CURSOR.execute("SELECT name, department_id FROM employee WHERE id = ?", (emp.id,))
    row = CURSOR.fetchone()
    assert row[0] == "Alice"
    assert row[1] == dept.id
