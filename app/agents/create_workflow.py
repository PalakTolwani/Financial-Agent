from langgraph.graph import END, StateGraph, START
from nodes.routing_nodes import (
    web_search,
    retrieve,
    grade_documents,
    generate,
    transform_query,
)

def create_workflow():
    """Create and compile the routing workflow."""
    workflow = StateGraph()

    # Define the nodes
    workflow.add_node("web_search", web_search)
    workflow.add_node("retrieve", retrieve)
    workflow.add_node("grade_documents", grade_documents)
    workflow.add_node("generate", generate)
    workflow.add_node("transform_query", transform_query)

    # Build the graph
    workflow.add_conditional_edges(
        START,
        lambda state: "web_search" if "search" in state else "retrieve",
        {
            "web_search": "web_search",
            "retrieve": "retrieve",
        },
    )
    workflow.add_edge("web_search", "generate")
    workflow.add_edge("retrieve", "grade_documents")
    workflow.add_conditional_edges(
        "grade_documents",
        lambda state: "transform_query" if "retry" in state else "generate",
        {
            "transform_query": "transform_query",
            "generate": "generate",
        },
    )
    workflow.add_edge("transform_query", "retrieve")
    workflow.add_edge("generate", END)

    # Compile and return the workflow
    return workflow.compile()
