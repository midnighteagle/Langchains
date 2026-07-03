from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv
load_dotenv()

# Setup the Chat Model
chatModel = ChatAnthropic(model = 'claude-3.5-sonnet')
# initialise the chatModel By the Invoke function
result = chatModel.invoke("what is your name:")
print(result)