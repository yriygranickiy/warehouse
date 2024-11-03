from core.models import Employee
from repository.employee_repository import EmployeeRepository


class EmployeeService:

    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def create_employee(self, first_name, last_name, email, position,phone):
        employee = Employee(first_name=first_name, last_name=last_name, email=email,position=position,phone=phone)
        self.employee_repository.add(employee)

    def get_all_employees(self):
        return self.employee_repository.get_all()