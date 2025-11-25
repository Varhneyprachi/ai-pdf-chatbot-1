📄 PDF Question–Answering App (RAG + Ollama + Streamlit)
A simple, fast and fully local PDF Question-Answering Application built using:


LangChain


Ollama (local LLM + embeddings)


Chroma vector store


Streamlit UI


Users can upload a PDF, the app extracts text, chunks it, embeds using Ollama, stores it in Chroma, and answers questions using a local LLM.

🚀 Live Demo (Render Deployment)
👉 Open the deployed app:
https://ai-pdf-chatbot-hzb9.onrender.com/

✨ Features


📄 Upload any PDF


🔍 Extracts and splits text into intelligent chunks


🧠 Embeds using local Ollama embedding model


📚 Stores chunks in Chroma vector DB


🤖 Uses local LLM (Ollama) to generate answers


⚡ Fully offline if Ollama models are downloaded


🛠 Simple Streamlit UI



🧰 Tech Stack
ComponentTechnologyLLMOllama (llama3, llama2, mistral, qwen, etc.)EmbeddingsOllama embeddingsVector DatabaseChromaFrameworkLangChainUIStreamlitLanguagePython

📦 Installation (Local Setup)
1️⃣ Clone the repository
git clone https://github.com/your-username/pdf-qa-rag-system.git
cd pdf-qa-rag-system

2️⃣ Create virtual environment
python -m venv venv

Activate:
Windows
venv\Scripts\activate


3️⃣ Install dependencies
(Add your simple requirements without version numbers)
pip install streamlit
pip install pypdf
pip install langchain
pip install langchain-community
pip install langchain-chroma
pip install langchain-ollama


4️⃣ Install Ollama and pull models
Download Ollama:
https://ollama.com/download
Pull required models:
ollama pull nomic-embed-text
ollama pull llama3.1

(You may replace them with any other local models.)

5️⃣ Run the application
streamlit run app.py

Then open the Streamlit link shown in terminal (usually http://localhost:8501).

🖥 How It Works


Upload a PDF.


App extracts text using PyPDFLoader.


Text is split into overlapping chunks.


Each chunk is embedded using an Ollama embedding model.


Chroma stores those embeddings.


User enters a query.


Semantically similar chunks are retrieved.


LLM (Ollama) generates the answer from the context.



📁 Project Structure
.
├── app.py
├── README.md
├── venv/
└── (optional) data/


🌐 Deployment (Render)
This project is deployed on Render using Streamlit.
Live Demo →
👉 https://ai-pdf-chatbot-hzb9.onrender.com/

🤝 Contributing
Pull requests and improvements are welcome!

📜 License
This project is open-source. Use it, modify it, learn from it.