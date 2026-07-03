#import of langchain with OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
#import the dotenv
from dotenv import load_dotenv
# here to Execute
load_dotenv()

#initialisation of Model that is ChatOpenAI
model = ChatOpenAI()

# capture the chat_History 
chat_History = [
    SystemMessage(content = 'You are a helpful Assistant'),
    
]

# Take a input and give output by the AI
while True:
    user_input = input("YOU: ")
    
    chat_History.append(HumanMessage(content = user_input))
    
    if user_input =="exit":
        break
    result = model.invoke(chat_History)
    chat_History.append(AIMessage(content = result.content))
    print("AI: ", result.content)
    
    
# Show the AI History.
print(chat_History)