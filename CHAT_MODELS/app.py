import streamlit as st
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os

load_dotenv()

st.set_page_config(page_title="AI/ML Teacher Bot", page_icon="🤖")
st.title("🤖 AI/ML Teacher Bot")

# ---- Initialize model (same logic as your script) ----
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9,
    max_tokens=1000,
)

# ---- Initialize chat history in session state ----
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are my AI/ML Teacher."),
    ]

# ---- Display chat history (skip the SystemMessage) ----
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# ---- Chat input ----
prompt = st.chat_input("YOU:")

if prompt:
    # Same logic: append human message, invoke model, append AI response
    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
            st.markdown(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))

# ---- Optional: clear chat button ----
with st.sidebar:
    st.header("Options")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            SystemMessage(content="You are my AI/ML Teacher."),
        ]
        st.rerun()