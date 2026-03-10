from xmlrpc import client

from chatbot.chatboat import ChatBot
from chatbot.fewshotchatbot import FewChatBot
from chatbot.image_gen_chatbot import ImageGenChatBot
from chatbot.text_generation import TextGeneration
from chatbot.oneshotchatbot import OneChatBot
from chatbot.zero_gemini_chatbot import ZeroChatBot

def chat():
    
    bot = ChatBot("Maths Mentor")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = bot.send_message(user_input)
        print(f"{bot.name}: {response}")
        
def text_generation():
    
    text_gen = TextGeneration("gpt-5.4")
    # prompt = "What is the capital of France?"
    prompt=input("You: ")
    response = text_gen.generate_text(prompt)
    print(f"Generated Text: {response}")
    
def text_generation_with_instructions():
    
    text_gen = TextGeneration("gpt-5")
    prompt = input("You: ")
    response = text_gen.generate_text_with_instructions(prompt)
    print(f"Generated Text with Instructions: {response}")
    
def one_shot_chatbot():
    
    
    bot = OneChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = bot.generate_response(user_input)
        print(f"Medical Assistant: {response}")
        
def few_shot_chatbot():
    
    bot = FewChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = bot.generate_response(user_input)
        print(f"Medical Assistant: {response}")
def zero_gemini_chatbot():
    
    bot = ZeroChatBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat. Goodbye!")
            break
        response = bot.generate_response(user_input)
        print(f"Medical Assistant: {response}")
def image_generation_chatbot():
    
    bot = ImageGenChatBot(client)
    prompt = input("You: ")
    bot.generate_image(prompt)
    
if __name__ == "__main__":   
        # chat()
        # text_generation()
        # text_generation_with_instructions()
        # one_shot_chatbot()
        # few_shot_chatbot()
        # zero_gemini_chatbot()
        # few_shot_chatbot()
        image_generation_chatbot()