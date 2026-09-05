import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage 
import uuid

#*************************** UTILITY FUNCTIONS ****************************

def generate_thread_id():
    thread_id=uuid.uuid4()
    return thread_id    

def reset_chat():
    thread_id=generate_thread_id()
    st.session_state['thread_id']=thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_converstion(thread_id):
    return chatbot.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']




#st.session_state : it is a dictionary ,whose content reamin as it is even after re-running of whole script
if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads']=[ ]


add_thread(st.session_state['thread_id'])


#************************************  SIDEBAR UI *************************************
st.sidebar.title('LangGraph Chatbot')


if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.subheader('My conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id']=thread_id
        messages=load_converstion(thread_id)

        temp_message=[]

        for message in messages:
            if isinstance(message, HumanMessage):
                role='user'
            else:
                 role='assistant'

            temp_message.append({'role':role, 'content': message.content})

        st.session_state['message_history']=temp_message



# ***********************************  MAIN UI  *****************************
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input=st.chat_input('Type Here')

if user_input:

    #first add message to message history
    st.session_state['message_history'].append({'role':'user', 'content':user_input})
    with st.chat_message('user'):
        st.text(user_input)


    CONFIG={'configurable': {'thread_id': st.session_state['thread_id']}}


    #st.session_state['message_history'].append({'role':'assistant', 'content':user_input})
    with st.chat_message('assistant'):
        ai_message=st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )
    st.session_state['message_history'].append({'role':'assistant', 'content':user_input})

    