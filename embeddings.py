import os

from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import Embeddings

load_dotenv()

_credentials = Credentials(
    url=os.getenv("URL"),
    api_key=os.getenv("API_KEY")
)

# Hosted embedding model on watsonx.ai (no local ONNX / onnxruntime needed).
_embedder = Embeddings(
    model_id="ibm/granite-embedding-278m-multilingual",
    credentials=_credentials,
    project_id=os.getenv("PROJECT_ID")
)


def embed_texts(texts):
    """Return a list of embedding vectors for the given list of strings."""
    return _embedder.embed_documents(texts=list(texts))
