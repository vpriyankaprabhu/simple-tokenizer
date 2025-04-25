import streamlit as st
import tiktoken
import pandas as pd

# Set up the page
st.title("Simple Text Tokenizer")
st.write("Let's see how text is broken into tokens")

# Choose tokenizer model
tokenizer_options = ["cl100k_base", "p50k_base", "gpt2"]
selected_tokenizer = st.selectbox("Choose tokenizer model:", tokenizer_options)

# Text input box
user_text = st.text_area("Enter your text:", "The quick brown fox jumps over the lazy dog")

# Process the text
if user_text:
    # Load the tokenizer
    tokenizer = tiktoken.get_encoding(selected_tokenizer)
    
    # Convert text to tokens
    tokens = tokenizer.encode(user_text)
    
    # Get the text for each token
    token_pieces = [tokenizer.decode([t]) for t in tokens]
    
    # Display results
    st.subheader("Results")
    
    # Show token count
    st.write(f"Total tokens: {len(tokens)}")
    
    # Create a table of tokens
    results = {
        "Token ID": tokens,
        "Token Text": token_pieces
    }
    st.dataframe(pd.DataFrame(results))