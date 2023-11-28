import os
import openai
import streamlit as st

from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
# Load the variables from .env
load_dotenv()

# Access the API key
openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key


st.set_page_config(page_title="LangChain", page_icon=":earth_americas:", layout="wide")
st.header("Hey there! Ask me about anything and I'll try to find similar things from my database!")

embeddings = OpenAIEmbeddings()

from langchain.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path='mydata.csv')

data = loader.load()

db = FAISS.from_documents(data, embeddings)

def get_text():
    input_text = st.text_input("Ask me anything!", key="input")
    return input_text

user_input = get_text()
submit = st.button("Find similar things in my DB")
if submit:
    docs = db.similarity_search(user_input)
    st.subheader("Top Matches:")
    st.text(docs[0].page_content)
    st.text(docs[1].page_content)

