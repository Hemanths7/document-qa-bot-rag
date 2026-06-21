# Document Q&A Bot using RAG (Retrieval-Augmented Generation)

## Overview

This project is a Retrieval-Augmented Generation (RAG) based Document Question Answering Bot built using Python, ChromaDB, Sentence Transformers, and Google Gemini.

The system allows users to ask natural language questions about a collection of documents. Instead of relying solely on the language model's training data, the system retrieves relevant information from a custom document knowledge base and generates grounded answers with source citations.

The project demonstrates the complete RAG pipeline including document ingestion, chunking, embedding generation, vector storage, semantic retrieval, and LLM-powered answer generation.

---

# Features

* PDF and DOCX document support
* Automatic text extraction
* Metadata tracking (source file and page number)
* Text chunking with overlap
* Semantic embeddings using Sentence Transformers
* Persistent vector database using ChromaDB
* Similarity-based retrieval
* Grounded answer generation using Gemini 2.5 Flash
* Source citations included in answers
* Interactive command-line interface
* Hallucination prevention through retrieval grounding

---

# Tech Stack

## Language

* Python 3.11

## Libraries

* chromadb
* sentence-transformers
* pypdf
* python-docx
* python-dotenv
* google-genai
* tqdm

## Embedding Model

* all-MiniLM-L6-v2

Reason:

* Lightweight
* Fast
* Produces high-quality semantic embeddings
* Suitable for local RAG systems

## Vector Database

* ChromaDB

Reason:

* Lightweight
* Persistent local storage
* Easy integration with Python
* No external server required

## Language Model

* Gemini 2.5 Flash

Reason:

* Fast response generation
* Strong reasoning capabilities
* Cost-effective for RAG applications

---

# Architecture

```text
Documents (PDF / DOCX)
            |
            v
Text Extraction
            |
            v
Chunking + Overlap
            |
            v
SentenceTransformer Embeddings
            |
            v
ChromaDB Vector Database
            |
            v
User Query
            |
            v
Query Embedding
            |
            v
Top-K Similarity Search
            |
            v
Retrieved Context
            |
            v
Gemini 2.5 Flash
            |
            v
Grounded Answer + Citations
```

---

# Project Structure

```text
document-qa-bot/
│
├── data/
│   ├── AI INDEX REPORT 2025.pdf
│   ├── AI RISK MANAGEMENT FRAMEWORK.pdf
│   ├── Use of GenAI in research.pdf
│   ├── NCSC_Quick_Guide_Phishing.docx
│   └── The-Game-of-Cricket.docx
│
├── db/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── ingest.py
│   ├── index_documents.py
│   ├── query.py
│   └── app.py
│
├── requirements.txt
├── README.md
└── .env
```

---

# Chunking Strategy

The project uses a fixed-size chunking strategy.

Parameters:

```python
chunk_size = 1000
chunk_overlap = 200
```

Why overlap?

When important information lies at chunk boundaries, overlap preserves context and improves retrieval quality.

Example:

```text
Chunk 1 -> Characters 0-1000
Chunk 2 -> Characters 800-1800
```

The shared overlap helps maintain semantic continuity.

---

# Embedding Strategy

The project uses:

```text
all-MiniLM-L6-v2
```

Each chunk is converted into a 384-dimensional vector representation.

The embeddings capture semantic meaning, allowing similarity search based on meaning rather than exact keywords.

---

# Retrieval Process

When a user asks a question:

1. The question is embedded using the same embedding model.
2. ChromaDB performs similarity search.
3. Top 3 most relevant chunks are retrieved.
4. Retrieved chunks are passed as context to Gemini.
5. Gemini generates a grounded response using only the retrieved information.

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd document-qa-bot
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Never commit API keys to GitHub.

---

# Build Vector Database

Run:

```bash
python src/index_documents.py
```

This performs:

* Document loading
* Chunking
* Embedding generation
* ChromaDB indexing

---

# Run the Bot

```bash
python src/query.py
```

Example:

```text
Ask a question:
What is phishing?
```

---

# Example Queries

## AI

```text
What are the major AI trends in 2025?
```

## Cyber Security

```text
What is phishing?
```

```text
What are the different types of phishing attacks?
```

## Generative AI

```text
What is Generative AI?
```

## Research

```text
How is AI used in research?
```

## Out-of-Scope Question

```text
Who won the FIFA World Cup 2022?
```

Expected Response:

```text
I cannot find the answer in the provided documents.
```

---

# Hallucination Prevention

The system uses Retrieval-Augmented Generation (RAG).

The language model is explicitly instructed to answer only from retrieved context.

If information is not found in the retrieved documents, the model responds:

```text
I cannot find the answer in the provided documents.
```

This prevents unsupported or fabricated answers.

---

# Results

Dataset Statistics:

```text
Documents Loaded: 95
Chunks Generated: 312
Embedding Dimension: 384
```

The system successfully retrieves relevant document chunks and generates grounded answers with source citations.

---

# Known Limitations

* Retrieval quality depends on chunk size.
* OCR-based scanned PDFs are not currently supported.
* Supports English documents only.
* Citations are limited to filename and page number.
* No reranking model is currently implemented.

---

# Future Improvements

* Streamlit Web Interface
* Hybrid Search (Keyword + Semantic)
* Cross-Encoder Reranking
* OCR Support
* Multi-document Citations
* Conversation Memory
* Document Upload Interface

---

# Author

Hemanth Shivarathri

B.Tech Computer Science and Engineering

AI Engineering Internship Assignment

2026
