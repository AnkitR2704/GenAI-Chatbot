import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model='mistral-small', temperature=0.9)

st.set_page_config(page_title="Mistral Chatbot", page_icon="🤖")

st.title("🤖 Mistral Chatbot")
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    
    response = model.invoke(user_input)
    st.session_state['messages'].append({"role": "bot", "content": response.content})
    
    st.session_state.input = ""

for msg in st.session_state['messages']:
    if msg['role'] == 'user':
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")