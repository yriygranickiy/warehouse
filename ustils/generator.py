import random

from faker import Faker

from core.models import Employee, Category, Suppliers, Product, Warehouse, Order, WarehouseTransaction

fake = Faker()

def generate_employee(num_info):

    list_info= []

    list_position= ['manager','admin','cleaner','loader',"staff"]

    for _ in range(num_info):
        employee = Employee(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            phone = fake.phone_number(),
            position= random.choice(list_position)
        )
        list_info.append(employee)

    return list_info

def generate_category(num_info):
    list_category= []

    for _ in range(num_info):
        category = Category(
            category_name = fake.word(),
            description = fake.text(),
        )
        list_category.append(category)

    return list_category

def generate_suppliers(num_info):
    list_suppliers=[]

    for _ in range(num_info):
        suppliers = Suppliers(
            supplier_name = fake.name(),
            contact_person= fake.word(),
            phone = fake.phone_number(),
            address = fake.address(),
            email = fake.email(),
        )

        list_suppliers.append(suppliers)

    return list_suppliers

def generate_product(num_info):
    list_product=[]

    for _ in range(num_info):
        product = Product(
            product_name = fake.word(),
            quantity = random.randint(1,100),
            price = random.randint(1,50),
            description = fake.text(),
            created_date= fake.date(pattern='%Y-%m-%d'),
            category_id = random.randint(1,20),
            supplier_id = random.randint(1,10)
        )

        list_product.append(product)

    return list_product

def generate_warehouse(num_info):
    list_warehouse=[]

    for _ in range(num_info):
        warehouse = Warehouse(
            warehouse_name = fake.name(),
            location = fake.address(),
        )
        list_warehouse.append(warehouse)

    return list_warehouse

def generate_order(num_info):
    list_order=[]

    order_status = [
        'Pending',
        'Processing',
        'Delivering',
        'Delivered',
    ]

    for _ in range(num_info):
        order = Order(
            quantity = random.randint(1,100),
            order_date = fake.date(pattern='%Y-%m-%d'),
            order_state=random.choice(order_status),
            product_id = random.randint(5,23),
        )
        list_order.append(order)

    return list_order

def generate_warehouse_transaction(num_info):
    list_warehouse_transaction=[]

    transaction_type = [
        'purchase', 'refund', 'transfer', 'withdrawal', 'deposit'
    ]

    for _ in range(num_info):
        wearhouse_transaction = WarehouseTransaction(
            quantity = random.randint(1,100),
            transaction_date = fake.date(pattern='%Y-%m-%d'),
            transaction_type= random.choice(transaction_type),
            comment= fake.text(),
            product_id = random.randint(5,23),
            employee_id=random.randint(1,23),
            warehouse_id=random.randint(1,5),
        )

        list_warehouse_transaction.append(wearhouse_transaction)

    return list_warehouse_transaction