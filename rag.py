import os
import chromadb

from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()
from setup_db import create_database
create_database()

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="food_knowledge"
)

credentials = Credentials(
    url=os.getenv("URL"),
    api_key=os.getenv("API_KEY")
)

model = ModelInference(
    model_id="ibm/granite-4-h-small",
    credentials=credentials,
    project_id=os.getenv("PROJECT_ID"),
    params={
        "max_new_tokens": 700,
        "temperature": 0.3
    }
)

def get_answer(query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    retrieved_chunks = results["documents"][0]

    if not retrieved_chunks:
        return (
            "I don't have enough information in my knowledge base to answer that food-related question.",
            []
        )   

    retrieved_chunk = "\n\n".join(retrieved_chunks)

    prompt = f"""
    You are EcoChef AI.

    You specialize only in:

    - Food storage
    - Recipes
    - Nutrition
    - Sustainability
    - Food waste reduction

    Use only the provided context.

    If the context does not contain enough information, reply:

    "I don't have enough information in my knowledge base to answer that food-related question."

    Context:
    {retrieved_chunk}

    Question:
    {query}

    Answer:
    """

    response = model.generate_text(
        prompt=prompt,
        raw_response=True
    )

    answer = response["results"][0]["generated_text"].strip()

    return answer, retrieved_chunks
