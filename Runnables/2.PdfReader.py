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

# manually Retrivers (fetches relevents Documents )
query = "what are they key takeaways from the documents?"
retrived_docs = retrivers._get_relevant_documents(query)

# Combine Retrived Text into a Single Prompt
retrived_text = "\n".join([doc.page_content for doc in retrived_docs])

# Initialised the llm 
llm = OpenAI(model = "gpt-3.5-turbo", temperature = 0.7)

# Manually pass Retrived text to LLM 
prompt = f"Based on the Following text, answer the Question: {query}\n\n {retrived_text}"
answer = llm.predict(prompt)

# print the Answer 
print ("Answer", answer)