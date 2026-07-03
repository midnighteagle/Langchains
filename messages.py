from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()



message = [
    SystemMessage(content= 'You are a helpful Assistant'),
    HumanMessage(content= 'tell me about langchain')
]


result = model.invoke(message)

message.append(AIMessage(content= result.content))

print(message)