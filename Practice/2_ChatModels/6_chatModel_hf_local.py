# importing the HuggingFacePipeline and ChatHuggingFace from langchain_huggingface
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

# import the load_dotenv from dotenv (NO NEED because no use of API Key Of HuggingFace)
# from dotenv import load_dotenv

# load the env file by 
# load_dotenv()

# Design the LLM by the help Of HuggingFacePipeline

LLM = HuggingFacePipeline.from_model_id( # locally HuggingFacePipeline.from_model_id to design the LLM.
    model_id ='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task = 'text-generation',
    
    pipeline_kwargs=dict(
        temperature = 1.5,
        max_new_tokens = 100 # max_new_tokens not token
    )
)

ChatModel = ChatHuggingFace(llm = LLM)

response  = ChatModel.invoke("what is your name ?")
print(response.content)