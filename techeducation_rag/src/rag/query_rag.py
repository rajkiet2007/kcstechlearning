import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAISS index


# Load chunks


# OpenAI client
client = OpenAI()

class QueryRAG:
    # Retrieve relevant chunks
    def retrieve(self ,query, k=3):
        index = faiss.read_index("index.faiss")
        with open("chunks.pkl", "rb") as f:
            chunks = pickle.load(f)
        query_embedding = model.encode([query])
        distances, indices = index.search(np.array(query_embedding), k)

        return [chunks[i] for i in indices[0]]

    # Generate answer
    def generate_answer(self,query):
        retrieved_chunks = self.retrieve(query)
        context = "\n\n".join(retrieved_chunks)

        prompt = f"""
        Answer based only on the context below.

        Context:
        {context}

        Question:
        {query}
        """

        response = client.responses.create(
            model="gpt-5",
            input=prompt
        )

        return response.output_text