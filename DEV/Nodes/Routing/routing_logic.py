def route_request(user_input: str) -> str:
    """
    Routes the user's input to the appropriate node or function.
    """
    if "budget" in user_input.lower():
        return "Budget Advice Node"
    elif "grade" in user_input.lower():
        return "Grading Node"
    elif "retrieve" in user_input.lower():
        return "Retriever Node"
    else:
        return "Unknown Node"

# Example usage
node = route_request("How do I improve my budget?")
print(f"Routed to: {node}")
