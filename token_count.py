import platform
import os
import requests as re
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')


class Tokenizer:
    @staticmethod
    def get_versions():
        return {
            'Python': platform.python_version(),
            're': re.__version__,
            'nltk': nltk.__version__,
        }

    def count_tokens(self, filename):
        with open(filename, 'r') as f:
            text = f.read()
        tokens = word_tokenize(text)
        return len(tokens)

    @staticmethod
    def break_up_file(tokens, chunk_size, overlap_size):
        if len(tokens) <= chunk_size:
            yield tokens
        else:
            chunk = tokens[:chunk_size]
            yield chunk
            yield from Tokenizer.break_up_file(tokens[chunk_size - overlap_size:], chunk_size, overlap_size)

    def break_up_file_to_chunks(self, filename, chunk_size=2000, overlap_size=100):
        with open(filename, 'r') as f:
            text = f.read()
        tokens = word_tokenize(text)
        return list(Tokenizer.break_up_file(tokens, chunk_size, overlap_size))

    @staticmethod
    def convert_to_detokenized_text(tokenized_text):
        prompt_text = " ".join(tokenized_text)
        prompt_text = prompt_text.replace(" 's", "'s")
        return prompt_text

    @staticmethod
    def convert_to_prompt_text(tokenized_text):
        prompt_text = " ".join(tokenized_text)
        return prompt_text
