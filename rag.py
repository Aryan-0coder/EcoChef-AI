import os
import chromadb

from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

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

    retrieved_chunk = "\n\n".join(retrieved_chunks)

    prompt = f"""
    You are EcoChef AI.

    Answer naturally in a helpful way.

    Give only the answer.
    Do not mention the context.
    Do not explain where the information came from.

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
print(get_answer("How should I store potatoes?"))
