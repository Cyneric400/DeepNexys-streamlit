import streamlit as st
import llm_man

if 'LLM' not in st.session_state:
    st.session_state.LLM = llm_man.OLLAMA(model_name="gemma3")
if 'prompt' not in st.session_state:
    st.session_state.prompt = ''
if 'messages' not in st.session_state:
    st.session_state.messages = []
#if 'chat_msg' not in st.session_state:
 #   st.session_state.chat_msg = ''


def send_prompt():
    response = st.session_state.LLM.predict(st.session_state.prompt)
    print(response)
    st.write(response)


def send_chat_msg():
    return st.session_state.LLM.predict(st.session_state.chat_msg)

st.title("DeepNexys")
st.subheader("Your Hub for New Ideas")


st.file_uploader(label="Upload a PDF", type="pdf", accept_multiple_files=True)

st.subheader("Chat with Nexy about your notes - now in a new, improved format!")
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