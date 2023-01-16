from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///../booker.db')
Base = declarative_base()


class Rate(Base):
    __tablename__ = 'rates'
    employee_id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    rate = Column(Integer, nullable=False)

    Employee = relationship('Employee')


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    status = Column(Integer, nullable=False, default=1)
    position_id = Column(Integer, ForeignKey('positions.id'))
    payment = Column(Integer, nullable=False)

    Position = relationship('Position')
    Rate = relationship('Rate')


class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    Employee = relationship('Employee')


class ProductDetails(Base):
    __tablename__ = 'products_details'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    detail_id = Column(Integer, ForeignKey('details.id'), nullable=False)
    operation_id = Column(Integer, ForeignKey('operations.id'), nullable=False)
    cost = Column(Integer, nullable=False)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(Text)


class Detail(Base):
    __tablename__ = 'details'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(Text)


class Operation(Base):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(Text)


Base.metadata.create_all(engine)
