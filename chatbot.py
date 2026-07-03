from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

chat_History = [
    SystemMessage(content = 'You are a helpful Assistant'),
    
]

while True:
    user_input = input("YOU: ")
    
    chat_History.append(HumanMessage(content = user_input))
    
    if user_input =="exit":
        break
    result = model.invoke(chat_History)
    chat_History.append(AIMessage(content = result.content))
    print("AI: ", result.content)
    
    
    
print(chat_History)