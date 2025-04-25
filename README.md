# Simple Tokenizer App

This app helps you see how language models break text into tokens. You can input any text and see exactly how it gets split into smaller pieces for processing.

## What Are Tokens?

Tokens are the basic units that AI models like ChatGPT use to process text. They can be:
- Whole words, Parts of words, Punctuation marks, Spaces

## Installation Instructions

1. **Install Python requirements:**
   ```bash
   pip install streamlit tiktoken pandas
   ```

2. **Download the app file:**
   Save the `tokenizer_app.py` file to your computer.

3. **Run the app:**
   ```bash
   streamlit run tokenizer_app.py
   ```

4. **Open in browser:**
   The app will automatically open in your web browser (typically at http://localhost:8501).

## How to Use

1. Type or paste your text in the text box
2. Select a tokenizer model from the dropdown menu:
   - `cl100k_base` (Used by ChatGPT and GPT-4)
   - `p50k_base` (Used by GPT-3)
   - `gpt2` (Used by GPT-2)
3. View the results:
   - Total token count
   - Table showing each token ID and its text

## Example

Enter the text "Hello World!" and you'll see how it breaks down into tokens like:
- "Hello"
- " World" (includes a space)
- "!"

## Need Help?

If you have questions about tokenization or how to use this app, feel free to reach out!