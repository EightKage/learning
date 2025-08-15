# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    make = Column(String)
    model = Column(String)
    engine = Column(String)

    fitments = relationship("Fitment", back_populates="vehicle")

class Part(Base):
    __tablename__ = "parts"
    id = Column(Integer, primary_key=True, index=True)
    oem_number = Column(String)
    name = Column(String)
    description = Column(String)
    brand = Column(String)
    image_url = Column(String)
    category = Column(String)

    fitments = relationship("Fitment", back_populates="part")
    inventory_items = relationship("Inventory", back_populates="part")

class Fitment(Base):
    __tablename__ = "fitments"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    part_id = Column(Integer, ForeignKey("parts.id"))

    vehicle = relationship("Vehicle", back_populates="fitments")
    part = relationship("Part", back_populates="fitments")

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    api_key = Column(String)
    region = Column(String)

    inventory_items = relationship("Inventory", back_populates="supplier")

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    part_id = Column(Integer, ForeignKey("parts.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    price = Column(Float)
    quantity = Column(Integer)
    currency = Column(String)

    part = relationship("Part", back_populates="inventory_items")
    supplier = relationship("Supplier", back_populates="inventory_items")
