# 📄 DocuQuery

DocuQuery is an intelligent Q&A application that allows users to upload **PDF** or **JSON** documents and ask natural language questions about their contents. It uses **LangChain**, **Chroma vector store**, and **Groq’s Llama 3 model** to retrieve contextually accurate answers from your documents via an intuitive **Streamlit interface**.

---

## 🚀 Features

- 📁 Upload PDF or JSON documents
- 🔍 Ask context-aware questions about uploaded files
- ⚡ Fast and relevant answers using vector search and Groq LLM
- 🧠 Embeddings powered by HuggingFace (`all-MiniLM-L6-v2`)
- 🧩 Modular code (frontend in `app.py`, logic in `qna_engine.py`)

---

## 🛠️ Tech Stack

| Component        | Technology                  |
|------------------|------------------------------|
| UI               | Streamlit                   |
| Embeddings       | HuggingFace Sentence Transformers |
| Vector Store     | Chroma                      |
| LLM              | Groq Llama 3 (`llama-3.1-8b-instant`) |
| Orchestration    | LangChain                   |
| File Support     | PDF, JSON                   |

---


## 📥 Setup Instructions
### 1. Clone the Repo
git clone https://github.com/Hima-bindu03/DocuQuery.git
cd DocuQuery

### 2. Create and Activate a Virtual Environment

*Windows*
python -m venv venv
venv\Scripts\activate    
---
*macOS/Linux*
source venv/bin/activate  # macOS/Linux
---
### 3. Install Dependencies

pip install -r requirements.txt

### 4. Add Your .env File
Create a .env file in the root and add your Groq API key:

GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxx.

## 🔐 Environment Variables

This project uses a `.env` file to store sensitive environment variables like your Groq API key.

### 🚫 Do NOT Commit `.env`

Make sure your `.env` file is listed in `.gitignore` so that it is never tracked by Git or pushed to GitHub. Committing secrets can expose your API keys and pose a serious security risk.

### ✅ Steps to Setup Locally

1. Create a `.env` file in the project root:

GROQ_API_KEY=your_groq_api_key_here

2. Do **not** share or upload your `.env` file.

3. A sample `.env.example` is provided to guide other developers.



#### 📁 .gitignore

Ensure that `.env` is listed in your `.gitignore`:

.env

✅ Add to your .gitignore file

In your root directory, make sure your .gitignore includes this line:

.env

✅ This prevents Git from tracking the .env file going forward.


## Run the app:

streamlit run app.py

Upload your PDF or JSON file

Ask any question related to the content

Get AI-generated answers in real time



