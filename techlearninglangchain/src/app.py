from chatboat.chatbot import Chatbot
from chatboat.chatbot_tools import ChatbotTools
from chatboat.chatbot_memory import ChatMemory

def chat():
    bot=Chatbot()
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        response=bot.send_message(user_input)
        print(f"Bot: {response[0]['text']}")
def chat_with_tools():
    bot=ChatbotTools()
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        response=bot.send_message(user_input)
        print(f"Bot: {response}")
        
def chat_with_multi_tools():
    from chatboat.chatboat_multi_tools import ChatBoatMultiTools
    bot=ChatBoatMultiTools(tools=None)
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        response=bot.send_message(user_input)
        print(f"Bot: {response}")
def chat_with_memory():
    
    bot=ChatMemory()
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        response=bot.send_message(user_input)
        print(f"Bot: {response}")   
        
if __name__ == "__main__":  
    # chat()
    # chat_with_tools()
    # chat_with_multi_tools()
    chat_with_memory()