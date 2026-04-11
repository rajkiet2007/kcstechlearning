from openai import OpenAI
client = OpenAI()
MAX_MESSAGES = 10

class Conversation:
    def __init__(self):
        self.model="gpt-4o-mini"
        self.conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]
    def trim_memory(self):
        if len(self.conversation) > MAX_MESSAGES:
            # Keep system + last messages
            self.conversation = [self.conversation[0]] + self.conversation[-MAX_MESSAGES:]
            
    def conversation_with_memory(self, user_input):
        self.conversation.append({"role": "user", "content": user_input})
        self.trim_memory()
        response = client.chat.completions.create(
            model=self.model,
            messages=self.conversation
            
        )
        assistance_reply= response.choices[0].message.content
        
        self.conversation.append({"role": "assistant", "content": assistance_reply})
        return assistance_reply
    
    def conversation_without_memory(self, user_input):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content