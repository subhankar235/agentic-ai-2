# 🧠 RAG PDF / Notes AI Agent (LangChain + ChromaDB)

A Retrieval-Augmented Generation (RAG) based AI agent that can answer questions from your personal notes or documents using LangChain, ChromaDB, and LLMs.

---

## 🚀 Features

* 📄 Load personal notes (TXT / PDF)
* ✂️ Automatic text chunking
* 🔢 Embedding generation using LLM embeddings
* 🗄️ Vector database with ChromaDB
* 🤖 AI Agent with tool usage (LangGraph)
* 🔍 Context-aware answers from your own data

---

## 📁 Project Structure

```
rag-agent/
│
├── app.py                 # Main CLI app
├── config.py             # Configs (chunk size, paths)
├── requirements.txt
├── README.md
│
├── data/
│   └── notes.txt         # Your personal data
│
├── db/                   # Vector DB (auto-generated, ignored in git)
│
├── src/
│   ├── ingest.py         # Load → chunk → embed → store
│   ├── vectordb.py       # Load vector DB
│   ├── rag_chain.py      # Retrieval QA pipeline
│   └── agent.py          # Agent + tool logic
│
└── .env                  # API keys (not committed)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/your-username/rag-agent.git
cd rag-agent
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Add API key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

> If using OpenRouter:

```
OPENAI_API_KEY=sk-or-xxxx
```

---

### 5. Add your data

Put your notes in:

```
data/notes.txt
```

---

### 6. Run the app

```
python app.py
```

---

## 🧠 How it works

1. **Ingestion**

   * Reads your notes
   * Splits into chunks
   * Converts to embeddings
   * Stores in ChromaDB (`db/`)

2. **Query**

   * Your question is embedded
   * Vector DB finds similar chunks
   * LLM generates answer using context

3. **Agent**

   * Decides when to use RAG tool
   * Returns final answer

---

## 🧪 Example Questions

```
What is my goal?
What are my priorities?
Summarize my notes
What should I focus on first?
```

---

## ⚠️ Important Notes

* `db/` is auto-generated → do NOT commit
* `.env` contains secrets → do NOT commit
* Re-run ingestion if you update your notes

---

## 🛠️ Tech Stack

* LangChain
* LangGraph
* ChromaDB
* OpenAI / OpenRouter
* Python

---

## 📌 Future Improvements

* Web UI (Streamlit / React)
* Multi-document support
* Chat history (memory)
* Deployment (Render / Vercel)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License.
