from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()


model = ChatOpenAI()


st.header('Research Tool')


# Creation of prompt :

paper_input = st.selectbox( " Select Reasearch Paper Name", [ "Attention Is All You Need ", "BERT: Pre-training of Deep Bidirectional Transformers ", "GPT-3: Language Models are Few-Shot Learner", "Diffusion Models Beat GANs on Image Synthesis"])

Style_input = st.selectbox("Select Expalanation Style", ["Beginner-Friendly", "Technical ", "Core-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explaination Length", ["Short(1-2 paragraphs)","Medium(3-5 paragraph)", "Long (detailed explaination)"])


template = load_prompt('template.json')



#template



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
    input_variables=['paper_input','Style_input', 'length_input'],
    validate_template = True
)




# # fill the placeHolder 
# prompt = template.invoke({
#     'paper_input' : paper_input,
#     'Style_input' : Style_input,
#     'length_input': length_input
# })



if st.button('summerize'):
    chain = template | model
    result = chain.invoke({
        'paper_input' : paper_input,
        'Style_input' : Style_input,
        'length_input': length_input
    })
    
    
    # # fill the placeHolder 
    # prompt = template.invoke({
    #     'paper_input' : paper_input,
    #     'Style_input' : Style_input,
    #     'length_input': length_input
    # })
    # result = model.invoke(prompt)
    
    
    st.write(result.content)