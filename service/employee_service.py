from core.models import Employee
from repository.employee_repository import EmployeeRepository
from service.base_service import BaseService


class EmployeeService(BaseService[Employee]):
    def __init__(self, repository: EmployeeRepository):
        super().__init__(repository)
