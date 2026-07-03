from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
"""
By default, the length of the embedding vector is 1536 for text-embedding-3-small or 
3072 for text-embedding-3-large. 

To reduce the embedding’s dimensions without losing its concept-representing properties,
pass in the dimensions parameter.

Find more detail on embedding dimensions in the embedding use case section.

"""
enbedding  = OpenAIEmbeddings(model = "text-embedding-3-small", dimensions = 32)
document = [
    "Delhi is capital of India "
    "Kolkata is  capital of WestBengal"
    "Paris is the capital of france"
]
result = enbedding.embed_documents(document)
print (str(result))