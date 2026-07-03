from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task ="text-generation",
)
model = ChatHuggingFace(llm = llm)

# huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# print(huggingfacehub_api_token)

result = model.invoke("what is the Capital of INDIA ?")
print(result.content)