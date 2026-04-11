from chatboat.model import Model
from tools.tools_collection import Tools

from langchain.agents import create_agent
from langchain.messages import HumanMessage, SystemMessage, AIMessage
from chatboat.comman_util import CommanUtil

comman_util = CommanUtil()
model = Model()
tools_model = Tools()

class ChatBoatMultiTools:
    def __init__(self, tools):
        self.tools = tools
        self.model=model.get_model("gemini")

    def send_message(self, prompt):
        # Implement logic to process the prompt and utilize the tools as needed
        # For example, you can check for specific keywords in the prompt to determine which tool to use
        tools=[tools_model.search, tools_model.get_city_wheather, tools_model.suggest_clothing]
        agent=create_agent(self.model, 
                            tools=tools,
                            system_prompt="You are a helpful assistant that can use tools to answer questions.",
                            )

        agent_response = agent.invoke({
            "messages": [HumanMessage(content=prompt)]  
        })  
        result=comman_util.proceesed_response(agent_response)
        
        return result