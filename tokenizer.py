import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("ChatGPT is awesome!")
print(tokens)  # Output: [12643, 29278, 318, 11722, 0]
print([enc.decode([t]) for t in tokens])