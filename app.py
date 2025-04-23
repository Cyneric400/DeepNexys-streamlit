import streamlit as st
import llm_man
from VTI64_db import dbman

if 'model' not in st.session_state:
    st.session_state.model = "gemma3"
if 'LLM' not in st.session_state:
    st.session_state.LLM = llm_man.OLLAMA(model_name=st.session_state.model)
if 'prompt' not in st.session_state:
    st.session_state.prompt = ''
if 'messages' not in st.session_state:
    st.session_state.messages = []
#if 'chat_msg' not in st.session_state:
 #   st.session_state.chat_msg = ''

def read_files():
    for file in st.session_state.files:
        dbman.add_uploaded_file(file)


def send_prompt():
    response = st.session_state.LLM.predict(st.session_state.prompt)
    print(response)
    st.write(response)


def send_chat_msg():
    return st.session_state.LLM.predict(st.session_state.chat_msg)

def change_model():
    st.session_state.LLM = llm_man.OLLAMA(st.session_state.model)

st.title("DeepNexys")
st.subheader("Your Hub for New Ideas")

main_cols = st.columns(3)
with main_cols[0]:
    st.markdown("Upload files and chat with a...um...*mostly* state-of-the-art LLM about them!")
with main_cols[1]:
   st.selectbox(label="Select a model for Nexy to run on", key="model", options=["gemma3", "llama3.2:1b"], on_change=change_model)
with main_cols[2]:
    st.write("Please be patient with the slow response times, our *cough* state-of-the-art *cough* AI needs a more powerful server :'(")

st.subheader("Chat with Nexy about your notes!")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        

if prompt_input := st.chat_input("Send a message to Nexy", key="chat_msg"):
    with st.chat_message("user"):
        st.markdown(prompt_input)
    st.session_state.messages.append({"role": "user", "content": prompt_input})

    response = send_chat_msg()
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


st.file_uploader(label="Upload a PDF", key="files", type="pdf", accept_multiple_files=True, on_change=read_files)
