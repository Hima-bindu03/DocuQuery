# qna_engine.py

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader, JSONLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import tempfile

# Load environment variables (GROQ API key)
load_dotenv()

def process_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    # Load document
    if uploaded_file.name.endswith(".pdf"):
        loader = PyPDFDirectoryLoader(os.path.dirname(file_path))
    elif uploaded_file.name.endswith(".json"):
        loader = JSONLoader(file_path=file_path, jq_schema=".data", text_content=False)
    else:
        raise ValueError("Unsupported file type")

    docs = loader.load()

    # Split into chunks
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return splitter.split_documents(docs)

def init_llm():
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.0,
        verbose=True,
    )
    return embedding_function, llm

def build_vector_store(doc_texts, embedding_function):
    return Chroma.from_documents(doc_texts, embedding_function)

def answer_question(question, vector_store, llm):
    retriever = vector_store.as_retriever()
    relevant_docs = retriever.get_relevant_documents(question)
    context = " ".join([doc.page_content for doc in relevant_docs])

    input_text = f"Question: {question}\n\nContext: {context}\n\nAnswer:"
    response = llm.invoke(input_text)
    return response.content
