from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import re
import logging

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)

from graph import run_graph

app = FastAPI()


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]


@app.post("/chat")
def chat(request: ChatRequest):

    messages = []

    for msg in request.messages:
        if msg.role == "user":
            messages.append(HumanMessage(content=msg.content))
        else:
            messages.append(AIMessage(content=msg.content))

    try:
        result = run_graph(messages)

        print(result["messages"])
        content = result["messages"][-1].content

        if isinstance(content, list):
            response = "".join(
                part.get("text", "")
                for part in content
                if isinstance(part, dict)
            )
        else:
            response = content

        # Remove citations like 【2†L1-L3】
        response = re.sub(r"【\d+†L\d+(?:-L\d+)?】", "", response)

        # Clean up excessive blank lines and spaces
        response = re.sub(r"\n{3,}", "\n\n", response).strip()

        return {
            "response": response
        }

    except Exception as e:
        logging.exception(e)

        return {
            "response": (
                "Sorry, something went wrong while processing your request. "
                "Please try again in a few moments."
            )
        }