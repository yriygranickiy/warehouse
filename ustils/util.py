import random

from faker import Faker

from core.models import Employee, Category, Suppliers, Product

fake = Faker()

def generate_employee(num_info):

    list_info= []

    for _ in range(num_info):
        employee = Employee(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            phone = fake.phone_number(),
            position= 'default',
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
            category_id = random.randint(32,41),
            supplier_id = random.randint(1,23),
        )

        list_product.append(product)

    return list_product