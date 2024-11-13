from sqlalchemy.orm import Session

from core.models import Employee
from repository.base_repository import BaseRepository


class EmployeeRepository(BaseRepository[Employee]):
    def __init__(self, session: Session):
        super().__init__(session,Employee)

