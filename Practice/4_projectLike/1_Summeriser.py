from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# import the streamlit as st
import streamlit as st

# from langchain_core ke prompt se load prompt and promptTemplate import kro.
from langchain_core.prompts import PromptTemplate, load_prompt , prompt



# load the ENv 
load_dotenv()




# configure the Model
ChatModel = ChatOpenAI()

# create the header of name research tool
st.header('Reasearch Tool')




# create the prompt
paper_input = st.selectbox("Select Reasearch paper ", ["Atteention Is All You Need", "BERT: Pre-Training of Deep Bidirectional Transformer", "GPT-3: Langauge Models are few-Shot Learner", "Diffusion Models Beat GANs on Image Synthesis"] )

Style_input = st.selectbox("Select Explaination style", ["Biginner friendly", "Technical", "Core-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explaination length", ["Short(1-2 Paragraph)", "Medium (3-5 Paragraph)", "Long(Detailed Explaination)"])




# Prompt_Templates creation

template = PromptTemplate(
    template = """
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explaination Style: {Style_input}
    Explaination Length: {length_input}
    
    
    1. Mathematical Details:
        - Include relevent mathematical equations if present in the paper.
        - Explain the mathematical concepts using simple, intitutive code. snippets where   applicable.
    2. Analogies:
        - Use relatable analogies to simplify complex ideas.
    If certain information is not available in the paper, respond with: "Insufficint information available" instead of guessing.
    Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """, 
    input_variables= ['paper_input', 'Style_input', 'length_input'],
    validate_template = True
    
)

# Now I'm Streamlit make a user button get Summeries 

# if st.button("summaries"):
#     prompt = template.invoke({
#         'paper_input': paper_input,
#         'Style_input': Style_input,
#         'length_input': length_input
        
#     })
# Response = ChatModel.invoke(prompt)

if st.button('summaries'):
    chain = template | ChatModel
    result = chain.invoke({
        'paper_input': paper_input,
        'Style_input': Style_input,
        'length_input': length_input
    })
    
    st.write(result.content)