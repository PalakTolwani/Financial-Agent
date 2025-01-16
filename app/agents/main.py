from agents.create_workflow import create_workflow

def main():
    print("Welcome to the Financial Agent Chatbot! Type 'exit' to quit.")
    workflow = create_workflow()

    while True:
        query = input("You: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break

        # Example state for demonstration
        state = {"query": query}
        response = workflow.run(state)
        print(f"Bot: {response.get('generated_response', 'No response generated')}")

if __name__ == "__main__":
    main()
