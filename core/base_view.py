import time
from abc import abstractmethod
from typing import TypeVar, Generic, Protocol, List

from core.base_repository import EmployeeRepository, Repository
from core.base_service import Service, EmployeeService
from core.models import Employee
from database import SessionLocal

T = TypeVar('T')

session = SessionLocal()


class View(Protocol):
    @abstractmethod
    def get_view_all(self):
        ...


class BaseView(View):

    def __init__(self, service):
        self.service = service

    def get_view_all(self):
        self.get_view_all()


class EmployeeView(BaseView):
    def __init__(self, service: EmployeeService):
        super().__init__(service)
    #
    # repository = EmployeeRepository(session)
    # service = EmployeeService(repository)

    def get_view_all(self):
        employee_loop_menu = True

        while employee_loop_menu:
            print("\nEmployee:\n")
            print("1. Add")
            print("2. Delete")
            print("3. Update")
            print("4. Get all")
            print("5. Get employee by id")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                email = input("Enter your email: ")
                phone = input("Enter your phone number: ")
                created_employee = Employee(first_name=first_name,
                                            last_name=last_name,
                                            position="staff",
                                            email=email,
                                            phone=phone)
                print("Employee adding....")
                self.create(created_employee)
                time.sleep(0.3)
                print("Employee add successfully!")
            elif choice == "2":
                print("Input employee id for deleting")
                employee_id = int(input("Enter employee id: "))
                print("Deleting employee...")
                time.sleep(0.3)
                self.delete(employee_id)
                print("Employee delete successfully!")
            elif choice == "3":
                pass
            elif choice == "4":
                print("load list employee...")
                time.sleep(0.3)
                for employee in self.get_all():
                    print(employee)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                employee_id = input("Enter employee id: ")
                employee = self.get_by_id(employee_id)
                print("getting employee data...")
                time.sleep(0.3)
                print(employee)
                print("employee data get successfully!")
            elif choice == "6":
                employee_loop_menu = False
            else:
                print("Invalid choice")