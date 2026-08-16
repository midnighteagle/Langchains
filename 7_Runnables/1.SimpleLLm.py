# Simple_LLM_app
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

# initalisation of LLM
llm = ChatOpenAI(
    model = "gpt-4o",
    temperature = 0.7 
)

# create prompt
prompt = PromptTemplate(
    
    template = "Suggest the catchy blog title about {topic}",
    input_variables = ["topic"]   
)

# Define the topic
topic = input("Enter the topic")

# formating the template manually using PromptTemplates
formatted_prompt = prompt.format(topic = topic)

# Call the LLM directly
blog_title = llm.invoke(formatted_prompt)

print("generated Blog title: ", blog_title.content)
