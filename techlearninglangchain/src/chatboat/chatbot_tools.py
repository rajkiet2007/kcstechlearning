from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage
from tools.tools_collection import Tools
from chatboat.model import Model
from chatboat.comman_util import CommanUtil

comman_util = CommanUtil()

model=Model()
tools=Tools()
class ChatbotTools:
    def __init__(self):
        self.model=model.get_model("gemini")
        self.tools = {}
    def send_message(self, prompt):
        agent=create_agent(self.model, 
                           tools=[tools.search],
                           system_prompt="You are a helpful assistant that can use tools to answer questions.",
                           )
        human_message=HumanMessage(content=prompt)
        response = agent.invoke({
            "messages": [human_message]
        })
        result=comman_util.proceesed_response(response)
        # result=result['messages'][0][AIMessage].content
        return result 
    
