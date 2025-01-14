# budgeting/prompt.py
from langchain.prompts import PromptTemplate

budgeting_prompt = PromptTemplate(
    template="""You are a financial advisor helping the user with budgeting. \n
    Here is the user's query: {question}\n
    Provide actionable advice on how they can manage their budget effectively.""",
    input_variables=["question"],
)
