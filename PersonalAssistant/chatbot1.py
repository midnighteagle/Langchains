from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# --------------------------------
# Load environment variables
# --------------------------------

load_dotenv()


# --------------------------------
# Streamlit page configuration
# --------------------------------

st.set_page_config(
    page_title="Chiranjeevi Questionaire",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------
# Read knowledge document
# --------------------------------

knowledge_path = Path("chiranjeevi_knowledge.txt")

if not knowledge_path.exists():
    st.error("chiranjeevi_knowledge.txt was not found.")
    st.stop()

knowledge = knowledge_path.read_text(encoding="utf-8")


# --------------------------------
# Initialize model
# --------------------------------

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)


# --------------------------------
# System instruction
# --------------------------------

system_prompt = f"""
You are Chiranjeevi's personal AI assistant.

Your job is to answer questions about Chiranjeevi
using ONLY the information provided in the knowledge
document below.

KNOWLEDGE DOCUMENT
==================

{knowledge}

==================

IMPORTANT RULES:

1. Answer questions using the knowledge document.

2. Do not invent information about Chiranjeevi.

3. If the information is not present in the document,
say exactly:

"I don't have that information in my knowledge document."

4. If the document says something is a project idea,
do not describe it as a completed production project.

5. Keep answers clear and concise unless the user
asks for more detail.

6. For technical questions about Chiranjeevi,
use the technical information present in the document.

7. You are answering questions about Chiranjeevi,
not general questions unless they are related
to the document.
"""


# --------------------------------
# Initialize chat history
# --------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]


# --------------------------------
# Sidebar
# --------------------------------

with st.sidebar:
    st.title("🤖 Chiranjeevi AI")

    st.write(
        "Ask questions about Chiranjeevi "
        "based on the knowledge document."
    )

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            SystemMessage(content=system_prompt)
        ]
        st.rerun()


# --------------------------------
# Main UI
# --------------------------------

st.title("🤖 Chiranjeevi AI Assistant")

st.caption(
    "Ask me anything about Chiranjeevi."
)


# --------------------------------
# Display previous messages
# --------------------------------

for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.markdown(message.content)


# --------------------------------
# Chat input
# --------------------------------

user_input = st.chat_input(
    "Ask something about Chiranjeevi..."
)


# --------------------------------
# Process user message
# --------------------------------

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Add user message to history
    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = model.invoke(
                st.session_state.messages
            )

            response = result.content

            st.markdown(response)

    # Add AI response to history
    st.session_state.messages.append(
        AIMessage(content=response)
    )