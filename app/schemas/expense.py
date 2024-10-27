# schemas/expense.py
from pydantic import BaseModel
from typing import List, Optional

class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True

class ResponseModel(BaseModel):
    code: int
    status: str
    message: str
    data: Optional[List[Expense]] = None