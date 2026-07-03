from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding_Model = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=300)

document =[
    "virat Kohli is an Indian Cricketer known for his aggressive batting and leadership",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing Skills",
    "Sachin Tendulkar, also Known as the 'God Of Cricket', Holds many batting records",
    "Rohit Sharma is known for his elegant batting and record Breaking double centuries",
    "Jusprit Bumrah is an Indian Fast Bowler known for his unorthodox action and yorkers"
]

query = "Tell me about Rohit Sharma"

doc_embedding = embedding_Model.embed_documents(document)
query_embedding = embedding_Model.embed_query(query)

score = cosine_similarity([query_embedding], doc_embedding)[0]
# print(score)

print(list(enumerate(score)))
index,score = sorted (list(enumerate(score)) ,key = lambda x:x[1] )  [-1]

print(query)
print(document[index])
print("similarity Score is : ", score)

