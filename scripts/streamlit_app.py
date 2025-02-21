import streamlit as st
import base64
import os
import sys

# Ensure 'scripts' folder is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from voice_input import recognize_speech  # Import speech recognition function
from nlp_processing import process_user_input as process_query  # Import NLP query processing function
from text_to_speech import speak_output  # Import Text-to-Speech function

# Function to set background image
def set_background(image_path):
    """Sets a background image for the Streamlit app."""
    with open(image_path, "rb") as file:
        image_bytes = file.read()
        encoded_string = base64.b64encode(image_bytes).decode("utf-8")
    
    bg_css = f"""
    <style>
    .stApp {{
        background: url("data:image/jpeg;base64,{encoded_string}") no-repeat center center fixed;
        background-size: cover;
    }}
    h1, h2, h3, h4, h5, h6, p, label, li, span {{
        color: white !important;
    }}
    .response-container {{
        padding: 15px;
        background-color: rgba(0, 0, 0, 0.7);  
        border-radius: 10px;
        margin-top: 10px;
        color: white;
        font-size: 16px;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# Set background image (adjust path as needed)
bg_image_path = os.path.join(os.path.dirname(__file__), "background_image1.JPG")
set_background(bg_image_path)

# Streamlit UI
st.markdown("<h1>🧳 Travel Planner Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p>Welcome to the AI-powered travel assistant!</p>", unsafe_allow_html=True)

# User can either type the query or use voice input
query = st.text_input("💬 Type your query here:", "")

# Voice input button
if st.button("🎙️ Speak Now"):
    st.write("Listening...")
    voice_text = recognize_speech()  # Capture voice input
    if voice_text:
        st.success(f"Recognized: {voice_text}")
        query = voice_text  # Automatically fill the text input with voice result
    else:
        st.error("No speech detected. Try again.")

# Process the query if provided
if query:
    st.subheader("🔍 Your Query:")
    st.markdown(f"<p class='response-container'>{query}</p>", unsafe_allow_html=True)

    # Process query using NLP
    response = process_query(query)

    # Display response in white color inside styled container
    st.subheader("🤖 Chatbot Response:")
    st.markdown(f"<div class='response-container'>{response}</div>", unsafe_allow_html=True)

    # Option to enable Text-to-Speech
    if st.button("🔊 Listen to Response"):
        speak_output(response)  # Convert response to speech
