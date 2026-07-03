from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI (model = 'gpt-4', temperature = 1.5,)
result = model.invoke("Write 5 Line poem On cricket")
print(result)
print(result.content)
print(result.additional_kwargs) 

