from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal, Optional
import streamlit as st

load_dotenv()

# setup of the model
model = ChatOpenAI()

st.header("Users Reviews")
class Review (BaseModel):
    
    key_themes : list[str] = Field (descriptions = "give the all the key themes discussed in the review in a list")
    Summary : str = Field(description = "A brief Summary of the review ")
    sentiments: Literal["pos", "neg"] = Field(description = "Return the Sentiment of the Review either pos or neg")
    Pros: Optional[list[str]] = Field(default = None, description = "Give the all the pros of the reviews")
    Cons: Optional[list[str]] = Field(default = None, description = "give me all the cons of the reviews")
    name : Optional[str]= Field(default = None, description= "Write the name of reviewer")
    

# creation of the structured model:
Structured_Model = model.with_structured_output(Review)

userReview = st.text_area("Enter Your Review Here!!")

if st.button("Review OverView"):
    if userReview.strip() == "":
        st.warning("Please enter a review before submitting.")
    else:
        with st.spinner("Analysing Review..."):
            # invoke the Model 
            result = Structured_Model.invoke(userReview)
            
            # Displaying the structured output elegantly
            st.subheader("Analysis Result")
            st.write(f"**Reviewer Name:** {result.name if result.name else 'Unknown'}")
            st.write(f"**Sentiment:** {result.sentiments.upper()}")
            st.write(f"**Summary:** {result.Summary}")
            
            st.write("**Key Themes:**")
            st.write(result.key_themes)
            
            if result.Pros:
                st.write("**Pros:**")
                st.write(result.Pros)
                
            if result.Cons:
                st.write("**Cons:**")
                st.write(result.Cons)
    
