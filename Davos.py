import streamlit as st
from time import sleep
from Navegacao import make_sidebar
from autenticacao.auth import verify_credentials



make_sidebar()

st.title("Davos")

st.write("Acesse com seu `usuário` e `senha`.")

username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

if st.button("Log in", type="primary"):
    if verify_credentials(username, password):
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/0_Resumo.py")
    else:
        st.error("Usuário ou senha incorreta")
