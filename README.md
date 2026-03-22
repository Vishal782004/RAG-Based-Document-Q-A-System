# RAG-Based-Document-Q-A-System
A production-ready **Retrieval-Augmented Generation (RAG)** system that lets you ask questions from any PDF document and get accurate, context-aware answers using **MistralAI** and **ChromaDB**.


## 🚀 Features

- 📄 **Load and process PDF documents automatically**
- ✂️ **Smart text chunking with overlap** for better context retention
- 🔍 **Semantic search** using HuggingFace Embeddings
- 🧠 **MMR (Maximal Marginal Relevance)** retrieval for diverse, relevant results
- 💬 **Conversational Q&A** powered by Mistral AI (*mistral-small*)
- 💾 **Persistent vector storage** using ChromaDB
- 🚫 **Hallucination-free responses** — answers only from document context

---

## 🛠️ Tech Stack

| Component        | Technology                          |
|-----------------|------------------------------------|
| LLM             | MistralAI (mistral-small-2506)     |
| Embeddings      | HuggingFace (all-MiniLM-L6-v2)     |
| Vector Store    | ChromaDB                           |
| PDF Loader      | LangChain PyPDFLoader              |
| Text Splitting  | LangChain RecursiveCharacterTextSplitter |
| Framework       | LangChain                          |

---

## 📁 Project Structure

```
rag-document-qa/
│
├── Documents_loader/
│   └── deeplearning.pdf
│
├── chroma_db/
│
├── create_database.py
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Vishal782004/rag-document-qa.git
cd rag-document-qa
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file:

```
MISTRAL_API_KEY=your_mistral_api_key_here
```

Get your API key from: https://console.mistral.ai

---

## 📌 How to Use

### 🔹 Step 1: Add Your PDF

Place your PDF inside `Documents_loader/` and update:

```python
data = PyPDFLoader(r"Documents_loader/your_document.pdf")
```

---

### 🔹 Step 2: Create the Vector Database

```bash
python create_database.py
```

This will:
- Load and parse your PDF  
- Split into chunks *(size: 1000, overlap: 200)*  
- Generate embeddings  
- Store in ChromaDB  

---

### 🔹 Step 3: Start the Q&A System

```bash
python main.py
```

Example:

```
You : What is backpropagation?

AI : Backpropagation is a method used to train neural networks...
```

👉 Type `0` to exit

---

## 🧠 How It Works

```
PDF Document
     ↓
Text Chunking
     ↓
Embeddings
     ↓
Vector Store (ChromaDB)
     ↓
Query → MMR Retrieval
     ↓
LLM (MistralAI)
     ↓
Answer
```

---

## 📦 Requirements

- langchain  
- langchain-community  
- langchain-mistralai  
- langchain-core  
- chromadb  
- sentence-transformers  
- pypdf  
- python-dotenv  

Install:

```bash
pip install -r requirements.txt
```

---

## 🐛 Known Issues & Fixes

- ❌ `load_dotenv` not called → ✅ use `load_dotenv()`
- ❌ `if quary == 0` → ✅ use `if quary == "0": break`

---

## 🙋‍♂️ Author

**Vishal Pawar**

- 🔗 LinkedIn  
- 💻 GitHub  

---

## 📄 License

This project is **open-source** under the **MIT License**.
