class StateGraph:
    def __init__(self):
        self.state = "INITIAL"

    def transition(self, event: str) -> str:
        """
        Transition the current state based on an event.
        """
        transitions = {
            "INITIAL": {"request_budget": "BUDGET", "retrieve_data": "RETRIEVER"},
            "BUDGET": {"grade_advice": "GRADING", "reset": "INITIAL"},
            "RETRIEVER": {"reset": "INITIAL"},
            "GRADING": {"reset": "INITIAL"}
        }

        if event in transitions[self.state]:
            self.state = transitions[self.state][event]
        else:
            raise ValueError(f"Invalid event: {event} for state: {self.state}")
        return self.state

# Example usage
state_graph = StateGraph()
print(state_graph.transition("request_budget"))  # Output: BUDGET
print(state_graph.transition("grade_advice"))    # Output: GRADING
