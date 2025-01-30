import streamlit as st
from pdf_processing import extract_text_from_pdf
from preprocessing import preprocess_and_chunk
from embeddings import EmbeddingStore
from query_processor import QueryProcessor

# Initialize components
embed_store = EmbeddingStore()
query_processor = QueryProcessor(embed_store)

st.title("📄 AI Research Paper Q&A (RAG)")

# File Upload
uploaded_file = st.file_uploader("Upload a Research Paper (PDF)", type="pdf")
if uploaded_file:
    with st.spinner("Extracting text..."):
        raw_text = extract_text_from_pdf(uploaded_file)
        
        if "Error extracting text" in raw_text or raw_text.strip() == "":
            st.error("Failed to extract text from the PDF. Please upload a valid document.")
        else:
            text_chunks = preprocess_and_chunk(raw_text)
            embed_store.add_text_chunks(text_chunks)
            st.success("Paper processed successfully! ✅")
# Query Input
query = st.text_input("Ask a question about the paper:")
if query:
    with st.spinner("Searching and generating answer..."):
        answer = query_processor.generate_answer(query)
        st.subheader("💡 Answer:")
        st.write(answer)
