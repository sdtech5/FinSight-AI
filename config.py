import os
from dotenv import load_dotenv

# Load environment variables FIRST

load_dotenv()
from langchain_groq import ChatGroq

# Import tools AFTER environment variables are loaded
from tools import tools

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# llm = ChatGroq(
#     model="qwen/qwen3.6-27b",
#     temperature=0,
#     reasoning_effort="none",
#     max_tokens=4096
# )

llm = llm.bind_tools(tools)