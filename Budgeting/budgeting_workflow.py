# Budgeting/budgeting_workflow.py
from prefect import task, flow

@task
def fetch_budget_data():
    # Placeholder for fetching budget data
    return {"budget": 5000, "expenses": 2000, "savings": 3000}

@task
def calculate_savings(data):
    savings = data["budget"] - data["expenses"]
    return savings

@flow
def budgeting_workflow(state):
    # This flow orchestrates the budgeting process
    budget_data = fetch_budget_data()
    savings = calculate_savings(budget_data)
    return {"messages": [{"content": f"Savings: {savings}"}]}
