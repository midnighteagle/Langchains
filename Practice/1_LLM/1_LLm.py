from langchain_openai import OpenAI

from dotenv import load_dotenv

# load the Dotenv
load_dotenv()

# setup of ai model
llm = OpenAI(model = "gpt-4")
# initialisation of Model with invoke function.
result  = llm.invoke("what is your name?")
print(result)