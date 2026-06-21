import os
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Gemini Client
client_gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ChromaDB
client_db = chromadb.PersistentClient(path="db")

collection = client_db.get_collection(
    name="document_knowledge_base"
)

# Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

while True:

    query = input("\nAsk a question (or type exit): ")

    if query.lower() == "exit":
        break

    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = ""

    citations = []

    for doc, meta in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):

        source = meta["source"]
        page = meta["page"]

        citations.append(
            f"{source} (Page {page})"
        )

        context += f"\n\nSource: {source}, Page: {page}\n"
        context += doc

    prompt = f"""
You are a professional document question answering assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, say:

"I cannot find the answer in the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""

    response = client_gemini.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\n" + "=" * 80)
    print("ANSWER")
    print("=" * 80)

    print(response.text)

    print("\nSOURCES:")

    for citation in set(citations):
        print("-", citation)