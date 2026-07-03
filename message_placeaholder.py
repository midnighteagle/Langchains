from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
#Chat Template
chat_template = ChatPromptTemplate([
    ('system', 'You are helpful customer Support agent'),
    MessagesPlaceholder(variable_name= 'chat_history'),
    ('human', '{query}')
])

chat_history = []


# Load chat History
with open ('chat_history.txt')as f:
    chat_history.extend(f.readlines())
    
print(chat_history)


# create Prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query': 'where is My refund'})

print(prompt)