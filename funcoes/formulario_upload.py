from navegacao import make_sidebar
import streamlit as st
import pandas as pd
import io
import funcoes.leitura_arquivos as lta  # Certifique-se que a função está corretamente definida
import funcoes.leitura_registros as ltr  # Certifique-se que a função está corretamente definida


def formulario_upload():
        # Cria um dicionário para armazenar os DataFrames
        dfs_resultados = {}
        
        # Upload de arquivo
        arquivos = st.file_uploader("Escolha os arquivos", accept_multiple_files=True, type=['txt'])

        # Verifica se algum arquivo foi carregado
        if arquivos:
            # Exibe a mensagem de sucesso
            st.success("Arquivos carregados com sucesso!")

            # Processa cada arquivo individualmente
            for arquivo in arquivos:
                # Converte o arquivo carregado para um objeto BytesIO
                bytes_data = io.BytesIO(arquivo.getvalue())
                
                # Identifica o tipo de arquivo
                tipo = lta.leitura_tipo_arquivo(arquivo.name)
                
                # Chama a função de processamento para ler diretamente do objeto BytesIO
                dfs = lta.processar_arquivo_upload(bytes_data, tipo)
                
                # Armazena os DataFrames no dicionário usando o nome do arquivo como chave
                dfs_resultados[arquivo.name] = dfs