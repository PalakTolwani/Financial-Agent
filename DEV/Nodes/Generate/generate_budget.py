from app.models.budget_models import BudgetDetails
from app.Prompt.budget_prompts import generate_budget_prompt

def generate_budget_prompt_with_validation(data: BudgetDetails) -> str:
    """
    Generate a prompt for the AI model using validated budget details.
    """
    formatted_items = "\n".join([f"{item.name}: ${item.amount}" for item in data.items])
    return generate_budget_prompt(data.income, data.expenses, formatted_items)
