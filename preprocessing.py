import re

def preprocess_and_chunk(text, chunk_size=300):
    """
    Cleans extracted text and splits it into chunks of approximately `chunk_size` words.

    Args:
        text (str): The extracted text from the PDF.
        chunk_size (int): Number of words per chunk.

    Returns:
        List[str]: A list of text chunks.
    """

    # Step 1: Clean text
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespaces & line breaks
    text = re.sub(r'\n+', ' ', text)  # Remove excessive new lines

    # Step 2: Split into words and create chunks
    words = text.split()
    chunks = [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]

    return chunks

# Example usage
if __name__ == "__main__":
    sample_text = """This is an example research paper text. It contains multiple sentences and paragraphs.
                     The goal of this function is to clean and break it into smaller chunks for better processing."""
    processed_chunks = preprocess_and_chunk(sample_text)
    
    for i, chunk in enumerate(processed_chunks):
        print(f"Chunk {i+1}:\n{chunk}\n")
