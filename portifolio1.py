import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portfólio de Andrey", page_icon="💼", layout="centered")

# Cabeçalho
st.title("💼 Portfólio de Andrey")
st.subheader("Desenvolvedor Python | Entusiasta de IA | Criador de soluções digitais")

# Sobre mim
st.markdown("## 👨‍💻 Sobre mim")
st.write("""
Olá! Sou Andrey, apaixonado por tecnologia, programação e inovação. 
Tenho experiência com Python, automações, APIs e desenvolvimento de aplicações com Streamlit.
""")

# Habilidades
st.markdown("## 🧠 Habilidades")
st.markdown("""
- ✅ Python e automações  
- ✅ Streamlit para apps interativos  
- ✅ Integração com APIs (Telegram, ViaCEP, AwesomeAPI)  
- ✅ Lógica de programação e estrutura de dados  
""")

# Projetos com links
st.markdown("## 🚀 Projetos")
projetos = {
    "Consulta de CEP": {
        "descricao": "App que consulta dados de endereço via API do ViaCEP.",
        "link": "https://github.com/seuusuario/consulta-cep"
    },
    "Cotação do Dólar": {
        "descricao": "Consulta em tempo real da cotação do dólar usando AwesomeAPI.",
        "link": "https://github.com/seuusuario/cotacao-dolar"
    },
    "Monitoramento de Frota": {
        "descricao": "Interface para atualizar status de ônibus em tempo real.",
        "link": "https://github.com/seuusuario/monitoramento-frota"
    },
    "Bot Telegram": {
        "descricao": "Integração com Telegram para envio de mensagens automatizadas.",
        "link": "https://github.com/seuusuario/bot-telegram"
    }
}

for nome, dados in projetos.items():
    with st.expander(f"📌 {nome}"):
        st.write(dados["descricao"])
        st.markdown(f"[🔗 Acessar projeto]({dados['link']})")

# Contato
st.markdown("## 📬 Contato")
st.write("Você pode me encontrar nas redes abaixo ou enviar um e-mail:")

col1, col2 = st.columns(2)
with col1:
    st.markdown("[LinkedIn](https://www.linkedin.com/in/seuusuario)")
    st.markdown("[GitHub](https://github.com/seuusuario)")
with col2:
    st.markdown("[Instagram](https://instagram.com/seuusuario)")
    st.markdown("📧 Email: seuemail@exemplo.com")

# Rodapé
st.markdown("---")
st.caption("Feito com ❤️ usando Streamlit")
