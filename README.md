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

## 📂 Project Structure

DocuQuery/
├── app.py # Streamlit interface
├── qna_engine.py # File handling, vector DB, LLM logic
├── requirements.txt # Python dependencies
├── .gitignore
├── .env # API key (excluded from Git)
└── README.md

📥 Setup Instructions
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/Hima-bindu03/DocuQuery.git
cd DocuQuery
2. Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate  # macOS/Linux
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add Your .env File
Create a .env file in the root and add your Groq API key:

ini
Copy
Edit
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxx
⚠️ Do NOT share your .env publicly.

🧠 How to Use
Run the app:

bash
Copy
Edit
streamlit run app.py
Upload your PDF or JSON file

Ask any question related to the content

Get AI-generated answers in real time

