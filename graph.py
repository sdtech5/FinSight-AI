from langgraph.graph import StateGraph, START, END
from typing import TypedDict


from langgraph.prebuilt import ToolNode
from config import llm
from prompts import SYSTEM_PROMPT
from tools import tools


from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, SystemMessage


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


builder = StateGraph(GraphState)

# Create a node that can execute tools
tool_node = ToolNode(tools)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", tool_node)

builder.add_edge(START, "chatbot")
builder.add_conditional_edges(
    "chatbot",
    should_continue
)

builder.add_edge("tools", "chatbot")

graph = builder.compile()



# Send the conversation to the graph
def run_graph(messages):

    result = graph.invoke(
        {
            "messages": messages
        }
    )

    return result