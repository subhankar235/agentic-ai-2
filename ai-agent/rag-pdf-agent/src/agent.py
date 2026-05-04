# 🧠 What is a “Tool” in your agent?
# A tool is just:
# 👉 a function the agent can call when it needs help
# Nothing fancy. No magic.



# agent is a decision-maker that chooses whether to use tools (like your RAG search) or answer directly.

# 1. Read your question
# 2. Think:
#    - Do I need a tool?
# 3. If yes → call tool
# 4. Get result
# 5. Generate final answer

# agent.py

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent, ToolNode

from dotenv import load_dotenv
import os

from src.vectordb import load_db
from src.rag_chain import create_rag_chain

# ✅ Load env (for OpenRouter key)
load_dotenv()

# ✅ Load DB + RAG once (performance fix)
db = load_db()
qa_chain = create_rag_chain(db)


# 🔧 TOOL
@tool
def search_notes(query: str) -> str:
    """
    ALWAYS use this tool to answer ANY question about the user, their goals, plans, notes, or personal information.
    Do NOT answer from general knowledge if the question is about the user.
    """
    result = qa_chain.invoke({"query": query})   # ✅ FIXED
    return result["result"]


# 🤖 AGENT RUNNER
class AgentRunner:
    def __init__(self, agent_executor):
        self.agent_executor = agent_executor

    def run(self, query):
        result = self.agent_executor.invoke({
            "messages": [HumanMessage(content=query)]
        })

        # ✅ Safe return
        if result["messages"]:
            return result["messages"][-1].content
        return "No response generated."


# 🚀 BUILD AGENT
def build_agent():
    tools = [search_notes]

    # ✅ OpenRouter LLM config (FIXED)
    llm = ChatOpenAI(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        default_headers={
            "HTTP-Referer": "http://localhost",
            "X-Title": "RAG Agent"
        }
    )

    llm_with_tools = llm.bind_tools(tools)
    tool_node = ToolNode(tools)

    # ✅ Create agent ONCE (not every query)
    agent_executor = create_react_agent(llm_with_tools, tool_node)

    return AgentRunner(agent_executor)