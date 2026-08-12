import pytest
from ex11_3 import Employee

@pytest.fixture
def employee():
    employee = Employee('eric', 'matthes', 65000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.package == 70000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.package == 75000