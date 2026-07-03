from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name  = 'sentence-transformers/all-MiniLM-L6-v2')

document = [
    "Delhi is capital of India "
    "Kolkata is  capital of WestBengal"
    "Paris is the capital of france"
]
vector = embedding.embed_documents(document)
print(str(vector))