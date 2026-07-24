# FinSight AI

An AI-powered financial assistant built using **LangGraph**, **LangChain**, **Groq Llama 3.3**, and **Tavily Search**.

FinSight AI demonstrates how an AI agent can reason about user queries, decide whether a tool is required, execute that tool, and return a natural language response. This project was built as the first project in a larger AI Engineering portfolio.

---

# Features

* Conversational AI Assistant
* LangGraph-based agent workflow
* Calculator tool integration
* Tavily web search integration
* Intelligent tool routing
* Stateful conversations using LangGraph
* Modular project structure

---

# Tech Stack

* Python
* LangGraph
* LangChain
* Groq (Llama 3.3 70B)
* Tavily Search API

---

# Project Structure

```
FinSight-AI/
│
├── app.py
├── config.py
├── graph.py
├── llm.py
├── prompts.py
├── requirements.txt
├── state.py
├── tools.py
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/sdtech5/FinSight-AI.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file containing your API keys.

Example:

```
GROQ_API_KEY=YOUR_KEY
TAVILY_API_KEY=YOUR_KEY
```

---

# Running the Project

```bash
python app.py
```

---

# Example Questions

* What is 125 × 48?
* Who is the CEO of NVIDIA?
* What are the latest quarterly earnings of Asian Paints?
* Summarize today's AI news.

---

# Current Version

**Version 1.0**

Current capabilities

* LangGraph workflow
* Calculator tool
* Tavily Search
* Tool routing
* Stateful conversations

---

# Roadmap

## Version 1.1

* Finance API integration
* FastAPI backend
* Structured outputs
* Improved prompt engineering
* Better error handling
* Logging
* Code refactoring

---

# Learning Objectives

This project demonstrates practical implementation of:

* AI Agents
* LangGraph
* Tool Calling
* State Management
* Prompt Engineering
* External Tool Integration

---

# License

This project is intended for learning and portfolio purposes.