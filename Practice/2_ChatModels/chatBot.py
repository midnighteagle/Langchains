from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

