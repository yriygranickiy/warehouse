import time
from abc import abstractmethod, ABC
from datetime import datetime, date
from random import random
from typing import TypeVar

from sqlalchemy import Transaction

from core.base_service import EmployeeService, CategoryService, OrderService, ProductService, SupplierService, \
    WarehouseService, WarehouseTransactionService
from core.models import Employee, Category, Order, Product, Suppliers, Warehouse, WarehouseTransaction

T = TypeVar('T')

class BaseView:

    def __init__(self,service):
        self.service = service

    def show_menu(self,entity_name, options):
        print(f"\n{entity_name}\n")
        for key,option in options.items():
            print(f"{key}. {option}")
        return input("Enter your choice: ")

    def handler_create(self,data:T):
        try:
            entity = data
            print("Adding entity...")
            time.sleep(0.3)
            self.service.create(entity)
            print("Entity added successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def handler_delete(self):
        try:
            entity_id = int(input("Enter id: "))
            print("Deleting entity...")
            time.sleep(0.3)
            self.service.delete(entity_id)
            print("Entity deleted successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def handler_get_all(self):
        try:
            print("load data ...")
            time.sleep(0.3)
            for entity in self.service.get_all():
                print(entity)
                time.sleep(0.3)
            print("list load successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def handler_get_by_id(self):
        try:
            entity_id = int(int(input("Enter id: ")))
            print("Get entity by id...")
            time.sleep(0.3)
            entity = self.service.get_by_id(entity_id)
            print(entity)
            print("Get entity by id successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def handler_update_entity(self,update_function):
        try:

            entity_id = int(input("Enter id: "))

            entity = self.service.get_by_id(entity_id)

            if not entity:
                print("No such entity exists!")

                return

            print(f'Entity: {entity}')

            updated_entity = update_function(entity)

            print("Updating entity...")

            time.sleep(0.3)

            self.service.update(entity_id, updated_entity)

        except Exception as e:
            print(f"Error: {e}")

class EmployeeView(BaseView):
    def __init__(self, service: EmployeeService):
        super().__init__(service)

    def get_view_all(self):
        options = {
            "1": "Add employee",
            "2": "Delete employee",
            "3": "Update employee",
            "4": "Get all employee",
            "5": "Get employee by id",
            "6": "Exit"
        }

        while True:
            choice = self.show_menu("Employee",options)
            if choice == "1":
              self.handler_create(self._create_employee())
            elif choice == "2":
               self.handler_delete()
            elif choice == "3":
              self.handler_update_entity(self._update_employee)
            elif choice == "4":
                self.handler_get_all()
            elif choice == "5":
               self.handler_get_by_id()
            elif choice == "6":
                break
            else:
                print("Invalid choice")

    def _create_employee(self):
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")
        phone = int(input("Enter your phone number: "))
        return Employee(first_name= first_name,
                        last_name= last_name,
                        position = "staff",
                        email= email,
                        phone= phone)

    def _update_employee(self, employee: Employee):
        options = {
            "1": "Update first name",
            "2": "Update last name",
            "3": "Update Email",
            "4": "Update Phone Number",
            "5": "Update Position",
            "6": "Exit"
        }
        while True:

            choice = self.show_menu("Update employee menu",options)
            if choice == "1":
                employee.first_name = input("Enter your first name: ")
            elif choice == "2":
                employee.last_name = input("Enter your last name: ")
            elif choice == "3":
                employee.email = input("Enter your email: ")
            elif choice == "4":
                employee.phone = input("Enter your phone number: ")
            elif choice == "5":
                employee.position = input("Enter your position: ")
            elif choice == "6":
                break
            else:
                print("Invalid choice")

        return employee

class CategoryView(BaseView):

    def __init__(self, service: CategoryService):
        super().__init__(service)

    def get_view_all(self):
        options = {
            "1": "Add category",
            "2": "Delete category",
            "3": "Update category",
            "4": "Get all category",
            "5": "Get category by id",
            "6": "Exit"
        }
        while True:
            choice = self.show_menu("Category",options)
            if choice == "1":
                self.handler_create(self._create_category())
            elif choice == "2":
                self.handler_delete()
            elif choice == "3":
                self.handler_update_entity(self._update_category)
            elif choice == "4":
                self.handler_get_all()
            elif choice == "5":
                self.handler_delete()
            elif choice == "6":
                break
            else:
                print("Invalid choice")

    def _create_category(self):
        category_name = input("Enter category title: ")
        description = input("Enter description: ")
        return Category(category_name = category_name,
                        description = description)

    def _update_category(self, category: Category):
        options = {
            "1": "Update category title",
            "2": "Update description",
            "3": "Exit"
        }
        while True:

            choice = self.show_menu("Update category menu",options)

            if choice == "1":
                category.category_name = input("Enter category title: ")
            elif choice == "2":
                category.description = input("Enter description: ")
            elif choice == "3":
                break
            else:
                print("Invalid choice")
        return category

class OrderView(BaseView):

    def __init__(self, service: OrderService):
        super().__init__(service)

    def get_view_all(self):

        options = {
            "1": "Add order",
            "2": "Delete order",
            "3": "Update order",
            "4": "Get all order",
            "5": "Get order by id",
            "6": "Exit"
        }

        while True:
            choice = self.show_menu("Order",options)

            if choice == "1":
                self.handler_create(self._create_order())
            elif choice == "2":
                self.handler_delete()
            elif choice == "3":
                self.handler_update_entity(self._update_order)
            elif choice == "4":
                self.handler_get_all()
            elif choice == "5":
                self.handler_get_by_id()
            elif choice == "6":
                break
            else:
                print("Invalid choice")

    def _create_order(self):
        quantity = int(input("Enter quantity: "))
        order_state = "processing"
        product_id = input("Enter product id: ")
        if not product_id:
            print("Invalid product id")
            return

        return Order(quantity=quantity,
                     order_state = order_state,
                     product_id = product_id)

    def _update_order(self, order: Order):

        options = {
            "1": "Update quantity",
            "2": "Update sate",
            "3": "Update product number",
            "4": "Exit"
        }

        while True:
            choice = self.show_menu("Update order menu",options)

            if choice == "1":
                order.quantity = input("Enter quantity: ")
            elif choice == "2":
                order.order_state = input("Enter state: ")
            elif choice == "3":
                order.product_id = input("Enter product number: ")
            elif choice == "4":
                break
            else:
                print("Invalid choice")

        return order

class ProductView(BaseView):

    def __init__(self, service: ProductService):
        super().__init__(service)

    def get_view_all(self):
        options = {
            "1": "Add product",
            "2": "Delete product",
            "3": "Update product",
            "4": "Get all product",
            "5": "Get product with details",
            "6": "Get product by id",
            "7": "Exit"
        }

        while True:
            choice = self.show_menu("Product",options)
            if choice == "1":
                self.handler_create(self._create_product())
            elif choice == "2":
                self.handler_delete()
            elif choice == "3":
                self.handler_update_entity(self._update_product)
            elif choice == "4":
               self.handler_get_all()
            elif choice == "5":
                self._get_product_with_details()
            elif choice == "6":
              self.handler_get_by_id()
            elif choice == "7":
                break
            else:
                print("Invalid choice")

    def _create_product(self):
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        description = input("Enter description: ")
        category = input("Enter category: ")
        supplier = input("Enter supplier: ")

        return Product(product_name = product_name,
                       quantity = quantity,
                       price=price,
                       description=description,
                       category_id=category,
                       supplier_id = supplier)

    def _update_product(self, product: Product):
        options = {
            "1": "Update title product",
            "2": "Update quantity product",
            "3": "Update price product",
            "4": "Update description product",
            "5": "Update category product",
            "6": "Update supplier product",
            "7": "Exit"
        }

        while True:
            choice = self.show_menu("Update product menu",options)
            if choice == "1":
                product.product_name = input("Enter product title: ")
            elif choice == "2":
                product.quantity = input("Enter product quantity: ")
            elif choice == "3":
                product.price = input("Enter product price: ")
            elif choice == "4":
                product.description = input("Enter product description: ")
            elif choice == "5":
                product.category_id = input("Enter product category number: ")
            elif choice == "6":
                product.supplier_id = input("Enter product supplier number: ")
            elif choice == "7":
                break
            else:
                print("Invalid choice")
        return product

    def _get_product_with_details(self):
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

class SuppliersView(BaseView):
    def __init__(self, service: SupplierService):
        super().__init__(service)

    def get_view_all(self):
        options = {
            "1": "Add supplier",
            "2": "Delete supplier",
            "3": "Update supplier",
            "4": "Get all supplier",
            "5": "Get by id supplier",
            "6": "Exit"
        }
        while True:
            choice = self.show_menu("Suppliers",options)

            if choice == "1":
                self.handler_create(self._create_supplier())
            elif choice == "2":
                self.handler_delete()
            elif choice == "3":
                self.handler_update_entity(self._update_supplier)
            elif choice == "4":
                self.handler_get_all()
            elif choice == "5":
                self.handler_get_by_id()
            elif choice == "6":
                break
            else:
                print("Invalid choice")

    def _create_supplier(self):
        supplier_name = input("Enter supplier name: ")
        contact_person = input("Enter contact persot: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        return Suppliers(supplier_name = supplier_name,
                         contact_person = contact_person,
                         phone=phone_number,
                         email=email,
                         address=address)

    def _update_supplier(self, supplier):
        options = {
            "1": "Update supplier name",
            "2": "Update supplier contact person",
            "3": "Update supplier phone number",
            "4": "Update supplier email",
            "5": "Update supplier address",
            "6": "Exit"
        }
        while True:
            choice = self.show_menu("Update supplier menu",options)
            if choice == "1":
                supplier.supplier_name = input("Enter supplier name: ")
            elif choice == "2":
                supplier.contact_person = input("Enter contact person: ")
            elif choice == "3":
                supplier.phone_number = input("Enter phone number: ")
            elif choice == "4":
                supplier.email = input("Enter email: ")
            elif choice == "5":
                supplier.address = input("Enter address: ")
            elif choice == "6":
                break
            else:
                print("Invalid choice")
        return supplier

class WarehouseView(BaseView):
    def __init__(self, service: WarehouseService):
        super().__init__(service)

    def get_view_all(self):

        options = {
            "1": "Add warehouse",
            "2": "Delete warehouse",
            "3": "Update warehouse",
            "4": "Get all warehouse",
            "5": "Get by id warehouse",
            "6": "Exit"
        }

        while True:
            choice = self.show_menu("Warehouse",options)
            if choice == "1":
                self.handler_create(self._create_warehouse())
            elif choice == "2":
                self.handler_delete()
            elif choice == "3":
                self.handler_update_entity(self._update_warehouse)
            elif choice == "4":
                self.handler_get_all()
            elif choice == "5":
                self.handler_get_by_id()
            elif choice == "6":
                break
            else:
                print("Invalid choice")

    def _create_warehouse(self):
        warehouse_title = input("Enter warehouse title: ")
        warehouse_address = input("Enter warehouse address: ")

        return Warehouse(warehouse_name=warehouse_title,
                         location=warehouse_address)

    def _update_warehouse(self, warehouse):
        options = {
            "1": "Update warehouse title",
            "2": "Update warehouse address",
            "3": "Exit"
        }
        while True:
            choice = self.show_menu("Update warehouse menu",options)
            if choice == "1":
                warehouse.warehouse_name = input("Enter warehouse title: ")
            elif choice == "2":
                warehouse.location = input("Enter warehouse address: ")
            elif choice == "3":
                break
            else:
                print("Invalid choice")
        return warehouse

class TransactionView(BaseView):

    def __init__(self, service:WarehouseTransactionService):
        super().__init__(service)

    def get_view_all(self):

        options = {
            "1": "Add transaction",
            "2": "Delete transaction",
            "3": "Update transaction",
            "4": "Get all transaction",
            "5": "Get by id transaction",
            "6": "Exit"
        }
        while True:
            choice = self.show_menu("Transaction",options)
            if choice == "1":
                self.handler_create(self._create_transaction())
            elif choice == "2":
               self.handler_delete()
            elif choice == "3":
                self.handler_update_entity(self._update_transaction)
            elif choice == "4":
                self.handler_get_all()
            elif choice == "5":
                self.handler_get_by_id()
            elif choice == "6":
                break
            else:
                print("Invalid choice")


    def _create_transaction(self):
        quantity = input("Enter quantity: ")
        transaction_type = input("Enter type transaction: ")
        comment = input("Enter comment: ")
        product = input("Enter product: ")
        employee = input("Enter employee: ")
        warehouse = input("Enter warehouse: ")

        return WarehouseTransaction(quantity = quantity,
                                    transaction_type = transaction_type,
                                    comment=comment,
                                    product_id = product,
                                    employee_id = employee,
                                    warehouse_id = warehouse)

    def _update_transaction(self, transaction):
        options = {
            "1": "Update quantity",
            "2": "Update transaction type",
            "3": "Update comment to transaction",
            "4": "Update product number",
            "5": "Update employee number",
            "6": "Update warehouse number",
            "7": "Exit"
        }
        while True:
            choice = self.show_menu("Update transaction menu",options)
            if choice == "1":
                transaction.quantity = input("Enter quantity: ")
            elif choice == "2":
                transaction.transaction_type = input("Enter transaction type: ")
            elif choice == "3":
                transaction.comment = input("Enter comment: ")
            elif choice == "4":
                transaction.product_id = input("Enter product number: ")
            elif choice == "5":
                transaction.employee_id = input("Enter employee number: ")
            elif choice == "6":
                transaction.warehouse_id = input("Enter warehouse number: ")
            elif choice == "7":
                break
            else:
                print("Invalid choice")
        return transaction

