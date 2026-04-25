from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver

from app.graph.state import AgentState
from app.graph.nodes import chatbot, tool_node
from app.graph.edges import should_continue

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("chatbot", chatbot)
    builder.add_node("tools", tool_node)

    builder.set_entry_point("chatbot")

    builder.add_conditional_edges(
        "chatbot",
        should_continue,
        {
            "tools": "tools",
            "__end__": "__end__",
        },
    )

    builder.add_edge("tools", "chatbot")

    memory = MemorySaver()

    return builder.compile(checkpointer=memory)