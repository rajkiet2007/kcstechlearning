from langchain.messages import AIMessage
from langchain.tools import tool


class CommanUtil:
       def proceesed_response(self, response):
        data=response['messages']
        messages = data if isinstance(data, list) else []
        result=''
        # Step 2: Loop and extract AIMessage text
        for msg in messages:
            if isinstance(msg, AIMessage):
                if isinstance(msg.content, list):
                    for item in msg.content:
                        if isinstance(item, dict) and item.get("type") == "text":
                            result += item.get("text")
                elif isinstance(msg.content, str):
                    result += msg.content
        return result