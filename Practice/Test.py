import os
import streamlit as st

from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# 1. Page Configration

st.set_page_config(
    page_title = "ASIAN PAINT COSTUMER ENQUIRY ",
    page_icon = "🎨",
    layout="centered"
)

# 2. load ENVIRONMENT VARIABLES
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
OFFICE_EMAIL = os.getenv("OFFICE_EMAIL","chiranjeevivaston@gmail.com")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

# 3. Session Configration
if "chatbot_started" not in st.session_state:
    st.session_state["chatbot_started"] = False
if "Costumer_data" not in st.session_state:
    st.session_state["Costumer_data"] = None
if "enquiry_id" not in st.session_state:
    st.session_state["enquiry_id"] = None
    
# 4. VALIDATION of ENVIRONMENT VARIABLES
if not MONGODB_URI:
    st.error("MONGO_URI is missing from your .env file")
    st.stop()
if not SENDER_EMAIL:
    st.error("SENDER_EMAIL is missing from your .env file")
    st.stop()
if not EMAIL_APP_PASSWORD:
    st.error("EMAIL_APP_PASSWORD is missing from your .env file")
    st.stop()

# 5. Connection to mongoDB
@st.cache_resource
def connect_to_mongodb():
    client = MongoClient(MONGODB_URI)
    # cheak the connection
    client.admin.command("ping")
    return client

try:
    client = connect_to_mongodb()
    # DATABASE
    db = client["ASIAN_PAINT_DB"]
    # Collection
    enquiries_collection = db["costumer_enquiries"]
    
except ConnectionFailure :
    st.error(
        """
        Could not connect to mongoDB Atlas   
        
            please cheak:
                - MONGO_URI
                - USERNAME/PASSWORD
                - NETWORK ACESS / IP ADDRESS
                - MONGODB ATLAS CLUSTER     
        """
    )
    st.stop()
except Exception as e:
    st.error(
        """
        MongoDB connection Error: 
        {e}
        """
    )
    
# 6. Email FUNCTION
def send_email(subject, body):
    # creation of email envelope
    message = MIMEMultipart()
    
    # Sender Detail
    message["From"] = SENDER_EMAIL
    
    # Reciver Detail
    message["To"] = OFFICE_EMAIL
    
    # subject
    message["Subject"] = subject
    
    # Body detail
    message.attach(
        MIMEText(
            body,
            "plain",
            "utf-8"
        )
    )
    # attach to gmail to smtp Server
    with smtplib.SMTP_SSL(
        
        "smtp.gmail.com",
        465,
        timeout = 30
        
        )as server:
        
        # login 
        server.login(
            SENDER_EMAIL,
            EMAIL_APP_PASSWORD
        )
        
        # send Email
        server.sendmail(
            SENDER_EMAIL,
            OFFICE_EMAIL,
            message.as_string()
        )

# 7. STREAMLIT UI 
st.title("ASIAN PAINT COSTUMER ENQUIRY")
st.write(
    "Tell me about Painting requirement "
    "our team can use these detail to understand"
    "your project better"
)

# 8. Costumer Information
st.header("👤 Costumer Information")

name = st.text_input(
    "Name",
    placeholder="Enter your Name"
)
phone = st.text_input(
    "Phone",
    placeholder=("Enter your Phone Number")
)
email = st.text_input(
    "email",
    placeholder="Enter the your Email"
)
location = st.text_input(
    "Location",
    placeholder = "Example: Bhopal, Madhaya Predesh"
)
# 9. property Information
st.header("🏠 Property Information")

property_type = st.selectbox(
    "Property Type",
    [
        "Home",
        "Appartment",
        "Villa",
        "Office",
        "Shops",
        "Commercial Building",
        "Other"
    ]
)
requirement = st.selectbox(
    "Painting Requirement",
    [
        "Interior Painting",
        "Exterior Painting",
        "WaterProofing",
        "Wood Finish",
        "Colour Selection",
        "Complete Painting",
        "Other"
    ]
)
Area = st.number_input(
    "Approximate Area",
    min_value = 0,
    max_value= 100000,
    value = 0,
    step = 100
)
# 10. Budget and Timelines
st.header("Budget & Timelines")

budget = st.selectbox(
    "Approximate Budget",
    [
        "Not Decided",
        "below 25000",
        "25000 - 50000",
        "50000 - 100000"
        "100000 - 200000",
        "Above 200000"
    ]
)

timeline = st.selectbox(
    "Expected Timeline",
    [
        "Just Exploring"
        "within 1 month",
        "within 2 week",
        "within 1 Week",
        "Immidiately"
    ]
)
# 11.Service Required
st.header("Service")
service_required = st.selectbox(
    "Do you required painting / service Assistant",
    [
        "Not Sure",
        "Yes",
        "No"
    ]
)
additional_requirements = st.text_area(
    "Additional Requirement",
    placeholder="Example: I Want Premium Finish for my"
    "Living room and bedrooms"
)

# 12. Consent
consent = st.checkbox(
    "I agreed to contract regarding painting Enquiry"
)
# 13. Submit
if st.button(
    "📩 Submit Enquiry",
    type = "primary",
    use_container_width= True 
):
    # Validation: 
    if not name.strip():
        st.error("Please Enter Your name")
        st.stop()
    if not phone.strip():
        st.error("Please Enter Your Phone")
        st.stop()
    if not location.strip():
        st.error("Please Enter Your location")
        st.stop()
    if Area <= 0 :
        st.error("Please Enter the Valid Area in sq ft")
        st.stop()
    if not concent:
        st.error("Please provide consent to be contracted")
        st.stop()
# 14 Costumer Data
costumer_data = {
    "Name": name.strip(),
    "Phone":phone.strip(),
    "Email":Email.strip(),
    "Location":location.stripe(),
    "Property Type": property_type,
    "Painting Requirment" : requirement,
    "Area": Area,
    "Budget": budget,
    "Timeline":timeline,
    "Service Required": service_required,
    "Additional Requirement": additional_requirements.strip(),
    
    "status" : "New",
    "created_at": datetime.now(timezone.utc) + timedelta(hours=5,minutes=30)
    
}
# 15. SAVE TO MONGODB 
try:
    # Save costumer data to mongoDB
    result = enquiries_collection.insert_one(
        costumer_data
    )
    # keep out the Enquiry id from mongoDb
    enquiry_id = str(
        result.inserted_id()
    )
except PyMongoError as e:
    st.error(
        f"""
        Could not save enquiry in the mongoDB Atlas:
        
        {e}
        """
    )
    st.stop()
    
# 16 creation of Email body

email_body = f"""

NEW ASIAN PAINT COSTUMER ENQUIRY
=================================

Enquiry
{enquiry_id} 
--------------

Costumer Information
----------------------
Name
{name}
Phone
{phone}
Email
{email if email else "not provided"}
location
{location}


Property Information
----------------------
Property Type
{property_type}
Painting Requirement
{requirement}
Area
{Area}


Budget & Timelines
----------------------
Budget 
{budget}
Timelines
{timeline}


Service Information
--------------------
Service Required
{service_required}

Additional Requirement
{additional_requirements if additional_requirements else None}


status
--------
New

DATABASE
----------
MONGODBATLAS

please contact to the costumer regarding this enquiry.

"""

# 17. send email
try:
    send_email(
        subject = f"new Costumer Enquiry - {name}",
        body = email_body
    )
    # A. save data for the chatbot 
    st.session_state["chatbot_started"] = True
    st.session_state["costumer_data"]= costumer_data
    st.session_state["enquiry_id"] = enquiry_id
    
    # B. sucess Information
    st.success(
        "Enquiry submitted Sucessfully!"
    )
    st.info(
        f"enquiry notification sent to {OFFICE_EMAIL}"
    )
    st.write(
        f"**Enquiry ID: ** `{enquiry_id}`"
    )
    # C. Open ChatBOT
    
    if st.session_state.get("chatbot_started"):
        st.switch_page(
            "pages/chatbot1.py"
        )
        
except Exception as e:
    st.warning(
        "Your Enquiry is saved to successfully "
        "in MongoDB Atlas, but the office email"
        "could not be sent"
    )
    
    st.write(
        f"**Enquiry ID:**`{enquiry_id}`"
    )
    st.error(
        f"Email error: {e}"
    )