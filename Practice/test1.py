from langchain_openai import ChatOpenAI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal
from dotenv import load_dotenv

load_dotenv()

class Review (BaseModel):
    KeyThemes : list[str] = Field(description="Write Down all the key themes of the Review in the list"),
    summary : str = Field(description = "Write down the brief summary for the Review "),
    sentiment:Literal["POS","NOS"] = Field(description="Write the Sentiment of the review "),
    Pros: Optional[list[str]] = Field(description="Write the Pros of the review in the list")
    Cons: Optional[list[str]] = Field("Write Down the cons of the Review in the list ")
    Name: Optional[str] = Field("Write the name of the Reviewer if Mentioned")
    
model = ChatOpenAI()
structured_model = model.with_structured_output(Review)
review = (
    """
    I recently upgraded to the Samsung Galaxy S24 Ultra , and I Must say, it's an absolute powerhouse! The Snapdragon 8 gen 3 processor makes everything lighting fast-Weather I'm gamings, Multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
                                
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

"""

)
result= structured_model.invoke(review)

print("Keythemes: ",result.KeyThemes)
print("Summary: ",result.summary)
print("Sentiments: ",result.sentiment)
print("Pros: ",result.Pros)
print("Cons: ",result.Cons)
print("Name: ",result.Name)
