from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()
template1 = PromptTemplate(
    template = "write detail report about {topic}",
    input_variables= ['topic']
)
template2 = PromptTemplate(
    template = "Write a 5 points of Summary on following text. \n {text}",
    input_variables = ['text']
)
prompt1 = template1.invoke({'topic' : 'blackhole'})

result = model.invoke(prompt1)
prompt2 = template2.invoke({'text' : result.content})

result2 = model.invoke(prompt2)

print (result2.content)

