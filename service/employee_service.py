from core.models import Employee
from repository.employee_repository import EmployeeRepository


class EmployeeService:

    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def create_employee(self, employee: Employee):
        pass