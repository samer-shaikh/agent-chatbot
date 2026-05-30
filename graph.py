from dotenv import load_dotenv

from langgraph.graph import StateGraph, START,END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import ToolNode, tools_condition

from state import ChatState
from tools import tools

load_dotenv()

memory = InMemorySaver()

# **************** making the model *********************
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    streaming=True
)

llm_with_tools = llm.bind_tools(tools=tools)

# **************** creating the nodes funcions *********************

def chatbot_node(state: ChatState):

    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# **************** creating the graph *********************
graph = StateGraph(ChatState)

graph.add_node('chatbot_node',chatbot_node)
graph.add_node('tools',ToolNode(tools))

graph.add_edge(START,'chatbot_node')
graph.add_conditional_edges('chatbot_node',tools_condition)
graph.add_edge('tools','chatbot_node')

chatbot = graph.compile(checkpointer=memory)