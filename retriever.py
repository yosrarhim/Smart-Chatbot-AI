from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from pathlib import Path


class Retriever:
def __init__(self, embed_model_name, faiss_path=None):
self.embed_model = SentenceTransformer(embed_model_name)
self.faiss_path = faiss_path
self.index = None
self.docs = []


def encode(self, texts):
return self.embed_model.encode(texts, convert_to_numpy=True)


def build_index(self, docs:list):
# docs: list of dicts {'id': str, 'text': str}
self.docs = docs
emb = self.encode([d['text'] for d in docs]).astype('float32')
dim = emb.shape[1]
index = faiss.IndexFlatIP(dim)
faiss.normalize_L2(emb)
index.add(emb)
self.index = index
if self.faiss_path:
faiss.write_index(index, self.faiss_path)


def load_index(self):
if self.faiss_path and os.path.exists(self.faiss_path):
self.index = faiss.read_index(self.faiss_path)


def query(self, text, top_k=5):
emb = self.encode([text]).astype('float32')
faiss.normalize_L2(emb)
D, I = self.index.search(emb, top_k)
results = []
for idx in I[0]:
results.append(self.docs[idx])
return results