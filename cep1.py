import streamlit as st
import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            st.error("❌ CEP não encontrado.")
        else:
            st.success("✅ Consulta realizada com sucesso!")
            st.write(f"**Logradouro:** {dados['logradouro']}")
            st.write(f"**Bairro:** {dados['bairro']}")
            st.write(f"**Cidade:** {dados['localidade']}")
            st.write(f"**Estado:** {dados['uf']}")
    else:
        st.error("❌ Erro na consulta. Verifique o CEP e tente novamente.")

# Interface Streamlit
st.title("Consulta de CEP 📍")

cep_input = st.text_input("Digite o CEP (somente números):")

if st.button("Consultar"):
    if cep_input:
        consultar_cep(cep_input)
    else:
        st.warning("⚠️ Por favor, digite um CEP antes de consultar.")