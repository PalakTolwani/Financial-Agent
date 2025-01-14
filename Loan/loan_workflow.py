# Loan/loan_workflow.py

from prefect import task, flow

# Define a Prefect task for loan data processing
@task
def fetch_loan_data(loan_id):
    # Placeholder for fetching loan data (could be from a database or API)
    loan_data = {"loan_id": loan_id, "amount": 10000, "interest_rate": 5.5}
    #print(f"Fetched loan data: {loan_data}")
    return loan_data

# Define a task to calculate loan repayment
@task
def calculate_repayment(loan_data):
    amount = loan_data["amount"]
    interest_rate = loan_data["interest_rate"]
    repayment = amount * (1 + interest_rate / 100)
    #print(f"Calculated repayment amount: {repayment}")
    return repayment

# Define a Prefect flow to tie tasks together
@flow
def loan_workflow(loan_id):
    loan_data = fetch_loan_data(loan_id)
    repayment = calculate_repayment(loan_data)
    #print(f"Final repayment for loan {loan_id}: {repayment}")
    return {"messages": [{"content": f"Loan repayment amount is: {repayment}"}]}

# Call the workflow in main block
if __name__ == "__main__":
    loan_workflow(12345)  # Pass a sample loan ID
