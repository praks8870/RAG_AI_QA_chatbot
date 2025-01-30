# 📄 AI Research Paper Q&A (RAG) App  

## 🚀 Project Overview  
This is a **Retrieval-Augmented Generation (RAG) application** that allows users to upload AI research papers (PDFs), ask questions, and receive **context-aware answers** using **semantic search** and an **LLM (GPT-4 or GPT-3.5-turbo)**.  

## 🔹 Features  
✔ **Upload Research Papers** – Supports **PDF format**.  
✔ **Semantic Search** – Retrieves relevant sections using **FAISS embeddings**.  
✔ **AI-Powered Q&A** – Uses **OpenAI GPT models** to generate responses.  
✔ **User-Friendly Interface** – Built with **Streamlit** for easy interaction.  
✔ **Multi-Paper Support** (Optional) – Query across multiple PDFs.  

## 🛠️ Tech Stack  

| Component        | Tool/Library Used |
|-----------------|------------------|
| **Frontend**    | Streamlit |
| **Text Extraction** | PyPDF2 / PDFMiner |
| **Vectorization** | Sentence Transformers (all-MiniLM-L6-v2) |
| **Vector Database** | FAISS |
| **LLM** | OpenAI GPT-4 / GPT-3.5-turbo |
| **Deployment** | Streamlit Cloud / Hugging Face Spaces |

## 📂 Project Structure  

│── app.py                 # Main Streamlit app
│── preprocessing.py       # Extracts and chunks text from PDFs
│── embeddings.py          # Creates and stores embeddings using FAISS
│── query_processor.py     # Performs search & calls OpenAI API
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
│── data/                  # Folder for uploaded PDFs
│── .venv/                 # Virtual environment (optional)



## ⚙️ Setup & Installation  

<!-- ### 1️⃣ Clone the Repository  
```bash
        # git clone https://github.com
        # cd ragai -->

### Create Virtual Environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

### Install Dependencies
pip install -r requirements.txt

### Running the app in local 
streamlit run app.py
