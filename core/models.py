
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
        return f'<Employee {self.first_name} {self.last_name} {self.email} {self.phone} {self.position}>'


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)

    product = relationship('Product', back_populates='category')

    def __repr__(self):
        return f'<Category {self.category_name} {self.description}>'


class Suppliers(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_name = Column(String(50), nullable=False)
    contact_person = Column(String(70), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(70), nullable=False)
    address = Column(Text, nullable=False)

    product = relationship("Product", back_populates="suppliers")
    order = relationship("Order", back_populates="suppliers")

    def __repr__(self):
        return f'<Suppliers {self.supplier_name} {self.contact_person} {self.phone} {self.address} {self.email}>'


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
    order = relationship('Order', back_populates='product')

    def __repr__(self):
        return f'<Product {self.product_name} {self.quantity} {self.price} {self.description}>'


class Warehouse(Base):
    __tablename__ = 'warehouse'

    id = Column(Integer, primary_key=True, autoincrement=True)
    warehouse_name = Column(String(50), nullable=False)
    location = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<Warehouse {self.warehouse_name} {self.location}>'


class WarehouseTransaction(Base):
    __tablename__ = 'warehouse_transaction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Float, nullable=False)
    transaction_type = Column(String(50), nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    comment = Column(Text, nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)

    product = relationship('Product', back_populates='warehouse_transaction')
    employee = relationship('Employee', back_populates='warehouse_transaction')

    def __repr__(self):
        return f'<Warehouse_transaction {self.quantity} {self.transaction_type} {self.transaction_date} {self.comment}>'


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    order_date = Column(DateTime, nullable=False)
    order_state = Column(String(50), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)

    suppliers = relationship('Suppliers', back_populates='order')
    product = relationship('Product', back_populates='order')

    def __repr__(self):
        return f'<Order {self.quantity} {self.order_date} {self.order_state}>'
