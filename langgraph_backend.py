from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

from langgraph.graph.message import add_messages


#state
class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


#chat niode
def chat_node(state: ChatState):

    # take user query from state
    messages = state['messages']

    # send to llm
    response = llm.invoke(messages)

    # response store state
    return {'messages': [response]}


#checkpointer
checkpointer=MemorySaver()

#graph
graph = StateGraph(ChatState)

# add nodes
graph.add_node('chat_node', chat_node)

#add edges
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)


