import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
from dotenv import load_dotenv
import os
import tempfile

from ingest import extract_pdf, extract_docx, chunk_documents

load_dotenv()

# Gemini Client
client_gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Embedding Model
model = SentenceTransformer("all-MiniLM-L6-v2")

st.set_page_config(
    page_title="Document Q&A Bot",
    page_icon="📚"
)

st.title("📚 Document Q&A Bot")
st.write("Upload PDF/DOCX files and ask questions.")

uploaded_files = st.file_uploader(
    "Upload PDF/DOCX Files",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

collection = None

if uploaded_files:

    st.success(f"{len(uploaded_files)} file(s) uploaded.")

    all_docs = []

    for uploaded_file in uploaded_files:

        suffix = "." + uploaded_file.name.split(".")[-1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as tmp:

            tmp.write(uploaded_file.getvalue())
            temp_path = tmp.name

        if uploaded_file.name.lower().endswith(".pdf"):
            all_docs.extend(
                extract_pdf(temp_path)
            )

        elif uploaded_file.name.lower().endswith(".docx"):
            all_docs.extend(
                extract_docx(temp_path)
            )

    chunks = chunk_documents(all_docs)

    client_db = chromadb.Client()

    collection = client_db.create_collection(
        name="uploaded_docs"
    )

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = model.encode(texts).tolist()

    collection.add(
        ids=[
            str(i)
            for i in range(len(texts))
        ],
        documents=texts,
        embeddings=embeddings,
        metadatas=[
            chunk["metadata"]
            for chunk in chunks
        ]
    )

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if not uploaded_files:
        st.error(
            "Please upload a PDF or DOCX file first."
        )

    elif not question:
        st.error(
            "Please enter a question."
        )

    else:

        query_embedding = model.encode(
            question
        ).tolist()

        results = collection.query(
            query_embeddings=[
                query_embedding
            ],
            n_results=3
        )

        context = "\n\n".join(
            results["documents"][0]
        )

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