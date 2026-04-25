from chatboat.chatbot import Chatbot
from chatboat.chatbot_tools import ChatbotTools
from chatboat.chatbot_memory import ChatMemory
from chatboat.chatbot_streaming import StreamingChatbot
from chatboat.chat_summarization_middkeware import ChatSummarizationMiddleware

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

def chat_streaming():
    
    bot=StreamingChatbot()
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        bot.stream_response(user_input)

def chat_json_format():
    from chatboat.chat_jsonformat import ChatJsonFormat
    bot=ChatJsonFormat()
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break
        bot.format(user_input)
        # print(f"Bot: {response}")
        
def chat_summarization():
    
    bot=ChatSummarizationMiddleware()
    bot.summarize()
    
if __name__ == "__main__":  
    # chat()
    # chat_with_tools()
    # chat_with_multi_tools()
    # chat_with_memory()
    chat_streaming()
    # chat_json_format()
    # chat_summarization()