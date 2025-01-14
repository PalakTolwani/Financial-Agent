# Credit/credit_workflow.py
from prefect import task, flow

@task
def fetch_credit_data(state):
    # Simulated credit data
    return {"credit_id": state, "limit": 5000, "used": 1200}

@task
def calculate_remaining_credit(data):
    # Calculate remaining credit
    limit = data["limit"]
    used = data["used"]
    remaining_credit = limit - used
    return remaining_credit

@flow
def credit_workflow(state):
    credit_data = fetch_credit_data(state)
    remaining_credit = calculate_remaining_credit(credit_data)
    # Return in the expected format
    return {"messages": [{"content": f"Remaining credit amount is: {remaining_credit}"}]}
