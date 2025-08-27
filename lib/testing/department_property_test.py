import pytest
from lib.department import Department

def test_department_name():
    dept = Department("Finance")
    assert dept.name == "Finance"
