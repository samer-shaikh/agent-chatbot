import streamlit as st
from graph import chatbot
from langchain_core.messages import HumanMessage

# ---------------- Page Config ----------------

st.set_page_config(
    page_title="Agent Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Session State ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "chat_1"

# ---------------- Sidebar ----------------

with st.sidebar:

    st.title("🤖 Agent Chatbot")

    st.caption("Powered by LangGraph + Gemini")

    st.divider()

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader("Conversation")

    if len(st.session_state.messages) == 0:
        st.info("No conversation yet")

    st.divider()

    st.markdown(
        """
        ### About
        
        Built using:
        - LangGraph
        - Gemini API
        - Streamlit
        """
    )

# ---------------- Main Page ----------------

st.title("🤖 Agent Chatbot")

st.caption(
    "Your AI Assistant powered by LangGraph and Google Gemini"
)

# ---------------- Display Messages ----------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- Chat Input ----------------

user_input = st.chat_input(
    "Ask anything..."
)

# ---------------- User Message ----------------

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # ---------------- AI Response ----------------

    with st.chat_message("assistant"):

        ai_respones = st.write_stream(
            message_chunk.content for message_chunk,meta_data in chatbot.stream( # type: ignore
                {'messages':[HumanMessage(content=user_input)]},
                config={
                    "configurable": {
                        "thread_id": st.session_state.thread_id
                        }},
                stream_mode='messages'  
            )
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_respones
        }
    )