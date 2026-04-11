from urllib import response

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent, AgentState
from chatboat.comman_util import CommanUtil
from chatboat.model import Model
comman_util = CommanUtil()


InMemorySaver= InMemorySaver()
class CustomAgentState(AgentState):
    user_id: str
    preferences: dict

class ChatMemory:
    def __init__(self):
        self.messages = []
        self.model = Model().get_model("gemini")

    def send_message(self, prompt):
        # Create short-term memory
        agent = create_agent(
            "gpt-5",
            tools=[],
            state_schema=CustomAgentState,
            checkpointer=InMemorySaver,
        )
        response = agent.invoke(
            {
                "messages": [{"role": "user", "content": prompt}],
                "user_id": "user_123",
                "preferences": {"theme": "dark"}
            },
            {"configurable": {"thread_id": "1"}})
        result=comman_util.proceesed_response(response)
        return result