# My Library
from Home.Employee.home_employee import home_page_employee
from Home.Employee.home_owner import home_page_owner


# Distinguishes between roles
def home_page(employee: dict):
    if employee["role"] == "owner":
        home_page_owner(employee)
    else:
        home_page_employee(employee)
