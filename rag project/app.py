import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings

# UI
st.title("📄 Simple RAG (No heavy install)")

# Load file
loader = TextLoader("data.txt")
documents = loader.load()

# Split
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# Lightweight embeddings (no download)
embeddings = FakeEmbeddings(size=384)

# Vector DB
db = FAISS.from_documents(texts, embeddings)

# Input
query = st.text_input("Ask a question:")

if query:
    docs = db.similarity_search(query, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    st.write("### Retrieved Context:")
    st.write(context)