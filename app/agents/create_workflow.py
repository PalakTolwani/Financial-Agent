from langgraph.graph import StateGraph, START, END
from states.state_graph import BudgetState
from nodes.hf_nodes import grade_retrieved_docs
from nodes.embedding_nodes import embed_and_retrieve

workflow = StateGraph(BudgetState)

# Nodes
workflow.add_node("embed_and_retrieve", embed_and_retrieve)
workflow.add_node("grade_retrieved_docs", grade_retrieved_docs)

# Edges
workflow.add_edge(START, "embed_and_retrieve")
workflow.add_edge("embed_and_retrieve", "grade_retrieved_docs")
workflow.add_edge("grade_retrieved_docs", END)

app = workflow.compile()
