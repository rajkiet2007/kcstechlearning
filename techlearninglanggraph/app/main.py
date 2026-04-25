import os

from fastapi import FastAPI
from langchain_core.messages import HumanMessage

from app.schemas.chat import ChatRequest, ChatResponse
from app.graph.builder import build_graph
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

graph = build_graph()

# print("API KEY:", os.getenv("LANGCHAIN_API_KEY"))
# print("TRACING:", os.getenv("LANGCHAIN_TRACING_V2"))
# print("PROJECT:", os.getenv("LANGCHAIN_PROJECT"))
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    config = {
        "configurable": {
            "thread_id": req.session_id
        }
    }

    result = graph.invoke(
        {"messages": [HumanMessage(content=req.message)]},
        config=config
    )

    return ChatResponse(
        response=result["messages"][-1].content
    )