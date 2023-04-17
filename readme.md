# Text Tokenizer

A simple Python library for tokenizing text files and breaking them into overlapping chunks.

## Features

- Count the number of tokens in a text file
- Break a text file into overlapping chunks of specified size
- Convert tokenized text back to a string

## Installation

Install the package from PyPI using pip:

```make install```

```make build```

## Removal 

```make clean```

## Usage

Here's an example of how to use the Text Tokenizer library:

```python
from token_count import Tokenizer

tokenizer = Tokenizer()

filename = "path/to/your/text/file.txt"
token_count = tokenizer.count_tokens(filename)
print(f"Number of tokens: {token_count}")

chunks = tokenizer.break_up_file_to_chunks(filename)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {len(chunk)} tokens")
```
Replace "path/to/your/text/file.txt" with the path of the file you want to process.

## To Do:

- [ ] Allow users to use it as a CLI
- [ ] Add Cost Estimator for commerical LLMs
- [ ] Add rate limiters which could be set by users

Dependencies
- nltk
- requests
