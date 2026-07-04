from langchain_openai import OpenAIEmbeddings
# dotenv se load_env ko import kr do
from dotenv import load_dotenv
# load the dotenv
load_dotenv()

# embedding setup
embedding = OpenAIEmbeddings(model= "text-embedding-3-small" , dimensions = 32)

# Embeding a query
response = embedding.embed_query("What is the capital of INDIA")
# print the Query.
print (str(response)) 