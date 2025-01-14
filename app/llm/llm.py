from langchain_huggingface import HuggingFaceEndpoint


def __init__(self, model_id="meta-llama/Llama-3.2-3B-Instruct"):
    self.model = HuggingFaceEndpoint(
         repo_id=model_id,
        task="text_generation",
        max_new_tokens=512,
        temperature=0.3,
        streaming=True,
    )