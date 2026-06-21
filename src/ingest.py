import os
from pypdf import PdfReader
from docx import Document

DATA_FOLDER = "data"


def extract_pdf(file_path):
    documents = []

    reader = PdfReader(file_path)

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text:
            documents.append({
                "text": text,
                "metadata": {
                    "source": os.path.basename(file_path),
                    "page": page_num
                }
            })

    return documents


def extract_docx(file_path):
    documents = []

    doc = Document(file_path)

    full_text = []

    for para in doc.paragraphs:
        if para.text.strip():
            full_text.append(para.text)

    documents.append({
        "text": "\n".join(full_text),
        "metadata": {
            "source": os.path.basename(file_path),
            "page": 1
        }
    })

    return documents


def load_documents():
    all_documents = []

    for file_name in os.listdir(DATA_FOLDER):

        file_path = os.path.join(DATA_FOLDER, file_name)

        if file_name.endswith(".pdf"):
            all_documents.extend(extract_pdf(file_path))

        elif file_name.endswith(".docx"):
            all_documents.extend(extract_docx(file_path))

    return all_documents


def chunk_documents(documents, chunk_size=1000, chunk_overlap=200):

    chunks = []

    for doc in documents:

        text = doc["text"]
        metadata = doc["metadata"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            chunks.append({
                "text": chunk_text,
                "metadata": {
                    "source": metadata["source"],
                    "page": metadata["page"]
                }
            })

            start += (chunk_size - chunk_overlap)

    return chunks


if __name__ == "__main__":

    documents = load_documents()

    chunks = chunk_documents(documents)

    print(f"\nTotal Documents: {len(documents)}")
    print(f"Total Chunks: {len(chunks)}\n")

    for chunk in chunks[:5]:
        print("=" * 50)
        print(chunk["metadata"])
        print(chunk["text"][:300])
        print()