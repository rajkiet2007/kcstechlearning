from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
from chatboat.model import Model

model=Model()

class Chatbot:
    def __init__(self):
        self.model=model.get_model("gemini")

    def send_message(self, prompt):
       model=self.model
       system_message=SystemMessage(content="You are a helpful assistant.")
       human_message=HumanMessage(content=prompt)
       message=[system_message, human_message]
       response=model.invoke(message)
       return response.content