from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# load the Dotenv 
load_dotenv()

# setup the Chat model 
chatModel = ChatOpenAI(model= "gpt-4" , temperature= 1.5)

# intialise the model by invoke function
result = chatModel.invoke("what is your name?")

# print the AI response
print(result)