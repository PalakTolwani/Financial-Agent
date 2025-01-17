from create_workflow import app
from state_graph import BudgetState

def main():
    print("Welcome to the Enhanced Budgeting Agent! Type 'exit' to quit.")
    state = BudgetState(budget=5000.0, expenses=[], savings=0.0, errors=[])

    while True:
        query = input("Enter your query: ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        state["question"] = query
        state = app.run(START, state)

        response = state.get("graded_docs", [{"content": "No relevant documents found"}])
        print("Bot: Top results:")
        for idx, doc in enumerate(response, start=1):
            print(f"{idx}. {doc['content']}")

if __name__ == "__main__":
    main()
