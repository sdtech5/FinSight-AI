# Import the LangChain message classes
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Import the LangChain LLM
from config import llm

# Import the conversation history
from state import conversation


# Send the user's prompt to the LLM and return the response
def ask_llm(prompt: str) -> str:

    # Add the user's message to the conversation
    conversation.append(HumanMessage(content=prompt))

    # Get the LLM's response
    response = llm.invoke(conversation)

    # If the LLM wants to call a tool, return the tool call for now
    if response.tool_calls:
        print(response.tool_calls)

    # Extract the text from the response
    answer = response.content

    # Store the AI's reply in the conversation
    conversation.append(AIMessage(content=answer))

    return answer