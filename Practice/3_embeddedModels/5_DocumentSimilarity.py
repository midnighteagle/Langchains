#import the OpenAIEmbeddings By the langchain_openai
from langchain_openai import OpenAIEmbeddings


# import dot_env from dotenv
from dotenv import load_dotenv


# import cosine_similarity from sklearn.metrics.pairwise
from sklearn.metrics.pairwise import cosine_similarity


#load the env
load_dotenv()


# setup the embedding tools (model)
embeddingModel = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 300)


# creation of documents
document = [
    "virat Kohli is Indian Cricketer known for his aggressive batting and leadership",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing Skills",
    "Sachin Tendulkar, also known as the 'God Of Cricket' , Holds many of batting records",
    "jasprit Bumrah is an Indian Fast Bowler known for his unorthodox action and yorkers"
]

# Setup of the query
query = "Tell me About Sachin Tendulkar"

# create the embedding of document and query 
embed_document = embeddingModel.embed_documents(document)
embed_query = embeddingModel.embed_query(query)

# Now find the Similarities in between the document and Query 
# In cosine_Similarity always give the first parameter is query and second is documents
score  = cosine_similarity([embed_query], embed_document)[0]
#print the score enumarate and list.

print(enumerate(score)) # it Enumate the score only.

print (list(enumerate(score))) # first enumate the vector of both doc and query then list the score.

print(sorted(list(enumerate(score)))) # keep this sorted one.

index, score =sorted(list(enumerate(score)), key = lambda x:x[1])[-1]

# print the query 
print(query)

# print the document index
print(document[index])

# print the similarity Score 
print('The Similarity Score: ', score)