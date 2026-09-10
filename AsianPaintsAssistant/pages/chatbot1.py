from pathlib import Path

import streamlit as st

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# ============================================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Asian Paints AI Assistant",
    page_icon="🎨",
    layout="centered"
)


# ============================================================
# 3. LOAD KNOWLEDGE DOCUMENT
# ============================================================

projectFolder = Path(__file__).resolve().parent.parent

knowledge_path = projectFolder/ "Asian_Paints_Knowledge.txt"
    
    
    


if not knowledge_path.exists():

    st.error(
        "❌ asian_paints_knowledge.txt was not found."
    )

    st.stop()


knowledge = knowledge_path.read_text(
    encoding="utf-8"
)


# ============================================================
# 4. CHECK CUSTOMER DATA
# ============================================================

if "customer_data" not in st.session_state:

    st.error(
        "❌ Customer information was not found."
    )

    st.info(
        "Please submit the enquiry form first."
    )

    st.stop()


customer_data = st.session_state.customer_data


# ============================================================
# 5. INITIALIZE MODEL
# ============================================================

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2
)


# ============================================================
# 6. SYSTEM PROMPT
# ============================================================

system_prompt = f"""
You are an Asian Paints AI Customer Sales Assistant.

Your job is to help the customer understand their
painting requirements and identify suitable Asian Paints
products.

The customer has already submitted an enquiry form.

Do NOT ask the customer to repeat information that
is already present below.

============================================================
CUSTOMER INFORMATION
============================================================

Name:
{customer_data.get("name", "Not provided")}

Phone:
{customer_data.get("phone", "Not provided")}

Email:
{customer_data.get("email", "Not provided")}

Location:
{customer_data.get("location", "Not provided")}

Property Type:
{customer_data.get("property_type", "Not provided")}

Painting Requirement:
{customer_data.get("requirement", "Not provided")}

Area:
{customer_data.get("area_sqft", "Not provided")} sq ft

Budget:
{customer_data.get("budget", "Not provided")}

Timeline:
{customer_data.get("timeline", "Not provided")}

Service Required:
{customer_data.get("service_required", "Not provided")}

Additional Requirements:
{customer_data.get("additional_requirements", "Not provided")}

Enquiry ID:
{customer_data.get("_id", "Not provided")}

============================================================
ASIAN PAINTS KNOWLEDGE
============================================================

{knowledge}

============================================================
IMPORTANT RULES
============================================================

1. Use the customer information when personalizing
   responses.

2. Do not ask the customer to repeat information
   already available.

3. Ask only relevant missing questions.

4. Behave like a professional Asian Paints sales
   consultant.

5. Use the knowledge document for Asian Paints
   product and domain knowledge.

6. Never invent prices.

7. Never invent product specifications.

8. Never invent product availability.

9. Never invent discounts or warranties.

10. Current prices must be verified from reliable
    current sources.

11. Prefer official Asian Paints sources for current
    product information.

12. If pricing information is not verified, clearly
    tell the customer.

13. Never present an estimate as an official quotation.

14. When recommending a product, explain why it matches
    the customer's requirements.

15. Prefer 1–3 relevant product recommendations.

16. For cost estimation, consider:
    - Area
    - Product
    - Number of coats
    - Primer
    - Putty
    - Surface condition
    - Finish
    - Labour

17. If important information is missing for an estimate,
    ask the customer for it.

18. If the customer has dampness, leakage or structural
    concerns, recommend professional inspection.

19. Keep normal responses concise and conversational.

20. The objective is to qualify the customer and help
    them choose an appropriate Asian Paints solution.

============================================================
RELIABILITY
============================================================

If information cannot be verified, do not guess.

Say:

"I don't have enough verified information to answer
that accurately."
"""


# ============================================================
# 7. INITIALIZE CHAT HISTORY
# ============================================================

if "chat_messages" not in st.session_state:

    st.session_state.chat_messages = [

        SystemMessage(
            content=system_prompt
        )

    ]


# ============================================================
# 8. SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎨 Asian Paints AI")

    st.write(
        "Personalized AI sales assistant"
    )

    st.divider()

    st.subheader(
        "Customer Information"
    )

    st.write(
        f"**Name:** "
        f"{customer_data.get('name', 'Not provided')}"
    )

    st.write(
        f"**Location:** "
        f"{customer_data.get('location', 'Not provided')}"
    )

    st.write(
        f"**Property:** "
        f"{customer_data.get('property_type', 'Not provided')}"
    )

    st.write(
        f"**Requirement:** "
        f"{customer_data.get('requirement', 'Not provided')}"
    )

    st.write(
        f"**Area:** "
        f"{customer_data.get('area_sqft', 'Not provided')} sq ft"
    )

    st.write(
        f"**Budget:** "
        f"{customer_data.get('budget', 'Not provided')}"
    )

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.chat_messages = [

            SystemMessage(
                content=system_prompt
            )

        ]

        st.rerun()


# ============================================================
# 9. MAIN UI
# ============================================================

st.title(
    "🎨 Asian Paints AI Assistant"
)

st.caption(
    f"Personalized assistance for "
    f"{customer_data.get('name', 'Customer')}"
)


# ============================================================
# 10. DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.chat_messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):

            st.markdown(
                message.content
            )

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):

            st.markdown(
                message.content
            )


# ============================================================
# 11. CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Ask about paints, colours, products or cost..."
)


# ============================================================
# 12. PROCESS USER MESSAGE
# ============================================================

if user_input:

    with st.chat_message("user"):

        st.markdown(user_input)


    st.session_state.chat_messages.append(

        HumanMessage(
            content=user_input
        )

    )


    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = model.invoke(

                st.session_state.chat_messages

            )

            response = result.content

            st.markdown(response)


    st.session_state.chat_messages.append(

        AIMessage(
            content=response
        )

    )