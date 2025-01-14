# credit/agent.py
from langchain_huggingface import HuggingFaceEndpoint

class CreditAgent:
    def __init__(self, model_id="meta-llama/Llama-3.2-3B-Instruct"):
        self.model = HuggingFaceEndpoint(
            repo_id=model_id,
            task="text_generation",
            max_new_tokens=512,
            temperature=0.3,
            streaming=True,
        )

    def process_credit_query(self, state):
        """
        Process the user query related to credit.
        Args:
            state (dict): The current state containing user messages.
        """
        messages = state["messages"]
        question = messages[0].content

        response = self.model.invoke([{"content": question}])
        return {"messages": [response]}
