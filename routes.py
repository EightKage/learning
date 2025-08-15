# app/api/routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/vehicles")
def get_vehicles(db: Session = Depends(get_db)):
    return db.query(models.Vehicle).all()
