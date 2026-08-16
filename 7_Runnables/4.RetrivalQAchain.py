from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI

# load the document
loader = TextLoader("./Resume.pdf") # Ensure Document exist
documents = loader.load()

# Split the text into Smaller chunks
text_Splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
docs = text_Splitter.split_documents(documents)

# Convert text into embeddings & stores in FAISS 
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# Create a retrivers (fetches relevent documents)
retrivers = vectorstore.as_retriever()

# Initialised the llm 
llm = OpenAI(model = "gpt-3.5-turbo", temperature = 0.7)

# creation of chains
qa_chain = llm | retrivers

# Manually pass Retrived text to LLM 
prompt = "What are the Key takeaways from the document?"
answer = qa_chain.invoke(prompt)

# print the Answer 
print ("Answer", answer)