from langchain_openai import  ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import  JsonOutputParser
from langchain.output_parsers.structured import StructuredOutputParser, ResponseSchema


load_dotenv()


model = ChatOpenAI()

schema = [
    Response_Schema (name = 'fact_1', descriptions = 'Fact 1 about the topic'),
    Response_Schema (name = 'fact_2', descriptions = 'Fact 2 about the topic'),
    Response_Schema (name = 'fact_3', descriptions = 'Fact 3 about the topic'),
]
parser = StructuredOutputParsers.from_response_schemas(schema)
template = PromptTemplate(
    template = 'Give 3 fact about {topic} \n {format_instruction}',
    input_variables = ['topic'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'black hole'})

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

chain = template | model | parser

result = chain.invoke({
    'topic' : 'black hole'
})
print(result)