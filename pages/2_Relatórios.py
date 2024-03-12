from Navegacao import make_sidebar
import streamlit as st
import pandas as pd


make_sidebar()


# Exemplo de dados
data = {
    'ID': [1, 2, 3, 4],
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Vendas': [234, 678, 194, 399],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']
}

df = pd.DataFrame(data)

# Lista de dimensões e medidas disponíveis
dimensoes_disponiveis = ['ID', 'Nome', 'Cidade']
medidas_disponiveis = ['Vendas']

# Usando st.expander para agrupar as dimensões
with st.sidebar.expander("Dimensões"):
    dimensoes_selecionadas = []
    for dimensao in dimensoes_disponiveis:
        if st.checkbox(f'{dimensao}', key=f'dim_{dimensao}'):
            dimensoes_selecionadas.append(dimensao)

# Similarmente, agrupando medidas se necessário
with st.sidebar.expander("Medidas"):
    medidas_selecionadas = []
    for medida in medidas_disponiveis:
        if st.checkbox(f'{medida}', key=f'med_{medida}'):
            medidas_selecionadas.append(medida)

# Atualizando o DataFrame baseado nas seleções
colunas_selecionadas = dimensoes_selecionadas + medidas_selecionadas
df_filtrado = df[colunas_selecionadas] if colunas_selecionadas else pd.DataFrame()

# Exibindo a tabela se houver pelo menos uma coluna selecionada
if not df_filtrado.empty:
    st.table(df_filtrado)
else:
    st.write("Por favor, selecione pelo menos uma dimensão ou medida para visualizar a tabela.")
