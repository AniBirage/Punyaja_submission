from sqlalchemy.orm import Session
from . import models, schemas

def create_finance_data(db: Session, data: schemas.FinanceDataCreate):
    db_data = models.FinanceData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_finance_data(db: Session):
    return db.query(models.FinanceData).all()

def delete_finance_data(db: Session, data_id: int):
    db_data = db.query(models.FinanceData).filter(models.FinanceData.id == data_id).first()
    if db_data:
        db.delete(db_data)
        db.commit()
    return db_data
