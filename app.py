import streamlit as st
import cohere

# Initializpie Cohere client with your API key
cohere_api_key = 'UDjAOSfIqchMsvQT5OURPfPM8C2VM2DOCYsHc47l'  # Replace with your actual API key
co = cohere.Client(cohere_api_key)

# Function to get response from Cohere model
def get_cohere_response(input_text, no_words, blog_style):
    # Create the prompt
    prompt = f"Write a blog for {blog_style} job profile for a topic '{input_text}' within {no_words} words."
    
    # Generate the response using Cohere
    response = co.generate(
        model='command-r-plus', 
        prompt=prompt,
        max_tokens=256,  # Adjust based on your needs
        temperature=0.01
    )
    
    return response.generations[0].text.strip()

st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

# Creating two more columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                               ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

# Final response
if submit:
    response = get_cohere_response(input_text, no_words, blog_style)
    st.write(response)
