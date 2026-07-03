from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = 'gpt-3.5-turbo-instruct')
result = llm.invoke("what is the Capital of INDIA ? ") # it give the string as output
print(result)