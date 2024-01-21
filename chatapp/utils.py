# chatbotapp/utils.py
from transformers import GPTNeoForCausalLM, GPT2Tokenizer ,GPT2LMHeadModel
import torch


    # return model, tokenizer
def load_local_gpt2_model():
    model_path = 'local_model_gpt2'
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    return model, tokenizer

