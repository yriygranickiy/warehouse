import time
from abc import abstractmethod
from datetime import datetime
from random import random
from typing import Protocol

from core.base_service import EmployeeService, CategoryService, OrderService, ProductService, SupplierService, \
    WarehouseService
from core.models import Employee, Category, Order, Product, Suppliers, Warehouse, WarehouseTransaction


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
                print("Input employee id for update")
                employee_id = int(input("Enter employee id: "))
                employee = self.get_by_id(employee_id)
                print(f'Employee: {employee}')
                update_employee = employee
                update_loop = True
                while update_loop:
                    print("Update Employee:\n")
                    print("1. Update First Name")
                    print("2. Update Last name")
                    print("3. Update Email")
                    print("4. Update Phone Number")
                    print("5. Update Position")
                    print("6. Exit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        print("Update First Name")
                        first_name = input("Enter your first name: ")
                        update_employee.first_name = first_name
                    elif choice == "2":
                        print("Update Last name")
                        last_name = input("Enter your last name: ")
                        update_employee.last_name = last_name
                    elif choice == "3":
                        print("Update Email")
                        email = input("Enter your email: ")
                        update_employee.email = email
                    elif choice == "4":
                        print("Update Phone Number")
                        phone = input("Enter your phone number: ")
                        update_employee.phone = phone
                    elif choice == "5":
                        print("Update Position")
                        position = input("Enter your position: ")
                        update_employee.position = position
                    elif choice == "6":
                        print("Exit")
                        update_loop = False
                    else:
                        print("Invalid choice")
                    self.update(employee, employee_id, update_employee)
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

class ProductView(BaseView):
    def __init__(self, service:ProductService):
        super().__init__(service)

    def get_view_all(self):
        product_loop_menu = True
        while product_loop_menu:
            print("\nProduct:\n")
            print("\nProduct:\n")
            print("1. Add")
            print("2. Delete")
            print("3. Update")
            print("4. Get all")
            print("5. Get product by id")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                product_name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                description = input("Enter description: ")
                product = Product(product_name=product_name,
                                  quantity=quantity,
                                  price=price,
                                  description=description,
                                  created_date=datetime.now(),
                                  category_id=random.randint(2, 11),
                                  supplier_id=random.randint(2, 5))
                print("Product adding....")
                time.sleep(0.3)
                self.create(product)
                print("Product add successfully!")
            elif choice == "2":
                product_id = int(input("Enter product id: "))
                print("Deleting product...")
                self.delete(product_id)
                print("Product delete successfully!")
            elif choice == "3":
                pass
            elif choice == "4":
                print("Load list product...")
                for product in self.get_all():
                    print(product)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                product_id = int(input("Enter product id: "))
                print("Getting product data...")
                time.sleep(0.3)
                product = self.get_by_id(product_id)
                print(product)
                print("Getting product data...")
            elif choice == "6":
                product_loop_menu = False
            else:
                print("Invalid choice")

class SuppliersView(BaseView):
    def __init__(self, service:SupplierService):
        super().__init__(service)

    def get_view_all(self):
        supplier_loop_menu = True
        while supplier_loop_menu:
            print("\nSuppliers:\n")
            print("1. Add")
            print("2. Delete")
            print("3. Update")
            print("4. Get all")
            print("5. Get suppliers by id")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                supplier_name = input("Enter supplier name: ")
                contact_person = input("Enter contact person: ")
                phone = input("Enter phone number: ")
                email = input("Enter email address: ")
                address = input("Enter address: ")

                supplier = Suppliers(supplier_name=supplier_name,
                                     contact_person=contact_person,
                                     phone=phone,
                                     email=email,
                                     address=address)
                print("Supplier adding....")
                time.sleep(0.3)
                self.create(supplier)
                print("Supplier add successfully!")
            elif choice == "2":
                supplier_id = int(input("Enter supplier id: "))
                print("Deleting supplier...")
                time.sleep(0.3)
                self.delete(supplier_id)
                print("Supplier delete successfully!")
            elif choice == "3":
                pass
            elif choice == "4":
                print("Load list supplier...")
                for supplier in self.get_all():
                    print(supplier)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                supplier_id = int(input("Enter supplier id: "))
                print("Getting supplier data...")
                supplier = self.get_by_id(supplier_id)
                time.sleep(0.3)
                print(supplier)
                print("Getting supplier data...")
            elif choice == "6":
                supplier_loop_menu = False
            else:
                print("Invalid choice")

class WarehouseView(BaseView):
    def __init__(self, service:WarehouseService):
        super().__init__(service)

    def get_view_all(self):
        warehouse_loop_menu = True
        while warehouse_loop_menu:
            print("\nWarehouses:\n")
            print("1. Add")
            print("2. Delete")
            print("3. Update")
            print("4. Get all")
            print("5. Get warehouse by id")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                warehouse_name = input("Enter warehouse name: ")
                location = input("Enter location: ")

                warehouse = Warehouse(warehouse_name=warehouse_name,
                                      location=location)
                print("Warehouse adding....")
                time.sleep(0.3)
                self.create(warehouse)
                print("Warehouse add successfully!")
            elif choice == "2":
                warehouse_id = int(input("Enter warehouse id: "))
                print("Deleting warehouse...")
                time.sleep(0.3)
                self.delete(warehouse_id)
                print("Warehouse delete successfully!")
            elif choice == "3":
                pass
            elif choice == "4":
                print("Load list warehouse...")
                for warehouse in self.get_all():
                    print(warehouse)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                warehouse_id = int(input("Enter warehouse id: "))
                print("Getting warehouse data...")
                time.sleep(0.3)
                print(self.get_by_id(warehouse_id))
                print("Getting warehouse data...")
            elif choice == "6":
                warehouse_loop_menu = False
            else:
                print("Invalid choice")

class TransactionView(BaseView):
    def __init__(self, service):
        super().__init__(service)

    def get_view_all(self):
        transaction_loop_menu = True
        while transaction_loop_menu:
            print("\nTransactions:\n")
            print("1. Add")
            print("2. Delete")
            print("3. Update")
            print("4. Get all")
            print("5. Get transaction by id")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                quantity = int(input("Enter quantity: "))
                comment = input("Enter comment: ")
                transaction = WarehouseTransaction(quantity=quantity,
                                                   transaction_type='purchase',
                                                   transaction_date=datetime.now(),
                                                   comment=comment,
                                                   product_id=random.randint(2, 3),
                                                   employee_id=random.randint(1, 2),
                                                   warehouse_id=random.randint(1, 2))
                print("Transaction adding....")
                time.sleep(0.3)
                self.create(transaction)
                print("Transaction add successfully!")
            elif choice == "2":
                transaction_id = int(input("Enter transaction id: "))
                print("Deleting transaction...")
                time.sleep(0.3)
                self.delete(transaction_id)
                print("Transaction delete successfully!")
            elif choice == "3":
                pass
            elif choice == "4":
                print("Load list transaction...")
                for transaction in self.get_all():
                    print(transaction)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                transaction_id = int(input("Enter transaction id: "))
                print("Getting transaction data...")
                time.sleep(0.3)
                print(self.get_by_id(transaction_id))
                print("Getting transaction data...")
            elif choice == "6":
                transaction_loop_menu = False
            else:
                print("Invalid choice")