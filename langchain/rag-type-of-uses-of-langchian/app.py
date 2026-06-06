from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

# ----------------------------------
# STEP 1: LOAD PDF
# ----------------------------------

loader = PyPDFLoader("python_notes.pdf")

documents = loader.load()

print("Documents Loaded")
print(len(documents))


# STEP 2: CHUNKING
splitter= RecursiveCharacterTextSplitter(
 chunk_size=500,
 chunk_overlap=100 
)
chunks = splitter.split_documents(documents)

print("Chunks Created")
print(len(chunks))

# STEP 3: EMBEDDINGS
embeddings = OpenAIEmbeddings()
# STEP 4: VECTOR STORE in chroma db


vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Stored in Chroma")


# STEP 5: RETRIEVER
# Take my Chroma DB
# ↓
# Convert it into a search engine
# ↓
# Return top 3 matching chunks

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# ----------------------------------
# STEP 6: SEARCH
# ----------------------------------

results = retriever.invoke(
    "What is OOP?"
)


# display result---