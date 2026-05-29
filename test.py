from graph import chatbot
from langchain_core.messages import HumanMessage

response = chatbot.invoke(
    {
        "messages": [
            HumanMessage(content="Hello")
        ]
    }
)

print(response["messages"][-1].content)