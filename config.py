import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables FIRST
load_dotenv()

# Import tools AFTER environment variables are loaded
from tools import tools

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

llm = llm.bind_tools(tools)