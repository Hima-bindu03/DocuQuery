import streamlit as st
from qna_engine import process_file, init_llm, build_vector_store, answer_question

# Initialize session state
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'llm' not in st.session_state:
    st.session_state.llm = None
if 'processed' not in st.session_state:
    st.session_state.processed = False

st.title(" Q&A Model for Your Document")

# Step 1: Upload file
if not st.session_state.processed:
    st.write("👋 Hello! Please upload your PDF or JSON document to start.")
    uploaded_file = st.file_uploader("Upload file", type=["pdf", "json"])

    if uploaded_file:
        st.success(f"Uploaded {uploaded_file.name}")
        doc_texts = process_file(uploaded_file)
        embedding_function, llm = init_llm()
        vector_store = build_vector_store(doc_texts, embedding_function)

        # Save in session state
        st.session_state.vector_store = vector_store
        st.session_state.llm = llm
        st.session_state.processed = True

        st.success("✅ Document processed! Now you can ask your questions.")

# Step 2: Ask questions
if st.session_state.processed:
    st.write("📄 Document is ready. Please enter your question below.")
    user_question = st.text_input("Your Question:")

    if user_question:
        answer = answer_question(user_question, st.session_state.vector_store, st.session_state.llm)
        st.write("### 🤖 Answer:")
        st.write(answer)

    if st.button("🔄 Upload a New File"):
        # Reset everything
        st.session_state.vector_store = None
        st.session_state.llm = None
        st.session_state.processed = False
