from langchain_core.messages import SystemMessage
from prompts import SYSTEM_PROMPT

# Store the conversation history
conversation = [
    SystemMessage(content=SYSTEM_PROMPT)
]