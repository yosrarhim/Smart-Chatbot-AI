import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


def load_config():
return {
'model_name': os.getenv('HF_MODEL', 'gpt2'),
'embed_model': os.getenv('EMBED_MODEL', 'sentence-transformers/all-MiniLM-L6-v2'),
'faiss_path': str(BASE_DIR / 'embeddings' / 'faiss_index.bin'),
'top_k': int(os.getenv('TOP_K', 5)),
}