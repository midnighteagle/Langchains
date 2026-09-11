import os
import smtplib
from datetime import datetime, timezone

import streamlit as st
from dotenv import load_dotenv

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Asian Paints Customer Enquiry",
    page_icon="🎨",
    layout="centered"
)


# =========================================================
# 2. LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

OFFICE_EMAIL = os.getenv(
    "OFFICE_EMAIL",
    "chiranjeevivaston@gmail.com"
)

SENDER_EMAIL = os.getenv("SENDER_EMAIL")

EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


# =========================================================
# 3. SESSION STATE
# =========================================================

if "chatbot_started" not in st.session_state:
    st.session_state["chatbot_started"] = False

if "customer_data" not in st.session_state:
    st.session_state["customer_data"] = None

if "enquiry_id" not in st.session_state:
    st.session_state["enquiry_id"] = None


# =========================================================
# 4. CHECK ENVIRONMENT VARIABLES
# =========================================================

if not MONGODB_URI:
    st.error("❌ MONGODB_URI is missing in your .env file.")
    st.stop()

if not SENDER_EMAIL:
    st.error("❌ SENDER_EMAIL is missing in your .env file.")
    st.stop()

if not EMAIL_APP_PASSWORD:
    st.error(
        "❌ EMAIL_APP_PASSWORD is missing in your .env file."
    )
    st.stop()


# =========================================================
# 5. CONNECT TO MONGODB ATLAS
# =========================================================

@st.cache_resource
def connect_to_mongodb():

    client = MongoClient(MONGODB_URI)

    # Test MongoDB connection
    client.admin.command("ping")

    return client


try:

    client = connect_to_mongodb()

    # Database
    db = client["asian_paints_db"]

    # Collection
    enquiries_collection = db["customer_enquiries"]


except ConnectionFailure:

    st.error(
        """
        ❌ Could not connect to MongoDB Atlas.

        Please check:

        - MongoDB URI
        - Username/password
        - Network Access / IP address
        - MongoDB Atlas cluster
        """
    )

    st.stop()


except Exception as e:

    st.error(
        f"❌ MongoDB connection error:\n\n{e}"
    )

    st.stop()


# =========================================================
# 6. EMAIL FUNCTION
# =========================================================

def send_email(subject, body):

    # Create email
    message = MIMEMultipart()

    # Sender
    message["From"] = SENDER_EMAIL

    # Receiver
    message["To"] = OFFICE_EMAIL

    # Subject
    message["Subject"] = subject

    # Email body
    message.attach(
        MIMEText(
            body,
            "plain",
            "utf-8"
        )
    )

    # Connect to Gmail SMTP server
    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        timeout=30
    ) as server:

        # Login
        server.login(
            SENDER_EMAIL,
            EMAIL_APP_PASSWORD
        )

        # Send email
        server.sendmail(
            SENDER_EMAIL,
            OFFICE_EMAIL,
            message.as_string()
        )


# =========================================================
# 7. STREAMLIT UI
# =========================================================

st.title("🎨 Asian Paints Customer Enquiry")

st.write(
    "Tell us about your painting requirements. "
    "Our team can use these details to understand "
    "your project better."
)


# =========================================================
# 8. CUSTOMER INFORMATION
# =========================================================

st.header("👤 Customer Information")

name = st.text_input(
    "Full Name *",
    placeholder="Enter your full name"
)

phone = st.text_input(
    "Phone Number *",
    placeholder="Enter your phone number"
)

customer_email = st.text_input(
    "Email",
    placeholder="Enter your email address"
)

location = st.text_input(
    "Location *",
    placeholder="Example: Indore, Madhya Pradesh"
)


# =========================================================
# 9. PROPERTY INFORMATION
# =========================================================

st.header("🏠 Property Information")

property_type = st.selectbox(
    "Property Type",
    [
        "Home",
        "Apartment",
        "Villa",
        "Office",
        "Shop",
        "Commercial Building",
        "Other"
    ]
)

requirement = st.selectbox(
    "Painting Requirement",
    [
        "Interior Painting",
        "Exterior Painting",
        "Waterproofing",
        "Wood Finish",
        "Colour Selection",
        "Complete Painting",
        "Other"
    ]
)

area = st.number_input(
    "Approximate Area (sq ft)",
    min_value=0,
    max_value=100000,
    value=0,
    step=100
)


# =========================================================
# 10. BUDGET & TIMELINE
# =========================================================

st.header("💰 Budget & Timeline")

budget = st.selectbox(
    "Approximate Budget",
    [
        "Not Decided",
        "Below ₹25,000",
        "₹25,000 – ₹50,000",
        "₹50,000 – ₹1,00,000",
        "₹1,00,000 – ₹2,00,000",
        "Above ₹2,00,000"
    ]
)

timeline = st.selectbox(
    "Expected Timeline",
    [
        "Just Exploring",
        "Within 1 Month",
        "Within 2 Weeks",
        "Within 1 Week",
        "Immediately"
    ]
)


# =========================================================
# 11. SERVICE INFORMATION
# =========================================================

st.header("🛠 Service")

service_required = st.selectbox(
    "Do you require painting/service assistance?",
    [
        "Not Sure",
        "Yes",
        "No"
    ]
)

additional_requirements = st.text_area(
    "Additional Requirements",
    placeholder=(
        "Example: I want premium finish for my "
        "living room and bedrooms."
    )
)


# =========================================================
# 12. CONSENT
# =========================================================

consent = st.checkbox(
    "I agree to be contacted regarding my painting enquiry."
)


# =========================================================
# 13. SUBMIT ENQUIRY
# =========================================================

if st.button(
    "📩 Submit Enquiry",
    type="primary",
    use_container_width=True
):

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not name.strip():

        st.error("Please enter your name.")
        st.stop()

    if not phone.strip():

        st.error("Please enter your phone number.")
        st.stop()

    if not location.strip():

        st.error("Please enter your location.")
        st.stop()

    if area <= 0:

        st.error("Please enter a valid area.")
        st.stop()

    if not consent:

        st.error(
            "Please provide consent to be contacted."
        )

        st.stop()


    # =====================================================
    # 14. CREATE CUSTOMER DATA
    # =====================================================

    customer_data = {

        "name": name.strip(),

        "phone": phone.strip(),

        "email": customer_email.strip(),

        "location": location.strip(),

        "property_type": property_type,

        "requirement": requirement,

        "area_sqft": area,

        "budget": budget,

        "timeline": timeline,

        "service_required": service_required,

        "additional_requirements":
            additional_requirements.strip(),

        "status": "New",

        "created_at":
            datetime.now(timezone.utc)
    }


    # =====================================================
    # 15. SAVE TO MONGODB ATLAS
    # =====================================================

    try:

        result = enquiries_collection.insert_one(
            customer_data
        )

        # MongoDB ObjectId
        enquiry_id = str(
            result.inserted_id
        )

    except PyMongoError as e:

        st.error(
            f"""
            ❌ Could not save enquiry to MongoDB:

            {e}
            """
        )

        st.stop()


    # =====================================================
    # 16. CREATE EMAIL CONTENT
    # =====================================================

    email_body = f"""

New Asian Paints Customer Enquiry

=================================

Enquiry ID:
{enquiry_id}


CUSTOMER INFORMATION
--------------------

Name:
{name}

Phone:
{phone}

Email:
{customer_email if customer_email else "Not provided"}

Location:
{location}


PROPERTY INFORMATION
--------------------

Property Type:
{property_type}

Painting Requirement:
{requirement}

Approximate Area:
{area} sq ft


BUDGET & TIMELINE
-----------------

Budget:
{budget}

Timeline:
{timeline}


SERVICE INFORMATION
-------------------

Service Required:
{service_required}


ADDITIONAL REQUIREMENTS
-----------------------

{additional_requirements if additional_requirements else "None"}


STATUS
------

New


DATABASE
--------

MongoDB Atlas

Enquiry ID:
{enquiry_id}


Please contact the customer regarding this enquiry.

"""


    # =====================================================
    # 17. SEND EMAIL
    # =====================================================

    try:

        send_email(
            subject=f"New Customer Enquiry - {name}",
            body=email_body
        )


        # =================================================
        # 18. SAVE DATA FOR CHATBOT
        # =================================================

        st.session_state["chatbot_started"] = True

        st.session_state["customer_data"] = customer_data

        st.session_state["enquiry_id"] = enquiry_id


        # =================================================
        # 19. SUCCESS
        # =================================================

        st.success(
            "✅ Enquiry submitted successfully!"
        )

        st.info(
            f"📧 Enquiry notification sent to {OFFICE_EMAIL}"
        )

        st.write(
            f"**Enquiry ID:** `{enquiry_id}`"
        )


        # =================================================
        # 20. OPEN CHATBOT PAGE
        # =================================================
        if  st.session_state.get("chatbot_started"):
            st.switch_page(
                "pages/chatbot1.py"
            )


    except Exception as e:

        st.warning(
            "⚠️ Your enquiry was saved successfully "
            "in MongoDB Atlas, but the office email "
            "could not be sent."
        )

        st.write(
            f"**Enquiry ID:** `{enquiry_id}`"
        )

        st.error(
            f"Email error: {e}"
        )