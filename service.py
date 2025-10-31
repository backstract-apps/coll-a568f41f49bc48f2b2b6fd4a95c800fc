from sqlalchemy.orm import Session, aliased
from database import SessionLocal
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
from datetime import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


def convert_to_datetime(date_string):
    if "T" in date_string:
        try:
            return datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        except ValueError:
            date_part = date_string.split("T")[0]
            try:
                return datetime.strptime(date_part, "%Y-%m-%d")
            except ValueError:
                return None
    else:
        try:
            return datetime.strptime(date_string, "%Y-%m-%d")
        except ValueError:
            return None


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_all": users_all},
    }
    return res


async def post_owners(db: Session, raw_data: schemas.PostOwners):
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    phone_number: str = raw_data.phone_number
    department: str = raw_data.department
    location: str = raw_data.location
    is_active: int = raw_data.is_active
    is_deleted: int = raw_data.is_deleted
    created_at: str = convert_to_datetime(raw_data.created_at)
    updated_at: str = convert_to_datetime(raw_data.updated_at)

    record_to_be_added = {
        "email": email,
        "location": location,
        "full_name": full_name,
        "is_active": is_active,
        "created_at": created_at,
        "department": department,
        "is_deleted": is_deleted,
        "updated_at": updated_at,
        "phone_number": phone_number,
    }
    new_owners = models.Owners(**record_to_be_added)
    db.add(new_owners)
    db.commit()
    db.refresh(new_owners)
    owners_inserted_record = new_owners.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"owners_inserted_record": owners_inserted_record},
    }
    return res


async def put_owners_id(db: Session, raw_data: schemas.PutOwnersId):
    id: int = raw_data.id
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    phone_number: str = raw_data.phone_number
    department: str = raw_data.department
    location: str = raw_data.location
    is_active: int = raw_data.is_active
    is_deleted: int = raw_data.is_deleted
    created_at: str = convert_to_datetime(raw_data.created_at)
    updated_at: str = convert_to_datetime(raw_data.updated_at)

    query = db.query(models.Owners)
    query = query.filter(and_(models.Owners.id == id))
    owners_edited_record = query.first()

    if owners_edited_record:
        for key, value in {
            "id": id,
            "email": email,
            "location": location,
            "full_name": full_name,
            "is_active": is_active,
            "created_at": created_at,
            "department": department,
            "is_deleted": is_deleted,
            "updated_at": updated_at,
            "phone_number": phone_number,
        }.items():
            setattr(owners_edited_record, key, value)

        db.commit()
        db.refresh(owners_edited_record)

        owners_edited_record = (
            owners_edited_record.to_dict()
            if hasattr(owners_edited_record, "to_dict")
            else vars(owners_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"owners_edited_record": owners_edited_record},
    }
    return res


async def delete_owners_id(db: Session, id: int):

    query = db.query(models.Owners)
    query = query.filter(and_(models.Owners.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        owners_deleted = record_to_delete.to_dict()
    else:
        owners_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"owners_deleted": owners_deleted},
    }
    return res


async def post_repairs(db: Session, raw_data: schemas.PostRepairs):
    laptop_id: int = raw_data.laptop_id
    technician_user_id: int = raw_data.technician_user_id
    created_by: int = raw_data.created_by
    updated_by: int = raw_data.updated_by
    repair_date: str = convert_to_datetime(raw_data.repair_date)
    issue_summary: str = raw_data.issue_summary
    description: str = raw_data.description
    repair_cost: float = raw_data.repair_cost
    status: str = raw_data.status
    invoice_url: str = raw_data.invoice_url
    is_deleted: int = raw_data.is_deleted
    created_at: str = convert_to_datetime(raw_data.created_at)
    updated_at: str = convert_to_datetime(raw_data.updated_at)

    record_to_be_added = {
        "status": status,
        "laptop_id": laptop_id,
        "created_at": created_at,
        "created_by": created_by,
        "is_deleted": is_deleted,
        "updated_at": updated_at,
        "updated_by": updated_by,
        "description": description,
        "invoice_url": invoice_url,
        "repair_cost": repair_cost,
        "repair_date": repair_date,
        "issue_summary": issue_summary,
        "technician_user_id": technician_user_id,
    }
    new_repairs = models.Repairs(**record_to_be_added)
    db.add(new_repairs)
    db.commit()
    db.refresh(new_repairs)
    repairs_inserted_record = new_repairs.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"repairs_inserted_record": repairs_inserted_record},
    }
    return res


async def delete_repairs_id(db: Session, id: int):

    query = db.query(models.Repairs)
    query = query.filter(and_(models.Repairs.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        repairs_deleted = record_to_delete.to_dict()
    else:
        repairs_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"repairs_deleted": repairs_deleted},
    }
    return res


async def get_manufacturers_id(db: Session, id: int):

    query = db.query(models.Manufacturers)
    query = query.filter(and_(models.Manufacturers.id == id))

    manufacturers_one = query.first()

    manufacturers_one = (
        (
            manufacturers_one.to_dict()
            if hasattr(manufacturers_one, "to_dict")
            else vars(manufacturers_one)
        )
        if manufacturers_one
        else manufacturers_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"manufacturers_one": manufacturers_one},
    }
    return res


async def post_manufacturers(db: Session, raw_data: schemas.PostManufacturers):
    name: str = raw_data.name
    website_url: str = raw_data.website_url
    support_phone: str = raw_data.support_phone
    notes: str = raw_data.notes
    is_active: int = raw_data.is_active
    is_deleted: int = raw_data.is_deleted
    created_at: str = convert_to_datetime(raw_data.created_at)
    updated_at: str = convert_to_datetime(raw_data.updated_at)

    record_to_be_added = {
        "name": name,
        "notes": notes,
        "is_active": is_active,
        "created_at": created_at,
        "is_deleted": is_deleted,
        "updated_at": updated_at,
        "website_url": website_url,
        "support_phone": support_phone,
    }
    new_manufacturers = models.Manufacturers(**record_to_be_added)
    db.add(new_manufacturers)
    db.commit()
    db.refresh(new_manufacturers)
    manufacturers_inserted_record = new_manufacturers.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"manufacturers_inserted_record": manufacturers_inserted_record},
    }
    return res


async def put_manufacturers_id(db: Session, raw_data: schemas.PutManufacturersId):
    id: int = raw_data.id
    name: str = raw_data.name
    website_url: str = raw_data.website_url
    support_phone: str = raw_data.support_phone
    notes: str = raw_data.notes
    is_active: int = raw_data.is_active
    is_deleted: int = raw_data.is_deleted
    created_at: str = convert_to_datetime(raw_data.created_at)
    updated_at: str = convert_to_datetime(raw_data.updated_at)

    query = db.query(models.Manufacturers)
    query = query.filter(and_(models.Manufacturers.id == id))
    manufacturers_edited_record = query.first()

    if manufacturers_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "notes": notes,
            "is_active": is_active,
            "created_at": created_at,
            "is_deleted": is_deleted,
            "updated_at": updated_at,
            "website_url": website_url,
            "support_phone": support_phone,
        }.items():
            setattr(manufacturers_edited_record, key, value)

        db.commit()
        db.refresh(manufacturers_edited_record)

        manufacturers_edited_record = (
            manufacturers_edited_record.to_dict()
            if hasattr(manufacturers_edited_record, "to_dict")
            else vars(manufacturers_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"manufacturers_edited_record": manufacturers_edited_record},
    }
    return res


async def delete_manufacturers_id(db: Session, id: int):

    query = db.query(models.Manufacturers)
    query = query.filter(and_(models.Manufacturers.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        manufacturers_deleted = record_to_delete.to_dict()
    else:
        manufacturers_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"manufacturers_deleted": manufacturers_deleted},
    }
    return res


async def get_repairs(db: Session):

    query = db.query(models.Repairs)

    repairs_all = query.all()
    repairs_all = (
        [new_data.to_dict() for new_data in repairs_all] if repairs_all else repairs_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"repairs_all": repairs_all},
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    username: str = raw_data.username
    email: str = raw_data.email
    password_hash: str = raw_data.password_hash
    first_name: str = raw_data.first_name
    last_name: str = raw_data.last_name
    status: str = raw_data.status
    is_admin: int = raw_data.is_admin
    is_deleted: int = raw_data.is_deleted
    created_at: str = convert_to_datetime(raw_data.created_at)
    updated_at: str = convert_to_datetime(raw_data.updated_at)

    record_to_be_added = {
        "email": email,
        "status": status,
        "is_admin": is_admin,
        "username": username,
        "last_name": last_name,
        "created_at": created_at,
        "first_name": first_name,
        "is_deleted": is_deleted,
        "updated_at": updated_at,
        "password_hash": password_hash,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_inserted_record": users_inserted_record},
    }
    return res


async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id: int = raw_data.id
    username: str = raw_data.username
    email: str = raw_data.email
    password_hash: str = raw_data.password_hash
    first_name: str = raw_data.first_name
    last_name: str = raw_data.last_name
    status: str = raw_data.status
    is_admin: int = raw_data.is_admin
    is_deleted: int = raw_data.is_deleted
    created_at: str = convert_to_datetime(raw_data.created_at)
    updated_at: str = convert_to_datetime(raw_data.updated_at)

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "email": email,
            "status": status,
            "is_admin": is_admin,
            "username": username,
            "last_name": last_name,
            "created_at": created_at,
            "first_name": first_name,
            "is_deleted": is_deleted,
            "updated_at": updated_at,
            "password_hash": password_hash,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_edited_record": users_edited_record},
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_deleted": users_deleted},
    }
    return res


async def post_laptops(db: Session, raw_data: schemas.PostLaptops):
    manufacturer_id: int = raw_data.manufacturer_id
    owner_id: int = raw_data.owner_id
    created_by: int = raw_data.created_by
    updated_by: int = raw_data.updated_by
    serial_number: str = raw_data.serial_number
    asset_tag: str = raw_data.asset_tag
    model_name: str = raw_data.model_name
    cpu_details: str = raw_data.cpu_details
    ram_gb: int = raw_data.ram_gb
    storage_size_gb: int = raw_data.storage_size_gb
    storage_type: str = raw_data.storage_type
    purchase_date: datetime.date = convert_to_datetime(raw_data.purchase_date)
    purchase_price: float = raw_data.purchase_price
    warranty_end_date: datetime.date = convert_to_datetime(raw_data.warranty_end_date)
    status: str = raw_data.status
    notes: str = raw_data.notes
    is_encrypted: int = raw_data.is_encrypted
    is_deleted: int = raw_data.is_deleted
    created_at: str = convert_to_datetime(raw_data.created_at)
    updated_at: str = convert_to_datetime(raw_data.updated_at)
    deleted_at: str = convert_to_datetime(raw_data.deleted_at)

    record_to_be_added = {
        "notes": notes,
        "ram_gb": ram_gb,
        "status": status,
        "owner_id": owner_id,
        "asset_tag": asset_tag,
        "created_at": created_at,
        "created_by": created_by,
        "deleted_at": deleted_at,
        "is_deleted": is_deleted,
        "model_name": model_name,
        "updated_at": updated_at,
        "updated_by": updated_by,
        "cpu_details": cpu_details,
        "is_encrypted": is_encrypted,
        "storage_type": storage_type,
        "purchase_date": purchase_date,
        "serial_number": serial_number,
        "purchase_price": purchase_price,
        "manufacturer_id": manufacturer_id,
        "storage_size_gb": storage_size_gb,
        "warranty_end_date": warranty_end_date,
    }
    new_laptops = models.Laptops(**record_to_be_added)
    db.add(new_laptops)
    db.commit()
    db.refresh(new_laptops)
    laptops_inserted_record = new_laptops.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"laptops_inserted_record": laptops_inserted_record},
    }
    return res


async def put_laptops_id(db: Session, raw_data: schemas.PutLaptopsId):
    id: int = raw_data.id
    manufacturer_id: int = raw_data.manufacturer_id
    owner_id: int = raw_data.owner_id
    created_by: int = raw_data.created_by
    updated_by: int = raw_data.updated_by
    serial_number: str = raw_data.serial_number
    asset_tag: str = raw_data.asset_tag
    model_name: str = raw_data.model_name
    cpu_details: str = raw_data.cpu_details
    ram_gb: int = raw_data.ram_gb
    storage_size_gb: int = raw_data.storage_size_gb
    storage_type: str = raw_data.storage_type
    purchase_date: datetime.date = convert_to_datetime(raw_data.purchase_date)
    purchase_price: float = raw_data.purchase_price
    warranty_end_date: datetime.date = convert_to_datetime(raw_data.warranty_end_date)
    status: str = raw_data.status
    notes: str = raw_data.notes
    is_encrypted: int = raw_data.is_encrypted
    is_deleted: int = raw_data.is_deleted
    created_at: str = convert_to_datetime(raw_data.created_at)
    updated_at: str = convert_to_datetime(raw_data.updated_at)
    deleted_at: str = convert_to_datetime(raw_data.deleted_at)

    query = db.query(models.Laptops)
    query = query.filter(and_(models.Laptops.id == id))
    laptops_edited_record = query.first()

    if laptops_edited_record:
        for key, value in {
            "id": id,
            "notes": notes,
            "ram_gb": ram_gb,
            "status": status,
            "owner_id": owner_id,
            "asset_tag": asset_tag,
            "created_at": created_at,
            "created_by": created_by,
            "deleted_at": deleted_at,
            "is_deleted": is_deleted,
            "model_name": model_name,
            "updated_at": updated_at,
            "updated_by": updated_by,
            "cpu_details": cpu_details,
            "is_encrypted": is_encrypted,
            "storage_type": storage_type,
            "purchase_date": purchase_date,
            "serial_number": serial_number,
            "purchase_price": purchase_price,
            "manufacturer_id": manufacturer_id,
            "storage_size_gb": storage_size_gb,
            "warranty_end_date": warranty_end_date,
        }.items():
            setattr(laptops_edited_record, key, value)

        db.commit()
        db.refresh(laptops_edited_record)

        laptops_edited_record = (
            laptops_edited_record.to_dict()
            if hasattr(laptops_edited_record, "to_dict")
            else vars(laptops_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"laptops_edited_record": laptops_edited_record},
    }
    return res


async def delete_laptops_id(db: Session, id: int):

    query = db.query(models.Laptops)
    query = query.filter(and_(models.Laptops.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        laptops_deleted = record_to_delete.to_dict()
    else:
        laptops_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"laptops_deleted": laptops_deleted},
    }
    return res


async def get_manufacturers(db: Session):

    query = db.query(models.Manufacturers)

    manufacturers_all = query.all()
    manufacturers_all = (
        [new_data.to_dict() for new_data in manufacturers_all]
        if manufacturers_all
        else manufacturers_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"manufacturers_all": manufacturers_all},
    }
    return res


async def get_owners_id(db: Session, id: int):

    query = db.query(models.Owners)
    query = query.filter(and_(models.Owners.id == id))

    owners_one = query.first()

    owners_one = (
        (owners_one.to_dict() if hasattr(owners_one, "to_dict") else vars(owners_one))
        if owners_one
        else owners_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"owners_one": owners_one},
    }
    return res


async def get_repairs_id(db: Session, id: int):

    query = db.query(models.Repairs)
    query = query.filter(and_(models.Repairs.id == id))

    repairs_one = query.first()

    repairs_one = (
        (
            repairs_one.to_dict()
            if hasattr(repairs_one, "to_dict")
            else vars(repairs_one)
        )
        if repairs_one
        else repairs_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"repairs_one": repairs_one},
    }
    return res


async def get_laptops_id(db: Session, id: int):

    query = db.query(models.Laptops)
    query = query.filter(and_(models.Laptops.id == id))

    laptops_one = query.first()

    laptops_one = (
        (
            laptops_one.to_dict()
            if hasattr(laptops_one, "to_dict")
            else vars(laptops_one)
        )
        if laptops_one
        else laptops_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"laptops_one": laptops_one},
    }
    return res


async def get_laptops(db: Session):

    query = db.query(models.Laptops)

    laptops_all = query.all()
    laptops_all = (
        [new_data.to_dict() for new_data in laptops_all] if laptops_all else laptops_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"laptops_all": laptops_all},
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_one": users_one},
    }
    return res


async def put_repairs_id(db: Session, raw_data: schemas.PutRepairsId):
    id: int = raw_data.id
    laptop_id: int = raw_data.laptop_id
    technician_user_id: int = raw_data.technician_user_id
    created_by: int = raw_data.created_by
    updated_by: int = raw_data.updated_by
    repair_date: str = convert_to_datetime(raw_data.repair_date)
    issue_summary: str = raw_data.issue_summary
    description: str = raw_data.description
    repair_cost: float = raw_data.repair_cost
    status: str = raw_data.status
    invoice_url: str = raw_data.invoice_url
    is_deleted: int = raw_data.is_deleted
    created_at: str = convert_to_datetime(raw_data.created_at)
    updated_at: str = convert_to_datetime(raw_data.updated_at)

    query = db.query(models.Repairs)
    query = query.filter(and_(models.Repairs.id == id))
    repairs_edited_record = query.first()

    if repairs_edited_record:
        for key, value in {
            "id": id,
            "status": status,
            "laptop_id": laptop_id,
            "created_at": created_at,
            "created_by": created_by,
            "is_deleted": is_deleted,
            "updated_at": updated_at,
            "updated_by": updated_by,
            "description": description,
            "invoice_url": invoice_url,
            "repair_cost": repair_cost,
            "repair_date": repair_date,
            "issue_summary": issue_summary,
            "technician_user_id": technician_user_id,
        }.items():
            setattr(repairs_edited_record, key, value)

        db.commit()
        db.refresh(repairs_edited_record)

        repairs_edited_record = (
            repairs_edited_record.to_dict()
            if hasattr(repairs_edited_record, "to_dict")
            else vars(repairs_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"repairs_edited_record": repairs_edited_record},
    }
    return res


async def get_owners(db: Session):

    query = db.query(models.Owners)

    owners_all = query.all()
    owners_all = (
        [new_data.to_dict() for new_data in owners_all] if owners_all else owners_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"owners_all": owners_all},
    }
    return res
