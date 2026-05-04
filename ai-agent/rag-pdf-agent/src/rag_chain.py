# It connects your vector DB-question and embedding (memory) with the LLM (thinking engine)

from langchain_classic.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from config import MODEL_NAME
from dotenv import load_dotenv
import os

load_dotenv()
def create_rag_chain(db):
    retriever = db.as_retriever()

    llm = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "My RAG Agent"
    }
)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
         return_source_documents=True   
    )

    return qa