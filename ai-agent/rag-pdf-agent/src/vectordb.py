# What it does:
# Stores embeddings
# Finds similar chunks for a query
# using chroma-db


from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from config import PERSIST_DIR

def load_db():
    embeddings = OpenAIEmbeddings()
    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings
    )