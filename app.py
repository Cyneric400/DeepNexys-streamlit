import streamlit as st

st.title("DeepNexys")
st.subheader("Your Hub for New Ideas")

st.file_uploader(label="Upload a PDF", type="pdf", accept_multiple_files=True)


