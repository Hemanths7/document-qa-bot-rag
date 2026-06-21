import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Gemini Client
client_gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ChromaDB
client_db = chromadb.PersistentClient(path="db")
collection = client_db.get_collection(
    name="document_knowledge_base"
)

# Embedding Model
model = SentenceTransformer("all-MiniLM-L6-v2")

st.set_page_config(page_title="Document Q&A Bot", page_icon="📚")

st.title("📚 Document Q&A Bot")
st.write("Upload PDF/DOCX files and ask questions.")

uploaded_files = st.file_uploader(
    "Upload PDF/DOCX Files",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded.")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question:

        query_embedding = model.encode(question).tolist()

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )

        context = "\n\n".join(results["documents"][0])

        prompt = f"""
        Answer only from the context below.

        Context:
        {context}

        Question:
        {question}

        If answer is not present in context,
        say:
        'I cannot find the answer in the provided documents.'
        """

        response = client_gemini.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        st.subheader("Answer")
        st.write(response.text)

        st.subheader("Sources")

        for meta in results["metadatas"][0]:
            st.write(
                f"{meta['source']} (Page {meta['page']})"
            )