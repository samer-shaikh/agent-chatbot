from dotenv import load_dotenv

from langgraph.graph import StateGraph, START,END
from langchain_google_genai import ChatGoogleGenerativeAI

from state import ChatState

load_dotenv()

# **************** making the model *********************
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-pro'
)

# **************** creating the nodes funcions *********************

def chatbot_node(state: ChatState):

    response = llm.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# **************** creating the graph *********************
graph = StateGraph(ChatState)

graph.add_node('chatbot_node',chatbot_node)

graph.add_edge(START,'chatbot_node')
graph.add_edge('chatbot_node',END)

chatbot = graph.compile()

