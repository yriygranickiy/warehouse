import time
from abc import abstractmethod
from datetime import datetime
from random import random
from typing import Protocol

from core.base_service import  EmployeeService, CategoryService, OrderService
from core.models import Employee, Category, Order


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
                employee = Employee(first_name=first_name,
                                            last_name=last_name,
                                            position="staff",
                                            email=email,
                                            phone=phone)
                print("Employee adding....")
                self.create(employee)
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

class CategoryView(BaseView):
    def __init__(self, service:CategoryService):
        super().__init__(service)

    def get_view_all(self):

        category_loop_menu = True

        while category_loop_menu:
            print("\nCategory:\n")
            print("1. Add")
            print("2. Delete")
            print("3. Update")
            print("4. Get all")
            print("5. Get category by id")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                category_name = input("Enter name: ")
                category_desc = input("Enter description: ")
                created_category = Category(category_name=category_name,
                                            description=category_desc)
                print("Category adding....")
                time.sleep(0.3)
                self.create(created_category)
                print("Category add successfully!")
            elif choice == "2":
                category_id = int(input("Enter category id: "))
                print("Deleting category...")
                time.sleep(0.3)
                self.delete(category_id)
                print("Category delete successfully!")
            elif choice == "3":
                pass
            elif choice == "4":
                print("Load list category...")
                time.sleep(0.3)
                for category in self.get_all():
                    print(category)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                category_id = int(input("Enter category id: "))
                category = self.get_by_id(category_id)
                print("Getting category data...")
                time.sleep(0.3)
                print(category)
                print("category data get successfully!")
            elif choice == "6":
                category_loop_menu = False
            else:
                print("Invalid choice")

class OrderView(BaseView):
    def __init__(self, service:OrderService):
        super().__init__(service)

    def get_view_all(self):

        order_loop_menu = True

        while order_loop_menu:
            print("\nOrder:\n")
            print("1. Add")
            print("2. Delete")
            print("3. Update")
            print("4. Get all")
            print("5. Get order by id")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                quantity = int(input("Enter quantity: "))
                order = Order(quantity=quantity,
                              order_date=datetime.now(),
                              order_state='Pending',
                              product_id=random.randint(2, 3))
                print("Order adding....")
                time.sleep(0.3)
                self.create(order)
                print("Order add successfully!")
            elif choice == "2":
                order_id = int(input("Enter order id: "))
                print("Deleting order...")
                self.delete(order_id)
                time.sleep(0.3)
                print("Order delete successfully!")
            elif choice == "3":
                pass
            elif choice == "4":
                print("Load list order...")
                for order in self.get_all():
                    print(order)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                order_id = int(input("Enter order id: "))
                order = self.get_by_id(order_id)
                print("Getting order data...")
                time.sleep(0.3)
                print(order)
                print("Order data get successfully!")
            elif choice == "6":
                order_loop_menu = False
            else:
                print("Invalid choice")