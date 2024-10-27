# controllers/expense_controller.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import Expense
from ..schemas import ExpenseCreate

def get_expense(db: Session, expense_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

def get_expenses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Expense).offset(skip).limit(limit).all()

def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def delete_expense(db: Session, expense_id: int):
    db_expense = get_expense(db, expense_id)
    db.delete(db_expense)
    db.commit()
    return db_expense