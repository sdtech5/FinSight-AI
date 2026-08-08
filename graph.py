from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated

from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages

from langchain_core.messages import (
    BaseMessage,
    SystemMessage,
    HumanMessage
)

from config import llm
from prompts import SYSTEM_PROMPT
from tools import tools, finance_tool


# Store the conversation messages in the graph state

class GraphState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# Invoke the LLM with the current conversation

def chatbot(state: GraphState):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"]
    ]

    response = llm.invoke(messages)

    return {
        "messages": [response]
    }


# Decide whether to execute a tool or finish the graph

def should_continue(state: GraphState):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return END


# Detect finance-related questions

def is_finance_query(state: GraphState):

    last_message = state["messages"][-1]

    if not isinstance(last_message, HumanMessage):
        return "chatbot"

    text = last_message.content.lower()

    finance_keywords = [
        "stock price",
        "share price",
        "current price",
        "current status",
        "stock status",
        "market price",
        "latest price",
        "today's price",
        "today price",
        "stock",
        "share"
    ]

    if any(keyword in text for keyword in finance_keywords):
        return "finance"

    return "chatbot"


# Finance router

def finance_router(state: GraphState):

    last_message = state["messages"][-1]
    text = last_message.content.strip()

    # Require an exact Yahoo Finance ticker symbol

    if ".NS" not in text.upper() and ".BO" not in text.upper():

        return {
            "messages": [
                HumanMessage(
                    content=(
                        "For accurate stock-market data, please provide the exact "
                        "Yahoo Finance ticker symbol for the stock.\n\n"
                        "For example:\n"
                        "HCL Technologies → HCLTECH.NS\n"
                        "Infosys → INFY.NS\n\n"
                        "You can find the exact ticker symbol on Yahoo Finance."
                    )
                )
            ]
        }

    # Extract ticker from user's message

    words = text.replace(",", " ").split()

    symbol = None

    for word in words:
        cleaned = word.strip(".,!?()[]{}\"'")

        if (
            cleaned.upper().endswith(".NS")
            or cleaned.upper().endswith(".BO")
        ):
            symbol = cleaned.upper()
            break

    if not symbol:

        return {
            "messages": [
                HumanMessage(
                    content=(
                        "Please provide the exact Yahoo Finance ticker symbol.\n\n"
                        "For example: HCLTECH.NS"
                    )
                )
            ]
        }

    # Fetch verified market data

    result = finance_tool.invoke(symbol)

    print("🔥 FINANCE ROUTER HIT")
    print("🔥 RAW FINANCE RESULT:")
    print(result)

    return {
        "messages": [
            HumanMessage(
                content=(
                    "Use the following verified market data to answer the user's "
                    "question. Do not replace, modify, or invent any values.\n\n"
                    f"{result}"
                )
            )
        ]
    }


# Create graph

builder = StateGraph(GraphState)

tool_node = ToolNode(tools)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", tool_node)
builder.add_node("finance", finance_router)


# Route the initial user message

builder.add_conditional_edges(
    START,
    is_finance_query
)


# Route tool calls from the chatbot

builder.add_conditional_edges(
    "chatbot",
    should_continue
)


builder.add_edge("tools", "chatbot")


# Compile graph

graph = builder.compile()


# Send conversation to graph

def run_graph(messages):

    result = graph.invoke(
        {
            "messages": messages
        }
    )

    return result