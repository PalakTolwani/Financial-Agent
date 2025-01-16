# main.py
import logging
from Budgeting.budgeting_workflow import budgeting_workflow
from Loan.loan_workflow import loan_workflow
from Credit.credit_workflow import credit_workflow

logging.getLogger("prefect").setLevel(logging.CRITICAL)

def handle_query(query):
    state = {"messages": [{"content": query}]}

    if "budget" in query.lower():
        response = budgeting_workflow(state)  # Call the function here
    elif "loan" in query.lower():
        response = loan_workflow(state)
    elif "credit" in query.lower():
        response = credit_workflow(state)
    else:
        response = {"messages": [{"content": "I'm not sure about that."}]}

    return response

def main():
    print("Welcome to the Financial Agent Chatbot! ")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! Have a great day!")
            break
        
        response = handle_query(user_input)
        print(f"Bot: {response['messages'][0]['content']}")


if __name__ == "__main__":
    main()
