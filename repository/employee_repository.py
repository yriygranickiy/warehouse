from sqlalchemy.orm import Session

from core.models import Employee


class EmployeeRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, employee: Employee):
        self.session.add(employee)
        self.session.commit()

    def get_all(self):
        return self.session.query(Employee).all()

    def get_by_id(self, employee_id):
        return self.session.query(Employee).filter_by(id=employee_id).first()

    # def update(self, employee: Employee):
    #     self.session.commit()

    def delete(self, employee: Employee):
        self.session.delete(employee)
        self.session.commit()