from transformers import pipeline

class HuggingFaceModel:
    def __init__(self, model_name: str = "tiiuae/falcon-7b-instruct", max_length: int = 512, temperature: float = 0.7):
        self.model = pipeline(
            "text-generation",
            model=model_name,
            max_length=max_length,
            temperature=temperature
        )

    def generate_text(self, prompt: str) -> str:
        response = self.model(prompt, num_return_sequences=1)
        return response[0]["generated_text"]

# Initialize the Hugging Face model
hf_model = HuggingFaceModel()
