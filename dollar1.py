import streamlit as st
import requests

def consultar_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        valor = dados['USDBRL']['bid']
        return valor
    else:
        return None

# Interface Streamlit
st.title("💵 Cotação do Dólar")

if st.button("Consultar cotação"):
    valor_dolar = consultar_dolar()
    if valor_dolar:
        st.success(f"Cotação atual do dólar: R$ {valor_dolar}")
    else:
        st.error("❌ Erro ao consultar a cotação.")