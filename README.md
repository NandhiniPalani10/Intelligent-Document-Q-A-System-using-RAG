AI Document Q&A Web Application (RAG)

This project is a Retrieval-Augmented Generation (RAG) based web application that allows users to ask questions from a document and receive context-aware answers.

Built using Streamlit and LangChain, the application retrieves relevant information from the document and generates responses based on that context.

🚀 Features
📄 Load and process text documents
✂️ Automatic text chunking for better retrieval
🔍 Semantic search using vector embeddings
🧠 Context-based answer generation
⚡ Fast and interactive UI with Streamlit
📊 Efficient similarity search using FAISS
🛠️ Tech Stack
Python
Streamlit
LangChain
FAISS (Vector Database)
HuggingFace / OpenAI (Embeddings & LLM)
📁 Project Structure
rag_project/
│── app.py
│── data.txt
│── requirements.txt
⚙️ Installation
Clone the repository:
git clone https://github.com/your-username/rag-project.git
cd rag-project
Install dependencies:
pip install -r requirements.txt
▶️ Run the Application
python -m streamlit run app.py

Then open in browser:

http://localhost:8501
📌 How It Works
Loads document (data.txt)
Splits text into smaller chunks
Converts text into embeddings
Stores embeddings in FAISS vector database
Retrieves relevant chunks based on user query
Generates answer using retrieved context
🎯 Use Cases
📚 Document-based Q&A
🧾 Knowledge retrieval systems
🤖 AI assistants for text data
📊 Research and learning tools
🚀 Future Improvements
📂 Upload PDF / multiple documents
💬 Chat-style interface
⚡ Faster retrieval with caching
🌐 Deployment on cloud
👩‍💻 Author

Nandhini P

⭐ Acknowledgement

This project is built using modern AI tools and frameworks like LangChain and Streamlit to demonstrate practical implementation of RAG systems.
