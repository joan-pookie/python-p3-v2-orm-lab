import pytest
from lib.employee import Employee

def test_employee_name():
    emp = Employee("Bob")
    assert emp.name == "Bob"
