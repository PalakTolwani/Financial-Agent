# run or execute the budgeting agent

from nodes.budget_nodes import calculate_budget, calculate_savings
from states.state_management import validate_state

class BudgetingAgent:
    def run(self, state):
        """
        Run the budgeting workflow.

        Args:
            state (dict): The initial workflow state.

        Returns:
            dict: Updated state after executing the workflow.
        """
        # Validate the state
        validate_state(state)

        # Calculate budget and savings
        state = calculate_budget(state)
        state = calculate_savings(state)

        return state
