# import the OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
# dotenv se load_env ko import kro 
from dotenv import load_dotenv

load_dotenv()

# setup the embedding tools or model 
Embedding = OpenAIEmbeddings(model = 'text-embedding-3-large' , dimensions = 32)

# Create an Documents for Embeddings
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West bengal",
    "Mumbai is the capital of Maharastra",
    "Gaya is the city of pleasure"
]

# embed the document by the help of embeding models

response =Embedding.embed_documents(documents)

# Print the Enbedding of the document of 32 dimensions

print(str(response))