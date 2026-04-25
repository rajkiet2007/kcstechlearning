from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from tools.tools_collection import Tools
from chatboat.model import Model
class ChatSummarizationMiddleware:
    def __init__(self, ):
        self.model = Model().get_model("gemini")

    def summarize(self):
        # Implement your summarization logic here using self.model
        # For example, you could use the model to generate a summary of the conversation history
        summary_llm = self.model
        middleware = [
        SummarizationMiddleware(
        model=summary_llm,
        trigger=("tokens", 200),   # low for demo
        keep=("messages", 5),
         )
        ]
        agent = create_agent(
            model=self.model,
            tools=[Tools().get_city_wheather, Tools().calculator],
            middleware=middleware,
        )
        inputs = {
            "messages": [
                {"role": "user", "content": "What is the weather in Delhi?"},
                {"role": "user", "content": "Now calculate 25 * 4"},
                {"role": "user", "content": "What is the weather in Mumbai?"},
                {"role": "user", "content": "Now calculate 100 / 5"},
                {"role": "user", "content": "What is the weather in Chennai?"},
            ]
        }
        print("\n--- Streaming Output ---\n")

        for chunk in agent.stream(inputs):
            print(chunk)
