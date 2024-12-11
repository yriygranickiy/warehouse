
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(70), nullable=False)
    position = Column(String(50), nullable=False)
    email = Column(String(70), nullable=False)
    phone = Column(String(50), nullable=False)

    warehouse_transaction = relationship("WarehouseTransaction", back_populates="employee")

    def __repr__(self):
        return (f'-------------\n'
                f'employee first name: {self.first_name}\n'
                f'employee last name: {self.last_name}\n'
                f'email: {self.email}\n'
                f'phone: {self.phone}\n'
                f'position: {self.position}\n'
                f'--------------')


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)

    product = relationship('Product', back_populates='category')

    def __repr__(self):
        return (f'------------\n'
                f'category name: {self.category_name}\n'
                f'description: {self.description}\n'
                f'------------\n')


class Suppliers(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_name = Column(String(50), nullable=False)
    contact_person = Column(String(70), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(70), nullable=False)
    address = Column(Text, nullable=False)

    product = relationship("Product", back_populates="suppliers")

    def __repr__(self):
        return (f'---------------\n'
                f'supplier name: {self.supplier_name}\n'
                f'supplier contact: {self.contact_person} \n'
                f'supplier phone: {self.phone} \n'
                f'supplier address: {self.address} \n'
                f'supplier email: {self.email}\n'
                f'---------------')

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    created_date = Column(DateTime, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)

    suppliers = relationship('Suppliers', back_populates='product')
    category = relationship('Category', back_populates='product')
    warehouse_transaction = relationship('WarehouseTransaction', back_populates='product')
    order = relationship('Order',back_populates='product')

    def __repr__(self):
        return (f'-------------\n'
                f'product name: {self.product_name}\n'
                f'quantity: {self.quantity}\n'
                f'price: {self.price}\n'
                f'created_date: {self.created_date}\n'
                f'description: {self.description}\n'
                f'--------------')


class Warehouse(Base):
    __tablename__ = 'warehouse'

    id = Column(Integer, primary_key=True, autoincrement=True)
    warehouse_name = Column(String(50), nullable=False)
    location = Column(String(50), nullable=False)

    warehouse_transaction = relationship('WarehouseTransaction', back_populates='warehouse')

    def __repr__(self):
        return (f'------------\n'
                f'Warehouse {self.warehouse_name}\n'
                f' {self.location}\n'
                f'--------------')


class WarehouseTransaction(Base):
    __tablename__ = 'warehouse_transaction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Float, nullable=False)
    transaction_type = Column(String(50), nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    comment = Column(Text, nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'), nullable=False)

    warehouse = relationship('Warehouse', back_populates='warehouse_transaction')
    product = relationship('Product', back_populates='warehouse_transaction')
    employee = relationship('Employee', back_populates='warehouse_transaction')

    def __repr__(self):
        return (f'------------\n'
                f'Warehouse_transaction\n '
                f'quantity: {self.quantity}\n'
                f'type: {self.transaction_type}\n'
                f'date: {self.transaction_date}\n'
                f'comment: {self.comment}\n'
                f'--------------')


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    order_date = Column(DateTime, nullable=False)
    order_state = Column(String(50), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)

    product = relationship('Product', back_populates='order')

    def __repr__(self):
        return (f'-----------\n'
                f'Order\n'
                f'quantity: {self.quantity}\n'
                f'date: {self.order_date}\n'
                f'state: {self.order_state}\n'
                f'-----------------')


