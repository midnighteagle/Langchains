from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal, Optional
import streamlit as st

load_dotenv()

# setup of the model
model = ChatOpenAI()

class Review (BaseModel):
    
    key_themes : list[str] = Field (descriptions = "give the all the key themes discussed in the review in a list")
    Summary : str = Field(description = "A brief Summary of the review "),
    sentiments: Literal["pos", "neg"] = Field("Return the Sentiment of the Review either pos or neg")
    Pros: Optional[list[str]] = Field(default = None, description = "Give the all the pros of the reviews")
    Cons: Optional[list[str]] = Field(default = None, description = "give me all the cons of the reviews")
    name : Optional[str]= Field(default = None, description= "Write the name of reviewer")

# creation of the structured model:
Structured_Model = model.with_structured_output(Review)
# user_Prompt are that user given here
user_review = input("Give your Reviews: >>  ")
# initialised the model
result = Structured_Model.invoke(user_review)
print(result)
print("Summary: ", result.Summary)
print("Key_themes: ", result.key_themes)
print("Pros: ", result.Pros)
print("Cons: ", result.Cons)
print("Name: ",result.name)
