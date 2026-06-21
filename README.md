# 📚 Document Q&A Bot using RAG

A Retrieval-Augmented Generation (RAG) based Question Answering system that enables users to upload PDF and DOCX documents, ask natural language questions, and receive context-aware answers grounded in the uploaded documents.

The application uses document ingestion, chunking, embeddings, vector search, and Google Gemini to provide accurate answers along with source citations.

---

## 🚀 Live Demo

**Streamlit Application**

https://document-app-bot-rag-dxjmo2v3ajrdgucqgstpg5.streamlit.app/

**GitHub Repository**

https://github.com/Hemanths7/document-qa-bot-rag

---

# 📸 Screenshots

## Home Page

![Home Page](screenshots/ui-home.png)

---

## Uploading Documents

![Upload Documents](screenshots/upload-doc.png)

---

## Answer Generation

![Answer Output](screenshots/answer-output.png)

---

## Document Indexing

![Indexing Terminal](screenshots/indexing-terminal.png)

---

## Project Structure

![Project Structure](screenshots/github-structure.png)

---

# 🎯 Assignment Objective

Build a complete Retrieval-Augmented Generation (RAG) pipeline capable of:

* Loading documents
* Chunking text
* Generating embeddings
* Storing embeddings in a vector database
* Retrieving relevant chunks
* Generating grounded answers using an LLM
* Providing source citations

---

# 📂 Project Structure

```text
document-qa-bot-rag/
│
├── data/
│   ├── AI INDEX REPORT 2025.pdf
│   ├── AI RISK MANAGEMENT FRAMEWORK.pdf
│   ├── NCSC_Quick_Guide_Phishing.docx
│   ├── The-Game-of-Cricket.docx
│   └── Use of GenAI in research.pdf
│
├── screenshots/
│
├── src/
│   ├── app.py
│   ├── ingest.py
│   ├── index_documents.py
│   ├── query.py
│   └── config.py
│
├── requirements.txt
├── runtime.txt
├── README.md
└── .env
```

---

# 🏗 Architecture Overview

```text
Documents (PDF / DOCX)
          │
          ▼
Document Ingestion
          │
          ▼
Text Extraction
          │
          ▼
Chunking
          │
          ▼
Embedding Generation
(all-MiniLM-L6-v2)
          │
          ▼
ChromaDB Vector Store
          │
          ▼
Similarity Search
          │
          ▼
Retrieved Chunks
          │
          ▼
Google Gemini
          │
          ▼
Answer + Citations
```

---

# ⚙️ Tech Stack

### Programming Language

* Python 3.11

### Frontend

* Streamlit

### Vector Database

* ChromaDB

### Embedding Model

* Sentence Transformers
* all-MiniLM-L6-v2

### Large Language Model

* Google Gemini 2.5 Flash

### Document Processing

* PyPDF
* python-docx

### Environment Management

* python-dotenv

---

# 📄 Knowledge Base Documents

The application uses the following documents:

1. AI INDEX REPORT 2025.pdf
2. AI RISK MANAGEMENT FRAMEWORK.pdf
3. NCSC_Quick_Guide_Phishing.docx
4. The-Game-of-Cricket.docx
5. Use of GenAI in research.pdf

These documents provide diverse domains including:

* Artificial Intelligence
* Cyber Security
* Research Methodology
* Sports

---

# ✂️ Chunking Strategy

### Strategy Used

Fixed-size chunking with overlap.

```python
chunk_size = 1000
chunk_overlap = 200
```

### Why This Strategy?

* Preserves contextual information.
* Prevents information loss at chunk boundaries.
* Improves retrieval quality.
* Simple and efficient for beginner RAG pipelines.

### Metadata Stored

Each chunk stores:

* Source filename
* Page number

---

# 🧠 Embedding Model

### Model

```text
all-MiniLM-L6-v2
```

### Why?

* Lightweight
* Fast embedding generation
* Good semantic similarity performance
* Popular choice for RAG systems

### Batch Embedding

Embeddings are generated in batches:

```python
texts = [chunk["text"] for chunk in chunks]
embeddings = model.encode(texts)
```

This improves performance compared to embedding one chunk at a time.

---

# 🗄 Vector Database

### Database Used

ChromaDB

### Why ChromaDB?

* Easy integration with Python
* Fast similarity search
* Lightweight
* Open source
* Suitable for small and medium RAG projects

---

# 🔄 RAG Workflow

### Step 1

Upload PDF or DOCX documents.

### Step 2

Extract text from uploaded files.

### Step 3

Split documents into overlapping chunks.

### Step 4

Generate embeddings using Sentence Transformers.

### Step 5

Store embeddings in ChromaDB.

### Step 6

Accept user question.

### Step 7

Generate query embedding.

### Step 8

Retrieve top-k relevant chunks.

### Step 9

Send retrieved context and question to Gemini.

### Step 10

Display answer and source citations.

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API Key from Google AI Studio.

⚠️ Never commit API keys to GitHub.

---

# 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/Hemanths7/document-qa-bot-rag.git
```

Move into the project:

```bash
cd document-qa-bot-rag
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Run Streamlit:

```bash
streamlit run src/app.py
```

Open:

```text
http://localhost:8501
```

---

# 💡 Example Queries

### AI Research

* What are the uses of Generative AI in research?
* How can AI support literature reviews?

### Cyber Security

* What is phishing?
* How can phishing attacks be prevented?

### AI Governance

* What is an AI Risk Management Framework?

### Cricket

* How many players are there in a cricket team?
* What are the basic rules of cricket?

---

# 📌 Sample Output

### Question

```text
What is phishing?
```

### Answer

```text
Phishing is a cyber attack where attackers impersonate trusted entities to steal sensitive information such as passwords, banking details, or personal data.
```

### Source

```text
NCSC_Quick_Guide_Phishing.docx (Page 1)
```

---

# ⚠️ Known Limitations

* OCR support for scanned PDFs is not implemented.
* Retrieval quality depends on chunk quality.
* Large documents may increase processing time.
* Multi-document reasoning can be improved further.
* Responses depend on the relevance of retrieved chunks.

---

# 🎥 Demonstration Video

The project demonstration includes:

* Project structure overview
* Document ingestion
* Chunking and indexing
* Streamlit application walkthrough
* Five sample queries
* Source citation display
* Handling unanswerable questions
* Technical design explanation

---

# 👨‍💻 Author

**Hemanth Shivarathri**

B.Tech – Computer Science & Engineering

JB Institute of Engineering and Technology

Hyderabad, India

GitHub: https://github.com/Hemanths7

---

# ✅ Assignment Requirements Covered

* Document Ingestion
* PDF and DOCX Support
* Text Chunking
* Chunk Overlap
* Metadata Storage
* Batch Embeddings
* ChromaDB Vector Database
* Similarity Search
* Google Gemini Integration
* Grounded Answer Generation
* Source Citations
* Streamlit User Interface
* Public GitHub Repository
* Cloud Deployment
