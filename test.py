from dotenv import load_dotenv

from langgraph.graph import StateGraph, START,END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage
from state import ChatState

load_dotenv()

memory = InMemorySaver()
config = {"configurable": {"thread_id": "session_1"}}

# **************** making the model *********************
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-pro',
    streaming=True
)


for chunk in llm.stream(
    [HumanMessage(content="Write a short story in 100 words")]
):
    print(chunk.content, end="", flush=True)