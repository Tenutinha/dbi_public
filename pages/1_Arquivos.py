from Navegacao import make_sidebar
import streamlit as st
import pandas as pd
import io
import funcoes.leitura_arquivos as lta  # Certifique-se que a função está corretamente definida
import funcoes.leitura_registros as ltr  # Certifique-se que a função está corretamente definida
import funcoes.formulario_upload as form1

make_sidebar()

# Título do formulário
st.title("Arquivos")
st.subheader(' ', divider='rainbow')

# Cria um dicionário para armazenar os DataFrames
dfs_resultados = {}

# Expander para exibir o formulário de upload
with st.expander("1 - Formulário de Upload de Arquivos", expanded=True):
    # Captura o DataFrame retornado pela função formulario_upload
    dfs_resultados = form1.formulario_upload()

# Expander para exibir e selecionar os arquivos importados
with st.expander("2 - Arquivos Importados", expanded=True):
    nomes_arquivos = list(dfs_resultados.keys())
    arquivo_selecionado = st.selectbox("Selecione o arquivo:", nomes_arquivos)
    
    if arquivo_selecionado:
        tipos_disponiveis = list(dfs_resultados[arquivo_selecionado].keys())
        tipo_selecionado = st.selectbox("Selecione o Registro:", tipos_disponiveis)
        
        if tipo_selecionado:
            st.write(f"Arquivo {arquivo_selecionado} - Registro {tipo_selecionado}:")
            st.dataframe(dfs_resultados[arquivo_selecionado][tipo_selecionado])
