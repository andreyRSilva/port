import streamlit as st

# Inicializa a frota como estado persistente
if "frota" not in st.session_state:
    st.session_state.frota = [
        ["Ônibus 101", "OK"],
        ["Ônibus 102", "Manutenção"],
        ["Ônibus 103", "OK"],
        ["Ônibus 104", "Manutenção"]
    ]

# Função para exibir status da frota
def mostrar_status(frota):
    st.subheader("🚌 Status da Frota")
    for onibus, status in frota:
        if status == "OK":
            st.write(f"✅ {onibus}: funcionando normalmente")
        elif status == "Manutenção":
            st.write(f"🛠️ {onibus}: em manutenção")
        else:
            st.write(f"❓ {onibus}: status desconhecido")

# Interface Streamlit
st.title("Monitoramento da Frota de Ônibus")

mostrar_status(st.session_state.frota)

st.subheader("🔧 Atualizar Status")

numero = st.text_input("Número do ônibus (ex: 101)")
novo_status = st.selectbox("Novo status", ["OK", "Manutenção"])
if st.button("Atualizar"):
    atualizado = False
    for linha in st.session_state.frota:
        if numero in linha[0]:
            linha[1] = novo_status
            atualizado = True
            st.success("✅ Status atualizado com sucesso!")
            break
    if not atualizado:
        st.error("❌ Ônibus não encontrado.")