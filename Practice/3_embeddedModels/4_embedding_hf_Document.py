# import the HuggingfaceModel by the help of Langchain_huggingface
from langchain_huggingface import HuggingFaceEmbeddings
embedding_Model = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
document = [
    "what is your name",
    "what is Your father name : ",
    "what is your Ocations of festival ",
    "what is your city name"
]
# embedding tools invoking.
vector = embedding_Model.embed_documents(document)
# printing the vector in the form of string [:5]
print(str(vector[:5]))