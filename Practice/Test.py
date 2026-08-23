# Create the basic Local HuggingFace_Model using openAI.
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline,HuggingFaceEndpoint
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_anthropic import 
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv


load_dotenv()

model = OpenAIEmbeddings(model = "text-embedding-3-small", dimensions= 32)
model1 = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
model2 = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-2 ")

query = input("Enter Query to embedding?")
document = [
    from pathlib import Path

content = """AI PERSONAL KNOWLEDGE DOCUMENT
==============================

Purpose
-------
This document is intended to be used as a knowledge/context file for an AI assistant that answers questions about Chiranjeevi. It consolidates publicly referenced profile information, technical background, projects, interests, and links. The AI should distinguish verified/public information from information that may have changed and should not invent missing details.

PRIMARY PUBLIC PROFILES
-----------------------
LinkedIn:
https://www.linkedin.com/in/chiranjeevi-38249a1b1/

GitHub:
https://github.com/midnighteagle/

Portfolio:
https://portfoliosakshat.netlify.app/

IDENTITY / NAME
---------------
Preferred/current name reference:
Chiranjeevi

GitHub identity/organization reference:
Midnight Eagle / @midnighteagle

Important:
- Do not confuse the person Chiranjeevi with the GitHub handle/brand "midnighteagle".
- Older references may contain the name "Akshat Arya"; the more recent resume/profile context identifies the user as Chiranjeevi. If a question depends on legal identity, do not assume without confirmation.

EDUCATION
---------
Degree:
B.Tech in Artificial Intelligence & Data Science (AI & Data Science)

University/affiliation:
RGPV (Rajiv Gandhi Proudyogiki Vishwavidyalaya)

College reference:
JNCT Bhopal / Jai Narain Institute of Technology

CGPA:
7.02

School education references:
Class 12: BSEB, Mirza Ghalib College, Gaya — 56%
Class 10: BSEB — 65%

Career stage:
Fresher / early-career technology learner and developer.

TECHNICAL SKILLS
----------------
Programming languages:
- Python
- C++
- Java
- C

Data Structures / Algorithms:
- Data Structures and Algorithms
- Competitive programming / LeetCode practice

AI / Machine Learning:
- Machine Learning
- Data Science
- Deep Learning
- Neural networks
- CNN concepts
- MLP
- Backpropagation
- Gradient descent
- Empirical Risk Minimization
- Regularization
- Data mining
- OLAP / data warehousing concepts
- RAG and embeddings
- LangChain
- LLM application development

Python ecosystem:
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook
- Streamlit
- LangChain
- LangGraph
- OpenAI integrations
- Google Gemini integrations
- Hugging Face integrations
- FAISS

Web development:
- HTML
- CSS
- JavaScript
- React
- React 18
- Tailwind CSS
- Vite

Backend:
- Node.js
- Express.js
- Mongoose
- MongoDB Atlas
- JWT authentication

Other libraries/tools referenced:
- lucide-react
- jspdf
- jspdf-autotable
- xlsx
- react-icons
- framer-motion
- Cloudinary
- Helmet
- CORS
- dotenv
- express-rate-limit
- bcryptjs

CURRENT AI / LANGCHAIN LEARNING
-------------------------------
The user is actively learning modern LLM application development using Python and LangChain.

Topics recently practiced:
- LLMs and Chat Models
- PromptTemplate
- Runnable / LCEL syntax
- Chains using the pipe operator
- LLMChain concepts and their modern replacements
- Output parsers
- ResponseSchema
- Structured output
- Text/document loaders
- Text splitting
- Embeddings
- Vector stores
- FAISS
- Retrieval
- RAG pipelines
- OpenAI models and embeddings
- Google Gemini models and embeddings
- Anthropic Claude models
- Hugging Face text-generation models
- ChatHuggingFace
- HuggingFaceEndpoint
- Streamlit AI applications
- PDF/document processing

Important LangChain preference:
The user often wants examples using current LangChain packages and APIs rather than old/deprecated imports.

Examples of current package style used:
- langchain_openai
- langchain_google_genai
- langchain_anthropic
- langchain_huggingface
- langchain_community
- langchain_core
- langchain_text_splitters

The user frequently asks why older tutorials/imports do not work with newer LangChain versions. Explain package migrations clearly and provide current equivalents.

AI PROJECT INTERESTS
--------------------
1. English-to-Hindi movie dubbing AI
The user previously explored creating an AI tool that converts an English movie into Hindi dubbed audio.
Preferred implementation direction:
- Python
- Possibly Streamlit
- AI pipeline involving speech/audio processing, translation, and text-to-speech.

2. RAG / document question-answering
The user is learning to:
- Load documents
- Split documents into chunks
- Generate embeddings
- Store vectors in FAISS
- Retrieve relevant chunks
- Send retrieved context to an LLM
- Generate answers.

3. AI / LLM learning applications
The user experiments with:
- OpenAI
- Google Gemini
- Anthropic
- Hugging Face
- LangChain
- Streamlit
- Local/hosted LLM workflows.

4. Timetable Generator
A significant software project involving automatic timetable generation.

Known requirements:
- Odd/even semesters
- Fixed 35 periods per week
- Monday-Friday
- 7 periods per day
- Lunch between periods IV and V
- Theory classes
- Practical classes requiring consecutive periods
- Extra classes
- Internship
- Mentor
- Library
- Teacher availability
- Teacher conflict prevention
- Teacher daily-count limits
- Subject repetition rules
- Backtracking / heuristic scheduling.

Known implementation concepts:
- timetableGeneratorCore.js
- slotHelpers
- schedulingHeuristics
- Backtracking
- Placement priority based on class type
- Hard constraints and scheduling heuristics

5. Midnight Eagle
The user has discussed a company/conglomerate concept named "Midnight Eagle", inspired by the idea of a diversified business group.

Proposed sectors:
- Technologies
- Healthcare
- Consumer care

The user has also worked on a company portfolio concept with:
- Vite frontend
- React
- Tailwind CSS
- Node.js / Express backend
- MongoDB Atlas
- Mongoose
- JWT
- Admin-editable content.

MIDNIGHT EAGLE GITHUB
---------------------
Public GitHub profile:
https://github.com/midnighteagle/

The public GitHub page currently shows:
- 34 repositories
- 8 stars
- 2 followers
- 6 following

Public repositories visible on the profile include:
- midnight-eagle — Jupyter Notebook
- my-work — C assignment
- my-work- — C assignment 2
- gui — Python/Pygame game project
- python-projects — Python
- house-prediction-ML- — Jupyter Notebook / machine learning house prediction project

These repository counts and contents can change over time. Treat the GitHub profile as the authoritative source for the latest repository list.

PORTFOLIO
---------
Portfolio:
https://portfoliosakshat.netlify.app/

The portfolio is associated with the user's developer profile. The user has previously wanted a dynamic, admin-editable portfolio and has worked with React/Vite/Tailwind and backend technologies.

DEVELOPMENT PROJECT: COMPANY PORTFOLIO
--------------------------------------
Project concept:
Midnight Eagle company/conglomerate portfolio.

Frontend:
- Vite
- React
- Tailwind CSS

Backend:
- Node.js
- Express
- MongoDB Atlas
- Mongoose
- JWT

Backend areas previously discussed:
- Authentication
- Analytics
- Blog
- Careers
- Contact
- Projects
- Services
- Team members

API approach:
- Frontend uses an API wrapper with BASE_URL = "/api"
- Vite proxy can forward /api to a local Express server.

DEVELOPMENT STYLE / PREFERENCES
--------------------------------
When answering technical questions for the user:
- Prefer Python when the user is working on AI/LLM applications.
- Give complete runnable examples when requested.
- Explain errors directly from the traceback.
- When LangChain has changed an API, show the modern package/import and explain the old equivalent.
- Avoid relying on deprecated APIs when a current API exists.
- For simple learning examples, avoid unnecessary abstractions.
- The user often prefers understanding code step-by-step.
- If the user explicitly asks for "without making chain", show direct model invocation rather than forcing LCEL.
- When demonstrating chat models, remember that LangChain chat models commonly return an AIMessage and the generated text is usually in result.content.
- For plain LLM/text-generation models, the return value may be a string.
- For structured output, explain the schema/parser clearly.

RECENT LANGCHAIN ERROR PATTERNS
--------------------------------
The user has encountered these kinds of issues:

1. OpenAI:
Using a chat model such as gpt-4o with the old `OpenAI` completion interface caused:
"This is a chat model and not supported in the v1/completions endpoint."

Correct conceptual distinction:
- `OpenAI` is for completion-style LLMs.
- `ChatOpenAI` is for chat models.

2. Invalid OpenAI model ID:
A typo such as:
"gpt-5.6,"
causes an invalid model ID error. Model names must be exact and should not contain accidental spaces/commas.

3. Gemini:
Google Generative AI chat models return AIMessage-like objects. Use:
result.content
to get generated text rather than printing the whole object.

4. Hugging Face:
`HuggingFaceEndpoint` requires a Hugging Face API token.
Authentication errors are different from model/provider availability errors.

5. Hugging Face provider error:
"The requested model ... is not supported by any provider you have enabled."
This means authentication succeeded but the selected model is not available through the enabled inference provider.

6. Google embeddings:
`GoogleGenerativeAIEmbeddings` expects:
model="..."
not:
model_name="..."

7. ResponseSchema:
The correct field is:
description="..."
not:
descriptions="..."

8. TextLoader:
TextLoader expects a text file. It should not be used to load a DOCX file. Use an appropriate DOCX loader for Word documents.

9. LangChain package migration:
Older tutorials may use imports such as:
langchain.document_loaders
langchain.embeddings
langchain.vectorstores
langchain.llms

Modern integrations are generally split into packages such as:
langchain_community
langchain_openai
langchain_google_genai
langchain_anthropic
langchain_huggingface
langchain_text_splitters
langchain_core

CAREER / PROFESSIONAL PROFILE
-----------------------------
The user is developing toward AI, Data Science, Machine Learning, and software development roles.

Profile positioning:
- B.Tech AI & Data Science student/graduate-level learner
- Fresher / early-career developer
- Python and AI/ML focused
- Full-stack development experience/interest
- LLM and RAG application development interest
- Strong interest in practical projects.

RESUME-RELATED INFORMATION
---------------------------
Previously referenced professional summary:
A result-oriented fresher with knowledge of programming languages, database management, C/C++, Java, Python, Data Structures and Algorithms, Machine Learning, Data Science, and related Python libraries.

The user has also described knowledge/experience with:
- Object-oriented programming through Java
- Database management
- Leadership/management concepts
- Web development
- AI/ML.

Do not invent employment history, years of experience, certifications, job titles, or achievements unless they are explicitly present in the latest source/profile.

LEARNING INTERESTS
------------------
The user frequently studies:
- Machine Learning
- Deep Learning
- Data Science
- Data Mining
- Computer Networks
- Data Warehousing
- OLAP
- Neural Networks
- LangChain
- Generative AI
- RAG
- Embeddings
- LLMs
- Python programming
- DSA
- Java
- C/C++
- Full-stack development.

ACADEMIC TOPICS PREVIOUSLY STUDIED
-----------------------------------
- OSI reference model
- Computer network design issues
- Connection-oriented vs connectionless services
- Data warehouse architecture
- Knowledge discovery process
- Data preprocessing
- ROLAP, MOLAP, HOLAP
- OLTP vs OLAP
- Data mining classification
- Clustering
- Apriori
- FP-Growth
- Neural networks
- McCulloch-Pitts neural model
- Empirical Risk Minimization
- Gradient descent
- Backpropagation
- CNNs
- RBMs
- IoT protocols.

HOW AN AI ASSISTANT SHOULD ANSWER QUESTIONS ABOUT THE USER
------------------------------------------------------------
If asked "Who is Chiranjeevi?":
Describe him as a B.Tech AI & Data Science student/early-career developer with interests and experience spanning Python, AI/ML, Data Science, LLM applications, LangChain, web development, and software projects.

If asked about GitHub:
Use:
https://github.com/midnighteagle/
and treat the live GitHub profile as the source of truth for current repositories.

If asked about LinkedIn:
Use:
https://www.linkedin.com/in/chiranjeevi-38249a1b1/
and avoid inventing information that cannot be verified from the profile.

If asked about portfolio:
Use:
https://portfoliosakshat.netlify.app/
and describe it as the user's developer portfolio.

If asked about projects:
Mention only projects supported by this document or the linked public profiles. Relevant known projects include:
- Midnight Eagle company portfolio
- Timetable Generator
- House Prediction ML
- Python projects
- Pygame GUI/game project
- English-to-Hindi movie dubbing AI concept
- RAG/document QA experiments
- LangChain/LLM learning applications.

FACT-CHECKING RULES
-------------------
1. Public profile information can change. Verify live GitHub/LinkedIn/portfolio data when necessary.
2. Do not fabricate employment, salary, company affiliation, awards, certifications, contact information, or personal details.
3. Do not expose API keys, passwords, tokens, secrets, or credentials.
4. Do not treat technical experiments as completed production systems unless the user explicitly says they are completed.
5. Distinguish "project idea", "learning project", "prototype", and "production project".
6. If two sources conflict, prefer the most recent source or ask the user when the distinction is important.
7. Do not infer sensitive personal attributes from projects, interests, or location.
8. GitHub repository information should be treated as dynamic.
9. The user is actively learning; do not describe every technology they've experimented with as professional-level expertise.

SOURCE LINKS
------------
LinkedIn:
https://www.linkedin.com/in/chiranjeevi-38249a1b1/

GitHub:
https://github.com/midnighteagle/

Portfolio:
https://portfoliosakshat.netlify.app/

END OF KNOWLEDGE DOCUMENT
"""

path = Path("/mnt/data/chiranjeevi_ai_knowledge_document.txt")
path.write_text(content, encoding="utf-8")
print(path)

]
Doc_Embedding = model.embed_documents(document)
Query_Embedding = model.embed_query(query)

score = cosine_similarity([Query_Embedding], Doc_Embedding)[0] # it shows the 2D document similarity.

print(list(enumerate(score)))
index,score = sorted(list(enumerate(score)),key = lambda x:x[1]) [-1] # x-> index : x-> score[1] list value index[0,1]

print(Query_Embedding)
print(query)
print(document[index])
print("Similar_score is: ", score)




