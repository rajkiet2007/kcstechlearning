from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage
from app.tools import tools
from app.config import GEMINI_API_KEY, GEMINI_MODEL

# Ensure API key is available (GEMINI_API_KEY falls back to GOOGLE_API_KEY in config)
if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY or GOOGLE_API_KEY is not set. Set it in your environment or .env file."
    )

# Gemini model (use GEMINI_MODEL env var to override). Default is set in config.
llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    temperature=0,
    api_key=GEMINI_API_KEY,
)

llm_with_tools = llm.bind_tools(tools)


def chatbot(state):
    # If the last message is already an AIMessage with content (e.g., tool result),
    # return it directly without calling the LLM again.
    last = state["messages"][-1]
    if isinstance(last, AIMessage) and getattr(last, "content", None):
        return state

    response = llm_with_tools.invoke(state["messages"])

    # If the model returned tool calls, preserve the original response
    # so the `tool_node` can handle them.
    if hasattr(response, "tool_calls") and response.tool_calls:
        return {"messages": [response]}

    def _extract_text(obj):
        """Recursively extract/flatten text from common response shapes."""
        if obj is None:
            return ""
        if isinstance(obj, str):
            return obj
        if isinstance(obj, (int, float, bool)):
            return str(obj)
        if hasattr(obj, "content"):
            return _extract_text(obj.content)
        if isinstance(obj, dict):
            # try common keys
            for k in ("content", "text", "message", "response"):
                if k in obj:
                    return _extract_text(obj[k])
            # fallback: join values
            return " ".join(_extract_text(v) for v in obj.values())
        if isinstance(obj, (list, tuple)):
            return " ".join(_extract_text(x) for x in obj)
        # fallback
        return str(obj)

    text = _extract_text(response)
    return {"messages": [AIMessage(content=text)]}


def tool_node(state):
    last_message = state["messages"][-1]

    if not hasattr(last_message, "tool_calls"):
        return state

    results = []

    for tool_call in last_message.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        for t in tools:
            if t.name == tool_name:
                result = t.invoke(tool_args)
                results.append(AIMessage(content=result))

    return {"messages": results}