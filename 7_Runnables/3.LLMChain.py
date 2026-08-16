from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
LLM = ChatOpenAI(model = "gpt-4o", temperature = 0.7 )

# Create a Prompt Templates 
prompt = PromptTemplate(
    template = "Suggest a catchy blog Title about {topic}",
    input_variables= ["topic"]
)

# Creating a Chain 
chain = prompt | LLM
# Entering the Topic Name
topic = input('Enter your Topic:  ')
# printing the result 
result = chain.invoke({"topic":topic})

print ("the Generated Blog Title: ", result.content)