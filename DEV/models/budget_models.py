from pydantic import BaseModel, Field, validator
from typing import List

class BudgetItem(BaseModel):
    name: str
    amount: float = Field(..., gt=0, description="Amount must be greater than zero")
    category: str
    due_date: str = Field(None, description="Due date in YYYY-MM-DD format")

class BudgetDetails(BaseModel):
    income: float = Field(..., gt=0, description="Income must be greater than zero")
    expenses: float = Field(..., ge=0, description="Expenses cannot be negative")
    items: List[BudgetItem] = Field(..., description="List of budget items")

    @validator("expenses")
    def validate_expenses(cls, v, values):
        if "income" in values and v > values["income"]:
            raise ValueError("Expenses cannot exceed income")
        return v

    @property
    def remaining_budget(self) -> float:
        return self.income - self.expenses
