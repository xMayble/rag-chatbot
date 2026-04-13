import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("📄 RAG Chatbot")
st.write("Upload a PDF and ask questions about it!")

# PDF Upload Section
st.subheader("Step 1: Upload a PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Uploading and processing..."):
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        response = requests.post(f"{API_URL}/upload", files=files)
        
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error("Something went wrong with the upload.")

# Question Section
st.subheader("Step 2: Ask a Question")
question = st.text_input("Ask anything about your document...")

if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            response = requests.post(
                f"{API_URL}/ask",
                json={"question": question}
            )
            
            if response.status_code == 200:
                st.write("### Answer:")
                st.write(response.json()["answer"])
            else:
                st.error("Something went wrong. Is the API running?")
    else:
        st.warning("Please enter a question first!")