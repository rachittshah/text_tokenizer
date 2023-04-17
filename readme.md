# Text Tokenizer

A simple Python library for tokenizing text files and breaking them into overlapping chunks.

## Features

- Count the number of tokens in a text file
- Break a text file into overlapping chunks of specified size
- Convert tokenized text back to a string

## Installation

Install the package from PyPI using pip:

```pip3 install text_tokenizer```


## Usage

Here's an example of how to use the Text Tokenizer library:

```python
from text_tokenizer import Tokenizer

tokenizer = Tokenizer()

filename = "path/to/your/text/file.txt"
token_count = tokenizer.count_tokens(filename)
print(f"Number of tokens: {token_count}")

chunks = tokenizer.break_up_file_to_chunks(filename)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {len(chunk)} tokens")
Replace "path/to/your/text/file.txt" with the path of the file you want to process.
```

Dependencies
- nltk
- requests