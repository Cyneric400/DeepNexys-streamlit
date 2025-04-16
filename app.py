import streamlit as st
import llm_man

if 'LLM' not in st.session_state:
    st.session_state.LLM = llm_man.OLLAMA(model_name="tinydolphin")
if 'prompt' not in st.session_state:
    st.session_state.prompt = ''


def send_prompt():
    response = st.session_state.LLM.predict(st.session_state.prompt)
    print(response)
    st.write(response)

st.title("DeepNexys")
st.subheader("Your Hub for New Ideas")


st.file_uploader(label="Upload a PDF", type="pdf", accept_multiple_files=True)

with st.form("nexychat"):
    st.subheader("Chat with Nexy about your notes!")
    cols = st.columns([0.92,0.08], vertical_alignment="bottom")
    with cols[0]:
        prompt = st.text_input(label="Enter a prompt...", key="prompt")
    with cols[1]:
        submit = st.form_submit_button("^", on_click=send_prompt)