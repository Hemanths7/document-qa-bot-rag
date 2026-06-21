import chromadb
from sentence_transformers import SentenceTransformer

from ingest import load_documents, chunk_documents

print("Loading documents...")

documents = load_documents()

chunks = chunk_documents(documents)

print("Total Chunks:", len(chunks))

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [chunk["text"] for chunk in chunks]

print("Generating embeddings...")

embeddings = model.encode(texts).tolist()

client = chromadb.PersistentClient(path="db")

try:
    client.delete_collection("document_knowledge_base")
except:
    pass

collection = client.create_collection(
    name="document_knowledge_base"
)

ids = [f"chunk_{i}" for i in range(len(chunks))]

metadatas = [chunk["metadata"] for chunk in chunks]

collection.add(
    ids=ids,
    documents=texts,
    embeddings=embeddings,
    metadatas=metadatas
)

print("\nIndexing Complete!")
print("Stored Chunks:", collection.count())