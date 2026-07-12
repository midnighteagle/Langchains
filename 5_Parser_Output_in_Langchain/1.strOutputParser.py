from langchain_openai import  ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()


model = ChatOpenAI()

# 1st prompt -> Detailed Report 
template1 = PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variables = ['topic'] 
)

# 2nd Prompt -> summary
template2 = PromptTemplate(
    template = 'write a 5 line Summary on the following text. \n {text}',
    input_variables = ['text'] 
)


# run the first template1 and store in prompt1
prompt1 = template1.invoke({'topic' : "black hole"})

# run the prompt1 by the help of model using store in result.
result = model.invoke(prompt1)


# run the first template2 and store in prompt2
prompt2 = template2.invoke({'text' : result.content}) 

# run the prompt1 by the help of model using store in result1.
result1 = model.invoke(prompt2)


# print the content of result1.
print(result1.content)