from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    name: str = Field(description = "Name of the Person")
    age : int = Field(gt = 18 , description = "Age of Person")
    city: str = Field(description = "Name of the city of the person where belongs to ")
    
parser = PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
    template = "Give the name, age, city of the {Place} person \n {format_Instruction}",
    input_variables =['place'],
    partial_variables = {"format_Instruction" : parser.get_format_instructions()}
)
# prompt = template.invoke(
#     {
#         "Place" : "Indian"
#     }
# )
# print(prompt)

chain = template | model | parser 

# result = model.invoke(prompt)
final_result = chain.invoke(
    {
        "Place": "Indian"
    }
)
print(final_result)
