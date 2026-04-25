from langchain.agents import create_agent
from chatboat.providerStrategy import ContactInfo
from chatboat.model import Model


class ChatJsonFormat:
    def __init__(self):
        self.model = Model().get_model("gemini")

    def format(self, user_input):
        contact_info_schema = {
            "type": "object",
            "description": "Contact information for a person.",
            "properties": {
                "name": {"type": "string", "description": "The name of the person"},
                "email": {"type": "string", "description": "The email address of the person"},
                "phone": {"type": "string", "description": "The phone number of the person"}
            },
            "required": ["name", "email", "phone"]
}
        agent = create_agent(
            model=self.model,
            tools=[],
            response_format=ContactInfo
            # response_format=contact_info_schema
        )
        # Invoke agent
        result = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": f"Extract contact info from: {user_input}"
                }
            ]
        })

        # Structured output
        print(result["structured_response"])
        # Output:
        # {'name': 'John Doe', 'email': 'john@example.com', 'phone': '(555) 123-4567'}