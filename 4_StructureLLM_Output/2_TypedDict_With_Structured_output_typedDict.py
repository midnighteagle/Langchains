from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

# Create the Schema
class Review(TypedDict):
    summary: str
    sentiment: str
    
# creation of Structured Model
Structured_Model = model.with_structured_output(Review)

result  = Structured_Model.invoke("""The hardware is great, but the software feels bloating feels bloated. There are too many Pre-installed apps that I can't remove. Also the UI looks outdated compared to other Brands. Hoping for a Software update to fix this. """)

print(result)