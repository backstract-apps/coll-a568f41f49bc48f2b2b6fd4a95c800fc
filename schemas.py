from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    username: Optional[str]=None
    email: Optional[str]=None
    password_hash: Optional[str]=None
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    status: Optional[str]=None
    is_admin: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[Any]=None
    updated_at: Optional[Any]=None


class ReadUsers(BaseModel):
    username: Optional[str]=None
    email: Optional[str]=None
    password_hash: Optional[str]=None
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    status: Optional[str]=None
    is_admin: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[Any]=None
    updated_at: Optional[Any]=None
    class Config:
        from_attributes = True


class Manufacturers(BaseModel):
    name: Optional[str]=None
    website_url: Optional[str]=None
    support_phone: Optional[str]=None
    notes: Optional[str]=None
    is_active: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[Any]=None
    updated_at: Optional[Any]=None


class ReadManufacturers(BaseModel):
    name: Optional[str]=None
    website_url: Optional[str]=None
    support_phone: Optional[str]=None
    notes: Optional[str]=None
    is_active: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[Any]=None
    updated_at: Optional[Any]=None
    class Config:
        from_attributes = True


class Owners(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    phone_number: Optional[str]=None
    department: Optional[str]=None
    location: Optional[str]=None
    is_active: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[Any]=None
    updated_at: Optional[Any]=None


class ReadOwners(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    phone_number: Optional[str]=None
    department: Optional[str]=None
    location: Optional[str]=None
    is_active: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[Any]=None
    updated_at: Optional[Any]=None
    class Config:
        from_attributes = True


class Laptops(BaseModel):
    manufacturer_id: Optional[int]=None
    owner_id: Optional[int]=None
    created_by: Optional[int]=None
    updated_by: Optional[int]=None
    serial_number: Optional[str]=None
    asset_tag: Optional[str]=None
    model_name: Optional[str]=None
    cpu_details: Optional[str]=None
    ram_gb: Optional[int]=None
    storage_size_gb: Optional[int]=None
    storage_type: Optional[str]=None
    purchase_date: Optional[datetime.date]=None
    purchase_price: Optional[float]=None
    warranty_end_date: Optional[datetime.date]=None
    status: Optional[str]=None
    notes: Optional[str]=None
    is_encrypted: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[Any]=None
    updated_at: Optional[Any]=None
    deleted_at: Optional[Any]=None


class ReadLaptops(BaseModel):
    manufacturer_id: Optional[int]=None
    owner_id: Optional[int]=None
    created_by: Optional[int]=None
    updated_by: Optional[int]=None
    serial_number: Optional[str]=None
    asset_tag: Optional[str]=None
    model_name: Optional[str]=None
    cpu_details: Optional[str]=None
    ram_gb: Optional[int]=None
    storage_size_gb: Optional[int]=None
    storage_type: Optional[str]=None
    purchase_date: Optional[datetime.date]=None
    purchase_price: Optional[float]=None
    warranty_end_date: Optional[datetime.date]=None
    status: Optional[str]=None
    notes: Optional[str]=None
    is_encrypted: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[Any]=None
    updated_at: Optional[Any]=None
    deleted_at: Optional[Any]=None
    class Config:
        from_attributes = True


class Repairs(BaseModel):
    laptop_id: Optional[int]=None
    technician_user_id: Optional[int]=None
    created_by: Optional[int]=None
    updated_by: Optional[int]=None
    repair_date: Optional[Any]=None
    issue_summary: Optional[str]=None
    description: Optional[str]=None
    repair_cost: Optional[float]=None
    status: Optional[str]=None
    invoice_url: Optional[str]=None
    is_deleted: Optional[int]=None
    created_at: Optional[Any]=None
    updated_at: Optional[Any]=None


class ReadRepairs(BaseModel):
    laptop_id: Optional[int]=None
    technician_user_id: Optional[int]=None
    created_by: Optional[int]=None
    updated_by: Optional[int]=None
    repair_date: Optional[Any]=None
    issue_summary: Optional[str]=None
    description: Optional[str]=None
    repair_cost: Optional[float]=None
    status: Optional[str]=None
    invoice_url: Optional[str]=None
    is_deleted: Optional[int]=None
    created_at: Optional[Any]=None
    updated_at: Optional[Any]=None
    class Config:
        from_attributes = True




class PostOwners(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    phone_number: Optional[str]=None
    department: Optional[str]=None
    location: Optional[str]=None
    is_active: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[str]=None
    updated_at: Optional[str]=None

    class Config:
        from_attributes = True



class PutOwnersId(BaseModel):
    id: Optional[int]=None
    full_name: Optional[str]=None
    email: Optional[str]=None
    phone_number: Optional[str]=None
    department: Optional[str]=None
    location: Optional[str]=None
    is_active: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[str]=None
    updated_at: Optional[str]=None

    class Config:
        from_attributes = True



class PostRepairs(BaseModel):
    laptop_id: Optional[int]=None
    technician_user_id: Optional[int]=None
    created_by: Optional[int]=None
    updated_by: Optional[int]=None
    repair_date: Optional[str]=None
    issue_summary: Optional[str]=None
    description: Optional[str]=None
    repair_cost: Optional[Any]=None
    status: Optional[str]=None
    invoice_url: Optional[str]=None
    is_deleted: Optional[int]=None
    created_at: Optional[str]=None
    updated_at: Optional[str]=None

    class Config:
        from_attributes = True



class PostManufacturers(BaseModel):
    name: Optional[str]=None
    website_url: Optional[str]=None
    support_phone: Optional[str]=None
    notes: Optional[str]=None
    is_active: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[str]=None
    updated_at: Optional[str]=None

    class Config:
        from_attributes = True



class PutManufacturersId(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    website_url: Optional[str]=None
    support_phone: Optional[str]=None
    notes: Optional[str]=None
    is_active: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[str]=None
    updated_at: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    username: Optional[str]=None
    email: Optional[str]=None
    password_hash: Optional[str]=None
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    status: Optional[str]=None
    is_admin: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[str]=None
    updated_at: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: Optional[int]=None
    username: Optional[str]=None
    email: Optional[str]=None
    password_hash: Optional[str]=None
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    status: Optional[str]=None
    is_admin: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[str]=None
    updated_at: Optional[str]=None

    class Config:
        from_attributes = True



class PostLaptops(BaseModel):
    manufacturer_id: Optional[int]=None
    owner_id: Optional[int]=None
    created_by: Optional[int]=None
    updated_by: Optional[int]=None
    serial_number: Optional[str]=None
    asset_tag: Optional[str]=None
    model_name: Optional[str]=None
    cpu_details: Optional[str]=None
    ram_gb: Optional[int]=None
    storage_size_gb: Optional[int]=None
    storage_type: Optional[str]=None
    purchase_date: Optional[Any]=None
    purchase_price: Optional[Any]=None
    warranty_end_date: Optional[Any]=None
    status: Optional[str]=None
    notes: Optional[str]=None
    is_encrypted: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[str]=None
    updated_at: Optional[str]=None
    deleted_at: Optional[str]=None

    class Config:
        from_attributes = True



class PutLaptopsId(BaseModel):
    id: Optional[int]=None
    manufacturer_id: Optional[int]=None
    owner_id: Optional[int]=None
    created_by: Optional[int]=None
    updated_by: Optional[int]=None
    serial_number: Optional[str]=None
    asset_tag: Optional[str]=None
    model_name: Optional[str]=None
    cpu_details: Optional[str]=None
    ram_gb: Optional[int]=None
    storage_size_gb: Optional[int]=None
    storage_type: Optional[str]=None
    purchase_date: Optional[Any]=None
    purchase_price: Optional[Any]=None
    warranty_end_date: Optional[Any]=None
    status: Optional[str]=None
    notes: Optional[str]=None
    is_encrypted: Optional[int]=None
    is_deleted: Optional[int]=None
    created_at: Optional[str]=None
    updated_at: Optional[str]=None
    deleted_at: Optional[str]=None

    class Config:
        from_attributes = True



class PutRepairsId(BaseModel):
    id: Optional[int]=None
    laptop_id: Optional[int]=None
    technician_user_id: Optional[int]=None
    created_by: Optional[int]=None
    updated_by: Optional[int]=None
    repair_date: Optional[str]=None
    issue_summary: Optional[str]=None
    description: Optional[str]=None
    repair_cost: Optional[Any]=None
    status: Optional[str]=None
    invoice_url: Optional[str]=None
    is_deleted: Optional[int]=None
    created_at: Optional[str]=None
    updated_at: Optional[str]=None

    class Config:
        from_attributes = True

