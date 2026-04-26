from agents.agent_builder import build_agent

def main():
    agent = build_agent()

    while True:
        query = input("\nAsk something (or 'exit'): ")

        if query.lower() == "exit":
            break

        response = agent.invoke({"input": query})
        print("\nResponse:", response["output"])

if __name__ == "__main__":
    main()