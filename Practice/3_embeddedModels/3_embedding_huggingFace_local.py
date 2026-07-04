# import the HuggingFaceEmbedding from langchain_huggingface
from langchain_huggingface import HuggingFaceEmbeddings

# setup the embedding model or tools.
embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

# creating the query for embedding
Query = "what is your name?"
# invokeing the embedding Model.
vector = embedding.embed_query(Query)
# print the Query

print(str(vector))