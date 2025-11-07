import streamlit as st

# Função para calcular a média das notas
def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

# Função para verificar a situação do aluno
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

# Interface Streamlit
st.title("📚 Verificador de Situação Escolar")

st.write("Informe as três notas do aluno:")

nota1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1)
nota2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1)
nota3 = st.number_input("Nota 3", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Calcular Média"):
    notas = [nota1, nota2, nota3]
    media_final = calcular_media(notas)
    situacao = verificar_situacao(media_final)

    st.write(f"**Média final:** {media_final:.2f}")
    st.write(f"**Situação:** {situacao}")