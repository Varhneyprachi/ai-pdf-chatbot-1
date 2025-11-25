📄 PDF Question–Answering App (RAG + Ollama + Streamlit)

This project is a simple and powerful PDF Question-Answering System.
It allows users to upload any PDF file and ask questions based on its content.
Built using LangChain, Ollama, ChromaDB, and Streamlit.

🚀 Live Demo

👉 Deployed App:
https://ai-pdf-chatbot-hzb9.onrender.com/

✨ Features

📄 Upload any PDF file

🔍 Extract and chunk text automatically

🧠 Embedding using local Ollama models

📚 Vector search using ChromaDB

🤖 Answer generation using local LLMs (Ollama)

⚡ Works offline once models are downloaded

🎨 Clean and simple Streamlit UI

🛠 Tech Stack
Component	Technology Used
Language Model	Ollama (llama3, etc.)
Embeddings	Ollama Embeddings
Vector Store	ChromaDB
Framework	LangChain
UI Framework	Streamlit
Language	Python
📥 Installation & Setup (Local)
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-pdf-chatbot-1.git
cd ai-pdf-chatbot-1

2️⃣ Create a Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate

3️⃣ Install Dependencies

(Using simple, conflict-free installs)

pip install streamlit
pip install pypdf
pip install langchain
pip install langchain-community
pip install langchain-chroma
pip install langchain-ollama

4️⃣ Install Ollama & Pull Models

Download Ollama from:
https://ollama.com/download

Pull required models:

ollama pull nomic-embed-text
ollama pull llama3.1


(You can use any other local models you prefer.)

5️⃣ Run the Application
streamlit run app.py


The app will start at:

http://localhost:8501

🧠 How It Works

User uploads a PDF.

Text is extracted using PyPDFLoader.

The text is chunked using RecursiveCharacterTextSplitter.

Chunks are embedded using Ollama embedding models.

Embeddings are stored in ChromaDB.

When the user asks a question:

Relevant chunks are retrieved via vector search

The local LLM generates an answer based on retrieved context

📁 Project Structure
.
├── app.py
├── README.md
├── requirements.txt (optional)
└── venv/ (not included in Git)

🌐 Deployment

This project is deployed on Render (free tier).

Live URL:
👉 https://ai-pdf-chatbot-hzb9.onrender.com/

🤝 Contributing

Pull requests, improvements, and suggestions are welcome!

📜 License

This project is open-source.
Feel free to use, modify, or enhance it.
