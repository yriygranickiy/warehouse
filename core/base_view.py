import time
from abc import abstractmethod, ABC
from datetime import datetime
from random import random
from typing import TypeVar

from core.base_service import EmployeeService, CategoryService, OrderService, ProductService, SupplierService, \
    WarehouseService
from core.models import Employee, Category, Order, Product, Suppliers, Warehouse, WarehouseTransaction

T = TypeVar('T')


class BaseView(ABC):

    @abstractmethod
    def get_view_all(self):
        ...
class EmployeeView(BaseView):
    def __init__(self, service: EmployeeService):
        self.service = service

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
                phone = int(input("Enter your phone number: "))
                employee = Employee(first_name=first_name,
                                    last_name=last_name,
                                    position="staff",
                                    email=email,
                                    phone=phone)
                print("Employee adding....")
                self.service.create(employee)
                time.sleep(0.3)
                print("Employee add successfully!")
            elif choice == "2":
                print("Input employee id for deleting")
                employee_id = int(input("Enter employee id: "))
                print("Deleting employee...")
                time.sleep(0.3)
                self.service.delete(employee_id)
                print("Employee delete successfully!")
            elif choice == "3":
                print("Input employee id for update")
                employee_id = int(input("Enter employee id: "))
                employee = self.service.get_by_id(employee_id)
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
                    self.service.update(employee_id, update_employee)
            elif choice == "4":
                print("load list employee...")
                time.sleep(0.3)
                for employee in self.service.get_all():
                    print(employee)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                id_employee = input("Enter employee id: ")
                employee = self.service.get_by_id(id_employee)
                print("getting employee data...")
                time.sleep(0.3)
                print(employee)
                print("employee data get successfully!")
            elif choice == "6":
                employee_loop_menu = False
            else:
                print("Invalid choice")


class CategoryView(BaseView):
    def __init__(self, service: CategoryService):
        self.service = service

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
                self.service.create(created_category)
                print("Category add successfully!")
            elif choice == "2":
                category_id = int(input("Enter category id: "))
                print("Deleting category...")
                time.sleep(0.3)
                self.service.delete(category_id)
                print("Category delete successfully!")
            elif choice == "3":
                print("Input category id for update...")
                category_id = int(input("Enter category id: "))
                category = self.service.get_by_id(category_id)
                print(f'Category: {category}')
                updated_category = category
                update_loop = True
                while update_loop:
                    print("Update Category:\n")
                    print("1. Update name category")
                    print("2. Update description category")
                    print("3. Exit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        print("Update category name")
                        category_name = input("Enter name: ")
                        updated_category.name = category_name
                    elif choice == "2":
                        print("Update category description")
                        description = input("Enter description: ")
                        updated_category.description = description
                    elif choice == "3":
                        update_loop = False
                    else:
                        print("Invalid choice")
                    self.service.update(category_id, updated_category)
            elif choice == "4":
                print("Load list category...")
                time.sleep(0.3)
                for category in self.service.get_all():
                    print(category)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                category_id = int(input("Enter category id: "))
                category = self.service.get_by_id(category_id)
                print("Getting category data...")
                time.sleep(0.3)
                print(category)
                print("category data get successfully!")
            elif choice == "6":
                category_loop_menu = False
            else:
                print("Invalid choice")


class OrderView(BaseView):
    def __init__(self, service: OrderService):
        self.service = service

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
                self.service.create(order)
                print("Order add successfully!")
            elif choice == "2":
                order_id = int(input("Enter order id: "))
                print("Deleting order...")
                self.service.delete(order_id)
                time.sleep(0.3)
                print("Order delete successfully!")
            elif choice == "3":
                print("Input order id for update...")
                order_id = int(input("Enter order id: "))
                order = self.service.get_by_id(order_id)
                print(f'Order: {order}')
                updated_order = order
                update_loop = True
                while update_loop:
                    print("Update Order:")
                    print("1. Update quantity")
                    print("2. Update order state")
                    print("3. Exit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        quantity = int(input("Enter quantity: "))
                        updated_order.quantity = quantity
                    elif choice == "2":
                        order_state = input("Enter order state: ")
                        updated_order.order_state = order_state
                    elif choice == "3":
                        update_loop = False
                    else:
                        print("Invalid choice")
                    self.service.update(order_id, updated_order)
            elif choice == "4":
                print("Load list order...")
                for order in self.service.get_all():
                    print(order)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                order_id = int(input("Enter order id: "))
                order = self.service.get_by_id(order_id)
                print("Getting order data...")
                time.sleep(0.3)
                print(order)
                print("Order data get successfully!")
            elif choice == "6":
                order_loop_menu = False
            else:
                print("Invalid choice")


class ProductView(BaseView):
    def __init__(self, service: ProductService):
        self.service = service

    def get_view_all(self):
        product_loop_menu = True
        while product_loop_menu:
            print("\nProduct:\n")
            print("1. Add")
            print("2. Delete")
            print("3. Update")
            print("4. Get all")
            print("5. Get product with details")
            print("6. Get product by id")
            print("7. Exit")
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
                                  category_id=1,
                                  supplier_id=1)
                print("Product adding....")
                time.sleep(0.3)
                self.service.create(product)
                print("Product add successfully!")
            elif choice == "2":
                product_id = int(input("Enter product id: "))
                print("Deleting product...")
                self.service.delete(product_id)
                print("Product delete successfully!")
            elif choice == "3":
                print("Input product id for update...")
                product_id = int(input("Enter product id: "))
                product = self.service.get_by_id(product_id)
                print(f'Product: {product}')
                updated_product = product
                update_loop = True
                while update_loop:
                    print("Update Product:")
                    print("1. Update name product")
                    print("2. Update quantity product")
                    print("3. Update price product")
                    print("4. Update description product")
                    print("5. Exit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        product_name = input("Enter product name: ")
                        updated_product.product_name = product_name
                    elif choice == "2":
                        quantity = int(input("Enter quantity: "))
                        updated_product.quantity = quantity
                    elif choice == "3":
                        price = float(input("Enter price: "))
                        updated_product.price = price
                    elif choice == "4":
                        description = input("Enter description: ")
                        updated_product.description = description
                    elif choice == "5":
                        update_loop = False
                    else:
                        print("Invalid choice")
                    self.service.update(product_id, updated_product)
            elif choice == "4":
                print("Load list product...")
                for product in self.service.get_all():
                    print(product)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                print("Load list product with details...")
                for product in self.service.get_product_with_details():
                    print('f----------------------------------------\n'
                          f'Product name: {product.product_name}\n'
                          f'Product quantity: {product.quantity}\n'
                          f'Product price: {product.price}\n'
                          f'Product date created: {product.created_date}\n'
                          f'Product category:{product.category.category_name}\n'
                          f'Suppliers name: {product.suppliers.supplier_name}\n'
                          f'Suppliers location: {product.suppliers.address}\n'
                          f'Suppliers phone: {product.suppliers.phone}\n'
                          f'Suppliers email: {product.suppliers.email}\n')
                    time.sleep(0.3)
                print("List load successfully!")
            elif choice == "6":
                product_id = int(input("Enter product id: "))
                print("Getting product data...")
                time.sleep(0.3)
                product = self.service.get_by_id(product_id)
                print(product)
                print("Getting product data...")
            elif choice == "7":
                product_loop_menu = False
            else:
                print("Invalid choice")


class SuppliersView(BaseView):
    def __init__(self, service: SupplierService):
        self.service = service

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
                self.service.create(supplier)
                print("Supplier add successfully!")
            elif choice == "2":
                supplier_id = int(input("Enter supplier id: "))
                print("Deleting supplier...")
                time.sleep(0.3)
                self.service.delete(supplier_id)
                print("Supplier delete successfully!")
            elif choice == "3":
                print("Input supplier id for update...")
                supplier_id = int(input("Enter supplier id: "))
                supplier = self.service.get_by_id(supplier_id)
                updated_supplier = supplier
                update_loop = True
                while update_loop:
                    print("Update Supplier:")
                    print("1. Update name supplier")
                    print("2. Update contact supplier")
                    print("3. Update phone")
                    print("4. Update email")
                    print("5. Update address")
                    print("6. Exit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        supplier_name = input("Enter supplier name: ")
                        updated_supplier.supplier_name = supplier_name
                    elif choice == "2":
                        contact_person = input("Enter contact person: ")
                        updated_supplier.contact_person = contact_person
                    elif choice == "3":
                        phone = input("Enter phone number: ")
                        updated_supplier.phone = phone
                    elif choice == "4":
                        email = input("Enter email address: ")
                        updated_supplier.email = email
                    elif choice == "5":
                        address = input("Enter address: ")
                        updated_supplier.address = address
                    elif choice == "6":
                        update_loop = False
                    else:
                        print("Invalid choice")
                    self.service.update(supplier_id, updated_supplier)
            elif choice == "4":
                print("Load list supplier...")
                for supplier in self.service.get_all():
                    print(supplier)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                supplier_id = int(input("Enter supplier id: "))
                print("Getting supplier data...")
                supplier = self.service.get_by_id(supplier_id)
                time.sleep(0.3)
                print(supplier)
                print("Getting supplier data...")
            elif choice == "6":
                supplier_loop_menu = False
            else:
                print("Invalid choice")


class WarehouseView(BaseView):
    def __init__(self, service: WarehouseService):
        self.service = service

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
                self.service.create(warehouse)
                print("Warehouse add successfully!")
            elif choice == "2":
                warehouse_id = int(input("Enter warehouse id: "))
                print("Deleting warehouse...")
                time.sleep(0.3)
                self.service.delete(warehouse_id)
                print("Warehouse delete successfully!")
            elif choice == "3":
                print("Input warehouse id for update...")
                warehouse_id = int(input("Enter warehouse id: "))
                warehouse = self.service.get_by_id(warehouse_id)
                updated_warehouse = warehouse
                update_loop = True
                while update_loop:
                    print("Update warehouse...")
                    print("1. Update name warehouse")
                    print("2. Update location warehouse")
                    print("3. Exit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        warehouse_name = input("Enter warehouse name: ")
                        updated_warehouse.warehouse_name = warehouse_name
                    elif choice == "2":
                        location = input("Enter location: ")
                        updated_warehouse.location = location
                    elif choice == "3":
                        update_loop = False
                    else:
                        print("Invalid choice")
                    self.service.update(warehouse_id, updated_warehouse)
            elif choice == "4":
                print("Load list warehouse...")
                for warehouse in self.service.get_all():
                    print(warehouse)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                warehouse_id = int(input("Enter warehouse id: "))
                print("Getting warehouse data...")
                time.sleep(0.3)
                print(self.service.get_by_id(warehouse_id))
                print("Getting warehouse data...")
            elif choice == "6":
                warehouse_loop_menu = False
            else:
                print("Invalid choice")


class TransactionView(BaseView):
    def __init__(self, service):
        self.service = service

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
                self.service.create(transaction)
                print("Transaction add successfully!")
            elif choice == "2":
                transaction_id = int(input("Enter transaction id: "))
                print("Deleting transaction...")
                time.sleep(0.3)
                self.service.delete(transaction_id)
                print("Transaction delete successfully!")
            elif choice == "3":
                print("Input transaction id for update...")
                transaction_id = int(input("Enter transaction id: "))
                transaction = self.service.get_by_id(transaction_id)
                updated_transaction = transaction
                update_loop = True
                while update_loop:
                    print("Update transaction...")
                    print("1. Update quantity")
                    print("2. Update type")
                    print("3. Update comment")
                    print("4. Exit")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        quantity = int(input("Enter quantity: "))
                        updated_transaction.quantity = quantity
                    elif choice == "2":
                        comment = input("Enter comment: ")
                        updated_transaction.comment = comment
                    elif choice == "3":
                        type = input("Enter type: ")
                        updated_transaction.type = type
                    elif choice == "4":
                        update_loop = False
                    else:
                        print("Invalid choice")
                    self.service.update(transaction_id, updated_transaction)
            elif choice == "4":
                print("Load list transaction...")
                for transaction in self.service.get_all():
                    print(transaction)
                    time.sleep(0.3)
                print("list load successfully!")
            elif choice == "5":
                transaction_id = int(input("Enter transaction id: "))
                print("Getting transaction data...")
                time.sleep(0.3)
                print(self.service.get_by_id(transaction_id))
                print("Getting transaction data...")
            elif choice == "6":
                transaction_loop_menu = False
            else:
                print("Invalid choice")
