from langchain_openai import  ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import  JsonOutputParser

load_dotenv()


model = ChatOpenAI()

parser = JsonOutputParser()
template = PromptTemplate(
    # template = 'give me the name, age and city of a fictional person \n{format_instruction}',
    # input_variables = [],
    # partial_variables = {'format_instruction': parser.get_format_instructions()}
    
    template = 'give me 5 fact about {topic} \n {format_instruction}',
    input_variables = ['topic'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()
# print(prompt)

# result = model.invoke(prompt)
# print(result)
# final_result = parser.parse(result.content)


# print(final_result)
# print(final_result['name'])
# print(type(final_result))


chain = template | model | parser
result = chain.invoke({'topic' : 'black hole'})
print(result)