from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch


class GenModel:
def __init__(self, model_name, device='cpu'):
self.tokenizer = AutoTokenizer.from_pretrained(model_name)
self.model = AutoModelForCausalLM.from_pretrained(model_name)
self.device = device
if device == 'cuda' and torch.cuda.is_available():
self.model.to('cuda')
self.pipe = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer, device=0 if device=='cuda' else -1)


def generate(self, prompt, max_tokens=256, temperature=0.7):
out = self.pipe(prompt, max_length=len(self.tokenizer(prompt)['input_ids']) + max_tokens, do_sample=True, temperature=temperature, num_return_sequences=1)
return out[0]['generated_text']