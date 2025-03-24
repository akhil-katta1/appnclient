import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input': {'subject': input_text}})

    return response.json()['output']['content']

st.title("Poem Generator")
input_text = st.text_input("Enter a topic")
    
if input_text:
    st.write(get_openai_response(input_text))
        
    
