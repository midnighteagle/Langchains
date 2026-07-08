from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description ="give the sentiment of the Feedback.")
    
parser2 = PydanticOutputParser(pydantic_object = Feedback)



prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive or negetive \n {feedback} \n {format_instructions}',
    input_variables = ['feedback'],
    partial_variables =  {'format_instructions': parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2


# result = classifier_chain.invoke(
#     {
#         'feedback':' This is a terrible SmartPhone'
#     }
# )

# print(result)
prompt2 = PromptTemplate(
    template = 'Write the appropiate response to this positive Feedback \n {feedback}',
    input_variables = ['feedback']
)
prompt3 = PromptTemplate(
    template = 'Write the appropiate response to this negative Feedback \n {feedback}',
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    # (condition, chain),
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find Sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke(
    {'feedback': 'this is beautiful Phone.'}
)
print(result)
chain.get_graph().print_ascii()
