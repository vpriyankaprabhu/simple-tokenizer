import tiktoken

#enc = tiktoken.get_encoding("cl100k_base")
enc = tiktoken.get_encoding("gpt2")
tokens = enc.encode("Hello World !")
print(tokens)  # Output: [15496, 2159, 5145]
print([enc.decode([t]) for t in tokens])