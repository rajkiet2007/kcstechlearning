from langchain.agents import AgentExecutor, create_react_agent
from models.llm import get_llm
from prompts.prompt_template import get_prompt
from tools.calculator import calculator
from tools.search import search
from config.settings import VERBOSE

def build_agent():
    llm = get_llm()
    tools = [calculator, search]
    prompt = get_prompt()

    agent = create_react_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=VERBOSE
    )

    return agent_executor