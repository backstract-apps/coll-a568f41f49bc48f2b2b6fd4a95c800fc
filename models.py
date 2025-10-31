from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID, LargeBinary, text, Interval
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True )
    username = Column(String, primary_key=False )
    email = Column(String, primary_key=False )
    password_hash = Column(String, primary_key=False )
    first_name = Column(String, primary_key=False )
    last_name = Column(String, primary_key=False )
    status = Column(String, primary_key=False )
    is_admin = Column(Integer, primary_key=False )
    is_deleted = Column(Integer, primary_key=False )
    created_at = Column(DateTime, primary_key=False )
    updated_at = Column(DateTime, primary_key=False )


class Manufacturers(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True, autoincrement=True )
    name = Column(String, primary_key=False )
    website_url = Column(String, primary_key=False )
    support_phone = Column(String, primary_key=False )
    notes = Column(String, primary_key=False )
    is_active = Column(Integer, primary_key=False )
    is_deleted = Column(Integer, primary_key=False )
    created_at = Column(DateTime, primary_key=False )
    updated_at = Column(DateTime, primary_key=False )


class Owners(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True, autoincrement=True )
    full_name = Column(String, primary_key=False )
    email = Column(String, primary_key=False )
    phone_number = Column(String, primary_key=False )
    department = Column(String, primary_key=False )
    location = Column(String, primary_key=False )
    is_active = Column(Integer, primary_key=False )
    is_deleted = Column(Integer, primary_key=False )
    created_at = Column(DateTime, primary_key=False )
    updated_at = Column(DateTime, primary_key=False )


class Laptops(Base):
    __tablename__ = 'laptops'
    id = Column(Integer, primary_key=True, autoincrement=True )
    manufacturer_id = Column(Integer, primary_key=False )
    owner_id = Column(Integer, primary_key=False )
    created_by = Column(Integer, primary_key=False )
    updated_by = Column(Integer, primary_key=False )
    serial_number = Column(String, primary_key=False )
    asset_tag = Column(String, primary_key=False )
    model_name = Column(String, primary_key=False )
    cpu_details = Column(String, primary_key=False )
    ram_gb = Column(Integer, primary_key=False )
    storage_size_gb = Column(Integer, primary_key=False )
    storage_type = Column(String, primary_key=False )
    purchase_date = Column(Date, primary_key=False )
    purchase_price = Column(Float, primary_key=False )
    warranty_end_date = Column(Date, primary_key=False )
    status = Column(String, primary_key=False )
    notes = Column(String, primary_key=False )
    is_encrypted = Column(Integer, primary_key=False )
    is_deleted = Column(Integer, primary_key=False )
    created_at = Column(DateTime, primary_key=False )
    updated_at = Column(DateTime, primary_key=False )
    deleted_at = Column(DateTime, primary_key=False )


class Repairs(Base):
    __tablename__ = 'repairs'
    id = Column(Integer, primary_key=True, autoincrement=True )
    laptop_id = Column(Integer, primary_key=False )
    technician_user_id = Column(Integer, primary_key=False )
    created_by = Column(Integer, primary_key=False )
    updated_by = Column(Integer, primary_key=False )
    repair_date = Column(DateTime, primary_key=False )
    issue_summary = Column(String, primary_key=False )
    description = Column(String, primary_key=False )
    repair_cost = Column(Float, primary_key=False )
    status = Column(String, primary_key=False )
    invoice_url = Column(String, primary_key=False )
    is_deleted = Column(Integer, primary_key=False )
    created_at = Column(DateTime, primary_key=False )
    updated_at = Column(DateTime, primary_key=False )


