import PyPDF2
import io

def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file uploaded via Streamlit."""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)  # Read binary data
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text if text else "No text extracted."
    except Exception as e:
        print(f"Error extracting text: {e}")
        return "Error extracting text."