from pydantic import BaseModel
from datetime import datetime


class Expense(BaseModel):
    date: datetime
    amount: float
    category: str
    description: str
