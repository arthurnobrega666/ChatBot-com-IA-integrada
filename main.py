import streamlit as st
from openai import OpenAI

# coloque sua nova chave aqui temporariamente
cliente = OpenAI(api_key="chave_pessoal_openAI")

st.title("ChatBot com IA do Arthur")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# exibir histórico
for mensagem in st.session_state["lista_mensagens"]:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

texto_usuario = st.chat_input("Digite aqui sua mensagem")

if texto_usuario:
    # mostrar mensagem do usuário
    st.session_state["lista_mensagens"].append({
        "role": "user",
        "content": texto_usuario
    })

    with st.chat_message("user"):
        st.write(texto_usuario)

    # chamada da IA
    resposta = cliente.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state["lista_mensagens"]
    )

    texto_resposta_ia = resposta.choices[0].message.content

    # mostrar resposta
    with st.chat_message("assistant"):
        st.write(texto_resposta_ia)

    # salvar no histórico
    st.session_state["lista_mensagens"].append({
        "role": "assistant",
        "content": texto_resposta_ia
    })