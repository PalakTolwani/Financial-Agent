def grade_retrieved_docs(state):
    """
    Grades retrieved documents based on relevance to the query.
    """
    query = state["question"]
    retrieved_docs = state.get("retrieved_docs", [])

    # Simple grading based on document content relevance
    graded_docs = sorted(
        retrieved_docs,
        key=lambda doc: query in doc["content"],
        reverse=True
    )

    state["graded_docs"] = graded_docs[:3]  # Return top 3
    return state
