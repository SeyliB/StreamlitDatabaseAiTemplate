import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
load_dotenv('.env')
api_key = os.getenv('API_KEY')

# Interface Streamlit
st.title("🤖 Chatbot IA avec Gemini")
st.write("Pose-moi une question !")

st.write("API Key:", api_key)  # This will likely be hidden

# Entrée utilisateur
user_input = st.text_input("💬 Votre question :", "")

# Si on souhaite intégrer la génération de code python via l'API Google
if st.button("Générer du code") and user_input:
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-pro-exp-02-05", contents=user_input
    )
    st.write("### 🤖 Code généré :")
    st.code(response.text)
