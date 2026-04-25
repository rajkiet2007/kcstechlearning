from chatboat import comman_util
from chatboat.model import Model
from tools.tools_collection import Tools
from langchain.agents import create_agent
from langchain.messages import HumanMessage, SystemMessage, AIMessage
from chatboat.comman_util import CommanUtil

comman_util = CommanUtil()

model=Model()
tools=Tools()
class StreamingChatbot:
    def __init__(self):
        self.tools = tools
        self.model = Model().get_model("gemini")

    def stream_response(self, human_message):
        messages = [HumanMessage(content=human_message)]
        for chunk in self.model.stream(messages):
            print(chunk.content, end="", flush=True)

