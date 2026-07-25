from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from graph import run_graph

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):

    result = run_graph([
        HumanMessage(content=request.message)
    ])

    return {
    "response": result["messages"][-1].content
    }   