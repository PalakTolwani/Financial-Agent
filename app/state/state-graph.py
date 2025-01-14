from typing import List
from pydantic import basemodel
from typing_extensions import TypedDict


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        documents: list of documents
        errors: errorrs defined in each stage of the application based on different senarios such llm key, token expire, etc
    """

    question: str
    generation: str
    documents: List[str]
    error: list[str]