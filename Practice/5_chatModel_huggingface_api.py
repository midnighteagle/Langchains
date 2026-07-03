from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

# load the dot env 
load_dotenv()

# creation of LLM By the HuggingFaceEndPoint
LLM = HuggingFaceEndpoint(
    repo_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task ='text-generation'
)

# Setup the ChatModel
ChatModel = ChatHuggingFace(llm = LLM)

# initialise the chat Model
response = ChatModel.invoke("What is Your Name: ")
# print  tha response of AI.
print(response)