from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
# load the env 
load_dotenv()

# setup the chatModel
chatModel = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
# initialise the model by the invoke function.
result = chatModel.invoke("what is Your Name?")
# print the response of the model.
print(result.content)