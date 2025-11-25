from langchain_community.document_loaders import PyPDFLoader
import os
import streamlit as st
import tempfile
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
import uuid


def extract_text_from_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return ' '.join([doc.page_content for doc in documents])


def split_text_into_chunks(text: str, chunk_size: int = 2000, chunk_overlap: int = 200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    docs = text_splitter.create_documents([text])

    for d in docs:
        d.metadata["id"] = str(uuid.uuid4())

    return docs


# Embeddings model
embeddings = OllamaEmbeddings(model="nomic-embed-text")


def create_vector_store(chunks):
    ids = [doc.metadata["id"] for doc in chunks]
    return Chroma.from_documents(chunks, embeddings, ids=ids)


def generate_response(vector_store, query):
    # Low-RAM safe LLM
    llm = Ollama(model="gemma:2b")

    # Smarter prompt
    prompt = ChatPromptTemplate.from_template(
        """Answer the following question based on the provided context. 
        If the context is incomplete, give your best logical guess:
        <context>
        {context}
        </context>

        Question: {input}"""
    )

    chain = create_stuff_documents_chain(llm, prompt)

    # Retrieve more chunks for better answers
    matching_docs = vector_store.similarity_search(query, k=10)

    response = chain.invoke(
        {"input": query, "context": matching_docs}
    )

    return response


st.title("PDF Question-Answering App")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        temp_file_path = temp_file.name

    st.write("Processing uploaded PDF...")
    raw_text = extract_text_from_pdf(temp_file_path)

    if raw_text:
        st.write("Splitting text into chunks...")
        chunks = split_text_into_chunks(raw_text)

        st.write("Creating vector store...")
        vector_store = create_vector_store(chunks)

        query = st.text_input("Enter your query:")

        if query:
            st.write("Processing your query...")
            answer = generate_response(vector_store, query)
            st.write("Answer:", answer)

    os.unlink(temp_file_path)

else:
    st.warning("Please upload a PDF file to proceed.")
