from .model import GenModel
from .retriever import Retriever


class SmartRAG:
def __init__(self, config):
self.config = config
self.retriever = Retriever(config['embed_model'], faiss_path=config['faiss_path'])
try:
self.retriever.load_index()
except Exception:
pass
self.gen = GenModel(config['model_name'])


def answer(self, question, session_id=None):
# 1) récupérer contextes
contexts = []
if self.retriever.index is not None:
docs = self.retriever.query(question, top_k=self.config.get('top_k', 5))
contexts = [d['text'] for d in docs]


# 2) construire prompt
prompt = """
You are a helpful assistant. Use the following context to answer the question.


Context:
"""
for i, c in enumerate(contexts, 1):
prompt += f"[{i}] {c}\n"
prompt += f"\nQuestion: {question}\nAnswer:"


# 3) génération
gen = self.gen.generate(prompt)
return {
'answer': gen,
'sources': [d.get('id') for d in (docs if 'docs' in locals() else [])]
}