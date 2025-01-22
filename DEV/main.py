from models.budget_models import BudgetDetails, BudgetItem
from AGENT.agent import get_budget_advice

# Sample budget details
items = [
    BudgetItem(name="Rent", amount=1500, category="Housing"),
    BudgetItem(name="Groceries", amount=500, category="Food"),
    BudgetItem(name="Utilities", amount=300, category="Bills"),
]

budget_data = BudgetDetails(income=5000, expenses=2300, items=items)

# Get budget advice
advice = get_budget_advice(budget_data)
print("AI Budget Advice:")
print(advice)
