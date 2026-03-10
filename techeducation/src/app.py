
from chatboat.one_chatbot import OneChatBot
from chatboat.zero_chatbot import ZeroChatBot
from chatboat.few_chatbot import FewChatBot


def chat():
    option=input("Choose chatbot type (zero, one, few): ").strip().lower()
    if option == "zero":
        chatbot = ZeroChatBot()
    elif option == "one":
        chatbot = OneChatBot()
    else:
        chatbot = FewChatBot()
    
    print("Welcome to the AI Tech Education Chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = chatbot.generate_response(user_input)
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    chat()