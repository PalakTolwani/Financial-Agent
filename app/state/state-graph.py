from typing import List, Dict
from pydantic import BaseModel
from typing_extensions import TypedDict


class BudgetState(TypedDict):
    """
    Represents the state of the budgeting workflow.

    Attributes:
        budget: Total budget defined by the user.
        expenses: A list of expenses with descriptions and amounts.
        savings: Remaining savings after deducting expenses from the budget.
        errors: List of error messages encountered during processing.
    """
    budget: float
    expenses: List[Dict[str, float]]  # Each expense has 'description' and 'amount'.
    savings: float
    errors: List[str]
