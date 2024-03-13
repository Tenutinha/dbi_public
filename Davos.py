import streamlit as st
from time import sleep
from Navegacao import make_sidebar
from autenticar.auth import verify_credentials


make_sidebar() 

col1, col2, col3 = st.columns(3)

col2.title("Área do Cliente")
col2.write("Acesse com seu `usuário` e `senha`.")

username = col2.text_input("Usuário")
password = col2.text_input("Senha", type="password")

if col2.button("Iniciar", type="primary"):
    if verify_credentials(username, password):
        st.session_state.logged_in = True
        col2.success("Seja bem-vindo!")
        sleep(0.5)
        st.switch_page("pages/0_Resumo.py")
        
    else:
        col2.error("Usuário ou senha incorreta")
