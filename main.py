import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the pre-trained T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./text_summarizer")
tokenizer = T5Tokenizer.from_pretrained("./text_summarizer")

# Function to summarize text
def generate_summary(text):
    # Encode the input text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate summary
    summary_ids = model.generate(inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    
    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Streamlit app
st.title("Text summarization app")
st.header("This app summarizes text using a pre-trained T5 model.")
st.write("Enter the text you want to summarize below:")
text_input = st.text_area("Input Text", height=300, placeholder="Paste your text here...")
if st.button("Generate Summary"):
    if text_input:
        with st.spinner("Generating summary..."):
            summary = generate_summary(text_input)
        st.subheader("Generated Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")