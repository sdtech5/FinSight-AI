# 📈 FinSight AI

An AI-powered Financial Research Assistant built using **LangGraph**, **FastAPI**, **Streamlit**, **Groq (Qwen 3.6-27B)**, **Tavily Search**, and **Yahoo Finance**.

FinSight AI is an end-to-end AI application that enables users to research stocks, analyze companies, understand market news, and have contextual financial conversations using real-time market data and web search.

This project was built as **Project 1** in my AI Engineering portfolio to demonstrate modern AI application architecture and deployment.

---

# 🌐 Live Demo

### Frontend (Streamlit)

https://finsight-ai-ru8aocorjbdecg8eqpvzzy.streamlit.app

### Backend API (FastAPI)

https://finsight-ai-api-8slx.onrender.com

> **Note**
>
> The backend is hosted on Render's free tier. The first request after a period of inactivity may take up to a minute while the server wakes up.

---

# ✨ Features

- AI-powered conversational financial assistant
- Context-aware multi-turn conversations
- Real-time financial market research
- Live stock price retrieval
- Latest financial news search
- AI tool calling using LangGraph
- FastAPI REST backend
- Streamlit frontend
- Modular architecture
- Cloud deployment

---

# 🏗️ Architecture

```
User
   │
   ▼
Streamlit (Frontend)
   │
HTTPS
   ▼
FastAPI (Render)
   │
   ▼
LangGraph
   │
   ├── Tavily Search
   ├── Yahoo Finance
   └── Groq (Qwen 3.6-27B)
```

---

# 🛠️ Tech Stack

- Python
- LangGraph
- LangChain
- FastAPI
- Streamlit
- Groq
- Qwen 3.6-27B
- Tavily Search
- Yahoo Finance
- Pydantic
- Git
- GitHub
- Render

---

# 📂 Project Structure

```
FinSight-AI/
│
├── api.py
├── app.py
├── config.py
├── graph.py
├── prompts.py
├── streamlit_app.py
├── tools.py
├── requirements.txt
├── README.md
└── .env
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/sdtech5/FinSight-AI.git
```

Move into the project

```bash
cd FinSight-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GROQ_API_KEY=YOUR_API_KEY
TAVILY_API_KEY=YOUR_API_KEY
```

---

# ▶️ Running Locally

### Start the FastAPI backend

```bash
uvicorn api:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

### Start the Streamlit frontend

```bash
streamlit run streamlit_app.py
```

Frontend runs on

```
http://localhost:8501
```

---

# 💬 Example Questions

- Current price of Infosys
- Latest news on TCS
- Compare Infosys and TCS
- Should I hold Cholamandalam Finance?
- Explain the impact of RBI interest rate decisions on banking stocks.
- Compare large-cap and flexi-cap mutual funds.

---

# 📚 Learning Objectives

This project demonstrates practical implementation of:

- AI Agents
- LangGraph Workflows
- Tool Calling
- Prompt Engineering
- Stateful Conversations
- FastAPI REST APIs
- Streamlit Applications
- Cloud Deployment
- External API Integration
- Production-style Git Workflow

---

# 📈 Current Version

**Version 1.3**

### Implemented

- AI Agent using LangGraph
- Financial Research Assistant
- FastAPI Backend
- Streamlit Frontend
- Tool Calling
- Yahoo Finance Integration
- Tavily Web Search
- Context-aware Conversations
- Cloud Deployment
- Public Demo

---

# 🔮 Future Improvements

- Portfolio Analysis
- Document Upload & Analysis
- RAG-based Financial Knowledge Base
- Multi-LLM Routing
- Automatic Model Fallback
- Authentication
- Chat History Persistence

---

# 📄 License

This project was built for educational purposes and portfolio demonstration.
