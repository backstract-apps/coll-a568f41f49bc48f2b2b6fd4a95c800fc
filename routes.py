from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/owners/')
async def post_owners(raw_data: schemas.PostOwners, db: Session = Depends(get_db)):
    try:
        return await service.post_owners(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/owners/id/')
async def put_owners_id(raw_data: schemas.PutOwnersId, db: Session = Depends(get_db)):
    try:
        return await service.put_owners_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/owners/id/')
async def delete_owners_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_owners_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/repairs/')
async def post_repairs(raw_data: schemas.PostRepairs, db: Session = Depends(get_db)):
    try:
        return await service.post_repairs(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/repairs/id/')
async def delete_repairs_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_repairs_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/manufacturers/id/')
async def get_manufacturers_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_manufacturers_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/manufacturers/')
async def post_manufacturers(raw_data: schemas.PostManufacturers, db: Session = Depends(get_db)):
    try:
        return await service.post_manufacturers(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/manufacturers/id/')
async def put_manufacturers_id(raw_data: schemas.PutManufacturersId, db: Session = Depends(get_db)):
    try:
        return await service.put_manufacturers_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/manufacturers/id/')
async def delete_manufacturers_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_manufacturers_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/repairs/')
async def get_repairs(db: Session = Depends(get_db)):
    try:
        return await service.get_repairs(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id/')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/laptops/')
async def post_laptops(raw_data: schemas.PostLaptops, db: Session = Depends(get_db)):
    try:
        return await service.post_laptops(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/laptops/id/')
async def put_laptops_id(raw_data: schemas.PutLaptopsId, db: Session = Depends(get_db)):
    try:
        return await service.put_laptops_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/laptops/id/')
async def delete_laptops_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_laptops_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/manufacturers/')
async def get_manufacturers(db: Session = Depends(get_db)):
    try:
        return await service.get_manufacturers(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/owners/id/')
async def get_owners_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_owners_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/repairs/id/')
async def get_repairs_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_repairs_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/laptops/id/')
async def get_laptops_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_laptops_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/laptops/')
async def get_laptops(db: Session = Depends(get_db)):
    try:
        return await service.get_laptops(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id/')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/repairs/id/')
async def put_repairs_id(raw_data: schemas.PutRepairsId, db: Session = Depends(get_db)):
    try:
        return await service.put_repairs_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/owners/')
async def get_owners(db: Session = Depends(get_db)):
    try:
        return await service.get_owners(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

