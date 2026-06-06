# pip install langchain
# pip install langchain-openai
# pip install langchain-chroma
# pip install chromadb

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma

# ----------------------------------
# STEP 1: LLM
# ----------------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

# ----------------------------------
# STEP 2: PROMPT TEMPLATE
# ----------------------------------

prompt = ChatPromptTemplate.from_template(
    """
    Answer the question using the context.

    Context:
    {context}

    Question:
    {question}
    """
)

# ----------------------------------
# STEP 3: DOCUMENTS
# ----------------------------------

docs = [
    Document(
        page_content="OOP stands for Object Oriented Programming."
    ),
    Document(
        page_content="Python supports OOP concepts."
    ),
    Document(
        page_content="Docker is a containerization platform."
    )
]

# ----------------------------------
# STEP 4: EMBEDDINGS
# ----------------------------------

embeddings = OpenAIEmbeddings()

# ----------------------------------
# STEP 5: VECTOR DATABASE
# ----------------------------------

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings
)

# ----------------------------------
# STEP 6: RETRIEVER
# ----------------------------------

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)

# ----------------------------------
# STEP 7: SEARCH
# ----------------------------------

results = retriever.invoke(
    "What is OOP?"
)

context = "\n".join(
    doc.page_content
    for doc in results
)

# ----------------------------------
# STEP 8: BUILD FINAL PROMPT
# ----------------------------------

final_prompt = prompt.invoke(
    {
        "context": context,
        "question": "What is OOP?"
    }
)

# ----------------------------------
# STEP 9: LLM ANSWER
# ----------------------------------

response = llm.invoke(
    final_prompt
)

print(response.content)