import streamlit as st
import requests

def enviar_mensagem(mensagem, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensagem
    }

    resposta = requests.post(url, data=payload)

    if resposta.status_code == 200:
        st.success("✅ Mensagem enviada com sucesso!")
    else:
        st.error("❌ Erro ao enviar mensagem.")

# Interface Streamlit
st.title("Enviar mensagem para Telegram 📩")

# Campos para token e chat_id
token = st.text_input("Token do Bot", type="password")
chat_id = st.text_input("Chat ID")

# Campo para mensagem