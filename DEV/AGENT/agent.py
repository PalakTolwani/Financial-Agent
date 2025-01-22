from models.budget_models import BudgetDetails
from LLM.llm_handler import hf_model
from Nodes.Generate.generate_budget import generate_budget_prompt_with_validation

def get_budget_advice(data: BudgetDetails) -> str:
    """
    Generate budget advice using the Hugging Face model.
    """
    # Generate the validated prompt
    prompt = generate_budget_prompt_with_validation(data)
    
    # Use Hugging Face model to generate advice
    response = hf_model.generate_text(prompt)
    return response
