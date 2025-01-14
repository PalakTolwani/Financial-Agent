# loan/prompt.py
from langchain.prompts import PromptTemplate

loan_prompt = PromptTemplate(
    template="""You are a loan advisor assisting the user with their loan inquiries. \n
    Here is the user's query: {question}\n
    Provide a detailed response regarding the loan options, eligibility, and best advice.""",
    input_variables=["question"],
)
