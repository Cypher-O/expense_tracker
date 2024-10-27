# expense_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, controllers, utils
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/expenses/", response_model=schemas.ResponseModel)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = controllers.create_expense(db=db, expense=expense)
    return utils.create_response(
        code=0,
        status="success",
        message="Expense created successfully",
        data=[db_expense]
    )

@router.get("/expenses/", response_model=schemas.ResponseModel)
def read_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    expenses = controllers.get_expenses(db=db, skip=skip, limit=limit)
    return utils.create_response(
        code=0,
        status="success",
        message="Expenses retrieved successfully",
        data=expenses
    )

@router.get("/expenses/{expense_id}", response_model=schemas.ResponseModel)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = controllers.get_expense(db=db, expense_id=expense_id)
    return utils.create_response(
        code=0,
        status="success",
        message="Expense retrieved successfully",
        data=[expense]
    )

@router.delete("/expenses/{expense_id}", response_model=schemas.ResponseModel)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = controllers.delete_expense(db=db, expense_id=expense_id)
    return utils.create_response(
        code=0,
        status="success",
        message="Expense deleted successfully",
        data=[expense]
    )