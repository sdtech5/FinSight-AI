import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="FinSight AI",
    page_icon="📈"
)

st.title("📈 FinSight AI")
st.subheader("AI-powered Financial Research Assistant")
st.caption(
    "Market insights, company research, and financial analysis powered by AI."
)

st.info(
    "⚠️ The information provided by FinSight AI is generated using AI and publicly available financial data. "
    "While every effort is made to provide accurate and up-to-date information, it should not be considered "
    "professional financial advice or the sole basis for investment decisions. Please conduct your own research "
    "and consult a qualified financial advisor before making any investment decisions."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask about a stock...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        response = requests.post(
        API_URL,
        json={"messages": st.session_state.messages}
        )

    if response.status_code == 200:
        answer = response.json()["response"]
    else:
        answer = f"Error {response.status_code}: {response.text}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)