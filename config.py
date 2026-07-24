import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables FIRST
load_dotenv()

# Import tools AFTER environment variables are loaded
from tools import tools

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY"),
)

llm = llm.bind_tools(tools)