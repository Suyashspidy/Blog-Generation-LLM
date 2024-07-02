import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
import asyncio

async def getLLamaresponse(input_text, no_words, blog_style):
    try:
        llm = CTransformers(
            model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
            model_type='llama',
            config={'max_new_tokens': 200, 'temperature': 0.7}  # Adjusted for better performance
        )

        template = """
            Write a blog for {blog_style} job profile for a topic {input_text}
            within {no_words} words.
        """

        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", 'no_words'],
            template=template
        )

        response = await asyncio.to_thread(llm.invoke, prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
        return response
    except Exception as e:
        st.error(f"Error generating blog: {e}")
        return None

def save_blog(blog_content, topic):
    try:
        with open(f"{topic}.txt", "w") as file:
            file.write(blog_content)
        st.success(f"Blog saved as {topic}.txt")
    except Exception as e:
        st.error(f"Error saving blog: {e}")

st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🦾',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.markdown("""
    <style>
    .stApp {
        background-color: #1e1e1e;
        color: white;
    }
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
    }
    div.stTextInput > label {
        color: white;
    }
    div.stNumberInput > label {
        color: white;
    }
    div.stSelectbox > label {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.header("Generate Blogs 🦾")

input_text = st.text_input("Enter the Blog Topic")

col1, col2, col3 = st.columns([5, 3, 2])

with col1:
    no_words = st.number_input('No of Words', min_value=10, max_value=10000, value=500)

with col2:
    blog_style = st.selectbox('Writing the blog for', 
                              ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

if submit:
    if not input_text:
        st.error("Please enter a blog topic")
    else:
        with st.spinner("Generating blog..."):
            response = asyncio.run(getLLamaresponse(input_text, no_words, blog_style))
        if response:
            st.write(response)
            if st.button("Save Blog"):
                save_blog(response, input_text)
