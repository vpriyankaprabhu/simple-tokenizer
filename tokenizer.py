import tiktoken

#enc = tiktoken.get_encoding("cl100k_base")
enc = tiktoken.get_encoding("gpt2")
tokens = enc.encode("Hello World !")
print(tokens)  # Output: [12643, 29278, 318, 11722, 0]
print([enc.decode([t]) for t in tokens])