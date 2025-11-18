import os
import json
from pathlib import Path
from chatbot.retriever import Retriever


DATA_DIR = Path('data/docs')


def load_docs(data_dir):
docs = []
for p in data_dir.glob('**/*'):
if p.is_file() and p.suffix.lower() in ['.txt', '.md']:
text = p.read_text(encoding='utf-8')
docs.append({'id': str(p), 'text': text})
return docs


if __name__ == '__main__':
retr = Retriever('sentence-transformers/all-MiniLM-L6-v2', faiss_path='embeddings/faiss_index.bin')
docs = load_docs(DATA_DIR)
retr.build_index(docs)
print('Index built with', len(docs), 'documents')