
# Intelligent Document Query System using RAG

This project is a Retrieval-Augmented Generation (RAG) based document query system that allows users to upload documents and interact with them using natural language.

The system processes documents, converts them into embeddings, stores them in a vector database, and retrieves relevant information to generate accurate responses.


## Key Features

◼Upload and process documents (PDF, text)
◼Intelligent text chunking
◼Embedding generation using Hugging Face models
◼Fast similarity search using FAISS
◼Chat-based interface for querying documents
◼Runs completely on localhost (no paid APIs required)
## Tech Stack

◼Frontend: Streamlit
◼Backend: Python
◼Framework: LangChain
◼Vector Database: FAISS (CPU)
◼Embeddings: Hugging Face
## How it works

1)Upload document
2)Text is split into smaller chunks
3)Chunks are converted into embeddings
4)Stored in FAISS vector database
5)User asks questions in chat interface
6)Relevant chunks are retrieved
7)Response is generated based on retrieved context


## Installation

1. Clone the repository
```bash
git clone <your-repo-link>
cd <your-project-folder>
```
2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
## Run the Application
```bash
streamlit run app.py
```
Open in browser:
```bash
http://localhost:8501
```
## Project Structure
```bash
├── app.py
├── requirements.txt
├── data/
├── utils/
├── embeddings/
└── README.md
```
## Key Learnings

⏺Practical understanding of RAG architecture
⏺Importance of chunking strategy
⏺Working with vector databases (FAISS)
⏺Running AI systems locally without API dependency
⏺Building end-to-end AI applications
## Future Improvements

⏺Improve response accuracy
⏺Add support for multiple file formats
⏺Optimize retrieval performance
⏺Deploy on cloud


## Author

- Nandhini P (https://github.com/NandhiniPalani10)

