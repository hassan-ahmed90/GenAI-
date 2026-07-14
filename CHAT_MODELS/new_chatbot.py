import streamlit as st
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os

load_dotenv()

st.set_page_config(page_title="AI Agent Bot", page_icon="🤖")
st.title("🤖 AI Agent Bot")

# ---- Initialize model (same logic as your script) ----
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9,
    max_tokens=1000,
)

# ---- Mode options (same 4 choices as your script) ----
MODES = {
    "1": ("😢 Sad AI Agent", "You are my Sad AI Agent, You respond in a sad tone and you are always sad."),
    "2": ("😄 Happy AI Agent", "You are my Happy AI Agent, You respond in a happy tone and you are always happy."),
    "3": ("😐 Neutral AI Agent", "You are my Neutral AI Agent, You respond in a neutral tone and you are always neutral."),
    "4": ("😂 Funny AI Agent", "You are my Funny AI Agent, You respond in a funny tone and you are always funny."),
}

# ---- Track whether mode has been chosen yet ----
if "mode_selected" not in st.session_state:
    st.session_state.mode_selected = False
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- Step 1: Mode selection screen (like the input() choice in your script) ----
if not st.session_state.mode_selected:
    st.subheader("Choose the AI Agent you want to talk to:")
    choice = st.radio(
        "Select a mode:",
        options=list(MODES.keys()),
        format_func=lambda k: MODES[k][0],
    )

    if st.button("Start Chat"):
        mode = MODES[choice][1]
        st.session_state.messages = [SystemMessage(content=mode)]
        st.session_state.mode_selected = True
        st.session_state.agent_label = MODES[choice][0]
        st.rerun()

# ---- Step 2: Chat screen ----
else:
    st.caption(f"Talking to: **{st.session_state.agent_label}**")

    # Display chat history (skip the SystemMessage)
    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.markdown(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(msg.content)

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

    # ---- Sidebar options ----
    with st.sidebar:
        st.header("Options")
        if st.button("🔄 Change Agent"):
            st.session_state.mode_selected = False
            st.session_state.messages = []
            st.rerun()
        if st.button("🗑️ Clear Chat"):
            mode = MODES[[k for k, v in MODES.items() if v[0] == st.session_state.agent_label][0]][1]
            st.session_state.messages = [SystemMessage(content=mode)]
            st.rerun()