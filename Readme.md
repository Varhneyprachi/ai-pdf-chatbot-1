# 📄 PDF Question–Answering App (RAG + Ollama + Streamlit)

This project is a simple and powerful **PDF Question-Answering System**.  
It allows users to upload any PDF file and ask questions based on its content.  
Built using **LangChain, Ollama, ChromaDB, and Streamlit**.

---

## 🚀 Live Demo

👉 **Deployed App:**  
https://ai-pdf-chatbot-hzb9.onrender.com/

---

## ✨ Features

- 📄 Upload any PDF file  
- 🔍 Extract and chunk text automatically  
- 🧠 Embedding using **local Ollama models**  
- 📚 Vector search using **ChromaDB**  
- 🤖 Answer generation using **local LLMs (Ollama)**  
- ⚡ Works offline once models are downloaded  
- 🎨 Clean & simple Streamlit UI  

---

## 🛠 Tech Stack

| Component        | Technology Used         |
|------------------|--------------------------|
| Language Model   | Ollama (llama3, etc.)   |
| Embeddings       | Ollama Embeddings       |
| Vector Store     | ChromaDB                |
| Framework        | LangChain               |
| UI Framework     | Streamlit               |
| Programming Lang | Python                  |

---

## 📥 Installation & Setup (Local)

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/your-username/ai-pdf-chatbot-1.git
cd ai-pdf-chatbot-1

### **4️⃣ Install Ollama & Pull Models**

Download Ollama:  
https://ollama.com/download

Then pull the required models:

```bash
ollama pull nomic-embed-text
ollama pull llama3.1

