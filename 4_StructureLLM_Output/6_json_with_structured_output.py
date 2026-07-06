from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, EmailStr, Field

load_dotenv()

model = ChatOpenAI()

# Create the Schema
json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "description": "Write down all the key themes discussed in the review in a list"
        },
        "summary": {
        "type": "string",
        "description": "A brief summary of the review"
        },
        "sentiment": {
        "type": "string",
        "enum": ["pos", "neg"],
        "description": "Return sentiment of the review either negative, positive or neutral"
        },
        "pros": {
        "type": ["array", "null"],
        "items": {
            "type": "string"
        },
        "description": "Write down all the pros inside a list"
        },
        "cons": {
        "type": ["array", "null"],
        "items": {
            "type": "string"
        },
        "description": "Write down all the cons inside a list"
        },
        "name": {
        "type": ["string", "null"],
        "description": "Write the name of the reviewer"
        }
    },
    "required": ["key_themes", "summary", "sentiment"]
}
    

    
# creation of Structured Model
Structured_Model = model.with_structured_output(json_schema)

result  = Structured_Model.invoke(""" I recently upgraded to the Samsung Galaxy S24 Ultra , and I Must say, it's an absolute powerhouse! The Snapdragon 8 gen 3 processor makes everything lighting fast-Weather I'm gamings, Multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
                                
The S-pen integaration is a great touch for note-taking and quick sketches, through I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning, captureing crisp, vibrant images even in low light. Zooming up to 100X.

However, The weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still come with bloatware-why do I need five diffrent Samsung apps for things google already provides? The $1,300 price tag is also a hard pill to shallow.

Pros:
Insanely powerful processer (great for gaming and productivity).
Stunning 200MP camera with incredible zoom capabilities.
Long battery life with fast charging.
S-pen Support is unique and useful.

Cons:
Bulky and Heavy- not great for one-handed use.
bloatware still exists in One UI.
Expensive comapred to Competitors.

Review By Akshat Arya. if not given then write Anonmous
""")

print(result)
print("Summary: ",result.get('summary'))
print("Sentiment: ",result.get('sentiment'))
print("Key Themes: ",result.get('key_themes'))
print("Pros: ",result.get('pros'))
print("Cons: ",result.get('cons'))
print("Name: ",result.get('name'))