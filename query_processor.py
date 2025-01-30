from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

# Load the pre-trained model and tokenizer
model_name = "google/flan-t5-base" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

class QueryProcessor:
    def __init__(self, embed_store):
        self.embed_store = embed_store

    def generate_answer(self, query, top_k=3):
        """Retrieve relevant chunks & generate an answer using the specified model."""
        retrieved_chunks = self.embed_store.search(query, top_k) 
        context = "\n".join(retrieved_chunks)

        prompt = f"Based on the following research content, answer the query:\n\n{context}\n\nQuery: {query}\nAnswer:"
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids

        # Generate answer using the Hugging Face Transformers model
        output = model.generate(input_ids, max_length=256, num_beams=5, no_repeat_ngram_size=2) 
        output_text = tokenizer.decode(output[0], skip_special_tokens=True)

        return output_text

