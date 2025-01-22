def generate_budget_prompt(income: float, expenses: float, items: str) -> str:
    """
    Generate a concise budget prompt for Hugging Face models.
    """
    return f"""
    You are an AI financial advisor. Based on the following budget details, provide actionable advice.

    Income: ${income}
    Expenses: ${expenses}
    Items:
    {items}

    What are your suggestions to improve the user's financial management?
    """
