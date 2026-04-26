from langchain_core.prompts import PromptTemplate

def get_prompt():
    return PromptTemplate.from_template("""
You are a helpful AI assistant.

You have access to the following tools:
{tools}

Follow this format:

Question: {input}
Thought: think step by step
Action: tool name
Action Input: input
Observation: result
Final Answer: answer

{agent_scratchpad}
""")