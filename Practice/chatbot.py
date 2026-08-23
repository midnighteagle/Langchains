from pathlib import Path
import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)

# --------------------------------
# Load environment variables
# --------------------------------

load_dotenv()


# --------------------------------
# Read knowledge document
# --------------------------------

knowledge_path = Path("chiranjeevi_knowledge.txt")

knowledge = knowledge_path.read_text(
    encoding="utf-8"
)


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
    say:

    "I don't have that information in my knowledge document.",
    " you search on web."

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
# Chat history
# --------------------------------

chat_history = [
    SystemMessage(content=system_prompt)
]


# --------------------------------
# Chatbot
# --------------------------------

print("===================================")
print("   Chiranjeevi AI Assistant")
print("===================================")
print("Ask me anything about Chiranjeevi.")
print("Type 'exit' to stop.")
print()


while True:

    user_input = input("YOU: ")

    # Exit
    if user_input.lower() == "exit":
        print("AI: Thank You to know about Chiranjeevi!")
        break

    # Add user message
    chat_history.append(
        HumanMessage(content=user_input)
    )

    # Ask model
    result = model.invoke(chat_history)

    # Add AI response
    chat_history.append(result)

    # Display response
    print("AI:", result.content)
    print()